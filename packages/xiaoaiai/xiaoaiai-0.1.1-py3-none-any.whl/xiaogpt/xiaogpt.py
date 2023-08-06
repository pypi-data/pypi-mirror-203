#!/usr/bin/env python3
import asyncio
import datetime
import functools
import http.server
import json
import logging
import os
import random
import re
import socket
import socketserver
import sys
import tempfile
import threading
import time
import traceback
# from datetime import datetime
from pathlib import Path

import edge_tts
import openai
from aiohttp import ClientSession
from miservice import MiAccount, MiIOService, MiNAService, miio_command
from rich import print
from rich.logging import RichHandler

from xiaogpt.bot import ChatGPTBot, GPT3Bot, NewBingBot
from xiaogpt.bot.newbing_acheongbot import NewBingAcheongBot
from xiaogpt.bot.revchatgpt_bot import RevChatgpt
from xiaogpt.bot.stringcontain import StringConcatenator
from xiaogpt.config import (
    COOKIE_TEMPLATE,
    EDGE_TTS_DICT,
    LATEST_ASK_API,
    MI_ASK_SIMULATE_DATA,
    WAKEUP_KEYWORD,
    Config,
)

from xiaogpt.utils import (
    calculate_tts_elapse,
    find_key_by_partial_string,
    get_hostname,
    parse_cookie_string,
)

EOF = object()


class ThreadedHTTPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class HTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    logger = logging.getLogger("xiaogpt")

    def log_message(self, format, *args):
        self.logger.debug(f"{self.address_string()} - {format}", *args)

    def log_error(self, format, *args):
        traceback.print_exc()
        self.logger.error(f"{self.address_string()} - {format}", *args)

    def copyfile(self, source, outputfile):
        try:
            super().copyfile(source, outputfile)
        except (socket.error, ConnectionResetError, BrokenPipeError):
            # ignore this or TODO find out why the error later
            pass


class MiGPT:
    def __init__(self, config: Config):
        self.config = config
        self.mi_token_home = Path.home() / ".mi.token"
        self.last_timestamp = int(time.time() * 1000)  # timestamp last call mi speaker
        self.last_record = None
        self.cookie_jar = None
        self._chatbot = None
        self.device_id = ""
        self.parent_id = None
        self.mina_service: MiNAService = None  # MiNAService(account)
        self.miio_service: MiIOService = None  # MiIOService(account)
        self.in_conversation = False
        self.polling_event = asyncio.Event()
        self.new_record_event = asyncio.Event()
        self.temp_dir = None

        # setup logger
        self.log = logging.getLogger("xiaogpt")
        self.log.setLevel(logging.DEBUG if config.verbose else logging.INFO)
        self.log.addHandler(RichHandler())
        self.log.debug(config)
        if sys.platform.startswith("win"):
            from xiaogpt.toast import ToastUtil
            self.toast = ToastUtil()
        self.toast.setFontSize(25)
        self.toast.setGravity(0)
        # self.toast.setWindowSize(0, 0)
        self.toast.setLocationOffsize(15, 15)
        self.print_screen("小爱同学音响已接入人工智能智能Chatgpt和新必应")

    async def poll_latest_ask(self):
        async with ClientSession() as session:
            session._cookie_jar = self.cookie_jar
            while True:
                if self.config.detailverbose:
                    self.log.debug(
                        "从小爱云中拉取新消息 timestamp: %s",
                        self.last_timestamp,
                    )
                await self.get_latest_ask_from_xiaoai(session)
                start = time.perf_counter()
                # if self.new_record_event.is_set():
                #     continue
                await self.polling_event.wait()  # event.isSet()==False将阻塞线程，event建立后默认为False
                if (d := time.perf_counter() - start) < 1:
                    # sleep to avoid too many request
                    await asyncio.sleep(1 - d)

    async def init_all_data(self, session):
        await self.login_miboy(session)
        await self._init_data_hardware()
        session.cookie_jar.update_cookies(self.get_cookie())
        self.cookie_jar = session.cookie_jar
        if self.config.enable_edge_tts:
            self.start_http_server()

    async def login_miboy(self, session):
        account = MiAccount(
            session,
            self.config.account,
            self.config.password,
            str(self.mi_token_home),
        )
        # Forced login to refresh to refresh token
        await account.login("micoapi")
        self.mina_service: MiNAService = MiNAService(account)
        self.miio_service: MiIOService = MiIOService(account)

    async def _init_data_hardware(self):
        if self.config.cookie:
            # if use cookie do not need init
            return
        hardware_data = await self.mina_service.device_list()
        # fix multi xiaoai problems we check did first
        # why we use this way to fix?
        # some videos and articles already in the Internet
        # we do not want to change old way, so we check if miotDID in `env` first
        # to set device id

        for h in hardware_data:
            if did := self.config.mi_did:
                if h.get("miotDID", "") == str(did):
                    self.device_id = h.get("deviceID")
                    break
                else:
                    continue
            if h.get("hardware", "") == self.config.hardware:
                self.device_id = h.get("deviceID")
                break
        else:
            raise Exception(
                f"we have no hardware: {self.config.hardware} please use `micli mina` to check"
            )
        if not self.config.mi_did:
            devices = await self.miio_service.device_list()
            try:
                self.config.mi_did = next(
                    d["did"]
                    for d in devices
                    if d["model"].endswith(self.config.hardware.lower())
                )
            except StopIteration:
                raise Exception(
                    f"cannot find did for hardware: {self.config.hardware} "
                    "please set it via MI_DID env"
                )

    def get_cookie(self):
        if self.config.cookie:
            cookie_jar = parse_cookie_string(self.config.cookie)
            # set attr from cookie fix #134
            cookie_dict = cookie_jar.get_dict()
            self.device_id = cookie_dict["deviceId"]
            return cookie_jar
        else:
            with open(self.mi_token_home) as f:
                user_data = json.loads(f.read())
            user_id = user_data.get("userId")
            service_token = user_data.get("micoapi")[1]
            cookie_string = COOKIE_TEMPLATE.format(
                device_id=self.device_id, service_token=service_token, user_id=user_id
            )
            return parse_cookie_string(cookie_string)

    @property
    def chatbot(self):
        if self._chatbot is None:
            if self.config.bot == "gpt3":
                self._chatbot = GPT3Bot(
                    self.config.openai_key, self.config.api_base, self.config.proxy
                )
            elif self.config.bot == "revchatgpt" or self.config.bot == "模式一" or self.config.bot == "模式1":
                self._chatbot = RevChatgpt(
                    self.config.access_token, self.config.proxy
                )
            elif self.config.bot == "chatgptapi":
                self._chatbot = ChatGPTBot(
                    self.config.openai_key, self.config.api_base, self.config.proxy
                )
            elif self.config.bot == "newbing":
                self._chatbot = NewBingBot(
                    bing_cookie_path=self.config.bing_cookie_path,
                    bing_cookies=self.config.bing_cookies,
                    proxy=self.config.proxy,
                )
            elif self.config.bot == "newbing1" or self.config.bot == "模式二" or self.config.bot == "模式2":
                self._chatbot = NewBingAcheongBot(
                    bing_cookie_path=self.config.bing_cookie_path,
                    bing_cookies=self.config.bing_cookies,
                    proxy=self.config.proxy,
                )
            else:
                raise Exception(f"Do not support {self.config.bot}")
        return self._chatbot

    async def simulate_xiaoai_question(self):
        data = MI_ASK_SIMULATE_DATA
        # Convert the data['data'] value from a string to a dictionary
        data_dict = json.loads(data["data"])
        # Get the first item in the records list
        record = data_dict["records"][0]
        # Replace the query and time values with user input
        record["query"] = input("Enter the new query: ")
        record["time"] = int(time.time() * 1000)
        # Convert the updated data_dict back to a string and update the data['data'] value
        data["data"] = json.dumps(data_dict)
        await asyncio.sleep(1)

        return data

    def need_ask_gpt(self, record):
        query: str = record.get("query", "")
        return (
                self.in_conversation
                and not query.startswith(WAKEUP_KEYWORD)
                or query.startswith(tuple(self.config.keyword))
        )

    def need_change_prompt(self, record):
        if self.config.bot == "gpt3":
            return False
        query = record.get("query", "")
        return query.startswith(tuple(self.config.change_prompt_keyword))

    def _change_prompt(self, new_prompt):
        new_prompt = re.sub(
            rf"^({'|'.join(self.config.change_prompt_keyword)})", "", new_prompt
        )
        new_prompt = "以下都" + new_prompt
        print(f"Prompt from {self.config.prompt} change to {new_prompt}")
        self.config.prompt = new_prompt
        if self.chatbot.history:
            print(self.chatbot.history)
            self.chatbot.history[0][0] = new_prompt

    async def get_latest_ask_from_xiaoai(self, session):
        retries = 2
        for _ in range(retries):
            r = await session.get(
                LATEST_ASK_API.format(
                    hardware=self.config.hardware,
                    timestamp=str(int(time.time() * 1000)),
                )
            )
            try:
                data = await r.json()
            except Exception:
                self.log.warning("get latest ask from xiaoai error, retry")
            else:
                try:
                    self._get_last_query(data)
                except Exception as e:
                    traceback.print_exc()
                    self.log.warning("轮询处理逻辑出现错误" + str(e))

    def _get_last_query(self, data):
        if d := data.get("data"):
            records = json.loads(d).get("records")
            if not records:
                return
            last_record = records[0]
            timestamp = last_record.get("time")
            systemTime = int(datetime.datetime.now().timestamp())
            timeLastMsgDistance: int = (self.last_timestamp - timestamp) / 1000
            timeDistance: int = systemTime - (timestamp / 1000)
            currentAsk: str = last_record.get("query")
            if self.config.detailverbose:
                ten_timeArray = time.localtime(timestamp / 1000)
                ten_otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", ten_timeArray)
                print("当前消息[" + ten_otherStyleTime + "]" + currentAsk + "和上一条消息间隔:" + str(
                    timeLastMsgDistance) + ",当前时间和新消息间隔:" + str(timeDistance))
            if timestamp == self.last_timestamp and timeDistance > 3:
                if self.config.detailverbose:
                    print(
                        "忽略相同消息,消息内容为:" + currentAsk + "间隔:" + str(timeDistance) + ",两条消息间隔:" + str(
                            timeLastMsgDistance))
            elif timeDistance < 1 and timeLastMsgDistance < 0 or timeLastMsgDistance < 0:  # or timeDistance < 600:  # 忽略距离凶弹时间过长消息,
                self.last_timestamp = timestamp
                self.last_record = last_record
                self.new_record_event.set()
                ten_timeArray = time.localtime(timestamp / 1000)
                ten_otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", ten_timeArray)
                print(
                    "加入新消息到处理队列:消息内容为:" + currentAsk + "間隔現在時間:" + ten_otherStyleTime + ",间隔:" + str(
                        timeDistance) + ",两条消息间隔:" + str(timeLastMsgDistance))
            else:
                if self.config.detailverbose:
                    print("忽略消息" + currentAsk + ",间隔" + str((self.last_timestamp - timestamp) / 1000) + "秒")

    async def do_tts(self, value, wait_for_finish=False):
        if not self.config.use_command:
            try:
                await self.mina_service.text_to_speech(self.device_id, value)
            except Exception:
                pass
        else:
            await miio_command(
                self.miio_service,
                self.config.mi_did,
                f"{self.config.tts_command} {value}",
            )
        if wait_for_finish:
            elapse = calculate_tts_elapse(value)
            await asyncio.sleep(elapse)
            await self.wait_for_tts_finish()

    def do_tts_asyncsend(self, text: str, delay: float = 15, beforeCloseVoice: bool = True):
        #     asyncio.run(self.do_tts_asyncsend_async(str,delay))
        # def do_tts_asyncsend_async(self, text: str, delay: int):
        async def my_coroutine(text: str, delay: float, beforeClose: bool):
            await asyncio.sleep(delay)
            if beforeClose:
                await self.stop_if_xiaoai_is_playing()
                await asyncio.sleep(0.3)
            try:
                await self.do_tts(text)
            except Exception as e:
                print("语言提示失败," + text + "," + str(e))

        future = asyncio.ensure_future(my_coroutine(text, delay, beforeCloseVoice))
        future.add_done_callback(lambda _: {})

        # async def async_read_voice( text: str, delay: int):
        #     await asyncio.sleep(delay)
        #     await self.do_tts(text)
        #     print("Async function called after {} seconds with text: {}".format(delay, text))
        #
        # t = threading.Thread(target=asyncio.run, args=(async_read_voice(text, delay),))
        # t.start()

    async def wait_for_tts_finish(self):
        while True:
            if not await self.get_if_xiaoai_is_playing():
                break
            await asyncio.sleep(1)

    def start_http_server(self):
        # set the port range
        port_range = range(8050, 8090)
        # get a random port from the range
        self.port = int(self.config.port) if self.config.port is not None else random.choice(port_range)
        self.temp_dir = tempfile.TemporaryDirectory(prefix="xiaogpt-tts-")
        # create the server
        handler = functools.partial(HTTPRequestHandler, directory=self.temp_dir.name)
        httpd = ThreadedHTTPServer(("", self.port), handler)
        # start the server in a new thread
        server_thread = threading.Thread(target=httpd.serve_forever)
        server_thread.daemon = True
        server_thread.start()

        self.hostname = get_hostname()
        print("hostname" + self.hostname + ",tempdir:" + str(self.temp_dir.name))
        self.log.info(f"Serving on {self.hostname}:{self.port}")

    async def text2mp3(self, text, tts_lang):
        communicate = edge_tts.Communicate(text, tts_lang)
        duration = 0
        with tempfile.NamedTemporaryFile(
                "wb", suffix=".mp3", delete=False, dir=self.temp_dir.name
        ) as f:
            async for chunk in communicate.stream():
                if chunk["type"] == "audio":
                    f.write(chunk["data"])
                elif chunk["type"] == "WordBoundary":
                    duration = (chunk["offset"] + chunk["duration"]) / 1e7
            if duration == 0:
                raise RuntimeError(f"Failed to get tts from edge with voice={tts_lang}")
            return (
                f"http://{self.hostname}:{self.port}/{os.path.basename(f.name)}",
                duration,
            )

    async def edge_tts(self, text_stream, tts_lang):
        async def run_tts(text_stream, tts_lang, queue):
            async for text in text_stream:
                try:
                    url, duration = await self.text2mp3(text, tts_lang)
                except Exception as e:
                    self.log.error(e)
                    continue
                await queue.put((url, duration))

        queue = asyncio.Queue()
        self.log.debug("Edge TTS with voice=%s", tts_lang)
        task = asyncio.create_task(run_tts(text_stream, tts_lang, queue))
        task.add_done_callback(lambda _: queue.put_nowait(EOF))
        while True:
            item = await queue.get()
            if item is EOF:
                break
            url, duration = item
            self.log.debug(f"play: {url}")
            await self.mina_service.play_by_url(self.device_id, url)
            await asyncio.sleep(duration)
            await self.wait_for_tts_finish()
        task.cancel()

    @staticmethod
    def _normalize(message):
        message = message.strip().replace(" ", "--")
        message = message.replace("\n", "，")
        message = message.replace('"', "，")
        return message

    async def ask_gpt(self, query: str):
        if not self.config.stream:
            async with ClientSession(trust_env=True) as session:
                openai.aiosession.set(session)
                answer = await self.chatbot.ask(query, **self.config.gpt_options)
                message = self._normalize(answer) if answer else ""
                yield message
                return

        async def collect_stream(queue):
            async with ClientSession(trust_env=True) as session:
                try:
                    concatenator = StringConcatenator()
                    mystr: str = ""

                    openai.aiosession.set(session)
                    async for message in self.chatbot.ask_stream(
                            query, **self.config.gpt_options
                    ):
                        mystr += message
                        print("[" + message + "]")
                        self.print_screen(mystr)  # concatenator.get_string())
                        await queue.put(message)
                except Exception as e:
                    print("stream消息出现异常，" + str(e))
                    await queue.put(query + "出现异常，" + str(e))

        def done_callback(future):
            queue.put_nowait(EOF)
            if future.exception():
                self.log.error(future.exception())

        self.polling_event.set()
        queue = asyncio.Queue()
        is_eof = False
        task = asyncio.create_task(collect_stream(queue))
        task.add_done_callback(done_callback)
        while True:
            if is_eof or self.new_record_event.is_set():
                break
            message = await queue.get()
            if message is EOF:
                break
            while not queue.empty():
                if (next_msg := queue.get_nowait()) is EOF:
                    is_eof = True
                    break
                message += next_msg
            if message:
                yield self._normalize(message)
        self.polling_event.clear()
        task.cancel()

    async def get_if_xiaoai_is_playing(self):
        playing_info = await self.mina_service.player_get_status(self.device_id)
        # WTF xiaomi api
        is_playing = (
                json.loads(playing_info.get("data", {}).get("info", "{}")).get("status", -1)
                == 1
        )
        return is_playing

    async def stop_xiaomi(self):
        self.mina_service.player_set_volume(self.device_id, "43")
        from miservice.cli import micli

    async def stop_if_xiaoai_is_playing(self):
        # is_playing = await self.get_if_xiaoai_is_playing()
        # if is_playing:
        #     # stop it
        await self.mina_service.player_pause(self.device_id)

    async def wakeup_xiaoai(self):
        return await miio_command(
            self.miio_service,
            self.config.mi_did,
            f"{self.config.wakeup_command} {WAKEUP_KEYWORD} 0",
        )

    async def run_forever(self):
        async with ClientSession() as session:
            await self.init_all_data(session)
            task = asyncio.create_task(self.poll_latest_ask())
            assert task is not None  # to keep the reference to task, do not remove this
            print(f"Running xiaogpt now, 用`{'/'.join(self.config.keyword)}`开头来提问")
            print(
                f"或用`{self.config.start_conversation}`开始持续对话\n对小爱说 关闭/安静模式 将关闭打断小爱的回答, 关闭/调试模式 将开启更详细的日志\n切换模式 将从新必应和chatgpt模式中切换")
            while True:
                if self.config.test:
                    await asyncio.sleep(2)
                    task.cancel()
                    continue
                # if (not self.new_record_event.is_set()):
                #     await self.new_record_event.wait() #可能有點bug, 双锁
                self.polling_event.set()  # poll消息

                if (not self.new_record_event.is_set()):
                    # if self.config.verbose:
                    # print("等待新消息")
                    # time.sleep(1)
                    await asyncio.sleep(0.1)
                    continue

                self.polling_event.clear()  # 不拉取新消息,isset=false waiting了
                new_record = self.last_record
                self.new_record_event.clear()

                query: str = new_record.get("query", "").strip()
                self.print_screen("语音提问:" + query)
                if self.config.detailverbose:
                    print("对新消息进行判断:" + query)
                if query.startswith(
                        tuple(
                            self.config.start_conversation)):  # query == self.config.start_conversation or self.config.start_conversation.find(query) >= 0:
                    if not self.in_conversation:
                        await self.stop_if_xiaoai_is_playing()
                        await asyncio.sleep(6)
                        print("开始对话")
                        self.in_conversation = True
                        await self.wakeup_xiaoai()
                        # await self.wakeup_xiaoai()
                    else:
                        await self.stop_if_xiaoai_is_playing()
                        await asyncio.sleep(3)
                        print("已经是打开状态,再次幻想开始对话")
                        await self.wakeup_xiaoai()
                    continue

                elif query.startswith(tuple(self.config.end_conversation)):  # query == self.config.end_conversation:
                    if self.in_conversation:
                        print("结束对话")
                        self.in_conversation = False
                    await self.stop_if_xiaoai_is_playing()
                    continue

                # we can change prompt
                if self.need_change_prompt(new_record):
                    print(new_record)
                    self._change_prompt(new_record.get("query", ""))

                if not self.config.answerall and self.need_ask_gpt(new_record) and not query.find("小爱同学") == 0:
                    self.log.debug("No new xiao ai record")
                    continue
                # drop 帮我回答
                query = re.sub(rf"^({'|'.join(self.config.keyword)})", "", query)
                print("-" * 20)
                print("正在处理问题：" + query + "？")
                if query.find("关闭音乐") == 0:
                    continue
                elif query.find("调试") >= 0:
                    print("已开启调试")
                    isOnDebug: bool = True
                    if query.find("关闭") >= 0:
                        isOnDebug: bool = False
                    self.config.detailverbose = isOnDebug
                    self.config.verbose = isOnDebug
                    await self.stop_if_xiaoai_is_playing()
                    await asyncio.sleep(0.3)
                    if isOnDebug:
                        await self.do_tts("已开启调试,当前日志会更详细")
                    else:
                        await self.do_tts("已关闭调试,日志将只会显示重要部分")
                    continue
                elif query.find("静默") >= 0 or query.find("安静") >= 0:
                    isOn: bool = True
                    if query.find("关闭") >= 0:
                        isOn: bool = False
                    self.config.mute_xiaoai = isOn
                    await self.stop_if_xiaoai_is_playing()
                    await asyncio.sleep(0.1)
                    if isOn:
                        await self.do_tts("已开启静默模式,小爱的回答将会中断")
                    else:
                        await self.do_tts("已关闭静默模式,小爱回答后人工智能回答")
                    continue
                elif query.find("切换") >= 0 and query.find("模式"):
                    await self.stop_if_xiaoai_is_playing()
                    await asyncio.sleep(0.3)
                    if self.config.bot == "newbing1" or self.config.bot == "模式2":
                        self.config.bot = "模式1"  # 切换为revchatgpt
                        await self.do_tts("已切换为傻妞模式")
                    elif self.config.bot == "revchatgpt" or self.config.bot == "模式1":
                        self.config.bot = "模式2"  # 切换为biying
                        await self.do_tts("已切换为太子模式")
                    else:
                        self.config.bot = "模式2"  # 切换为biying
                        await self.do_tts("已切换为太子模式")

                    self._chatbot = None
                    continue
                if not self.chatbot.history:
                    print("not in history------------------------------------")
                    # query = {query}#f"{query}，{self.config.prompt}"
                starttime = datetime.datetime.now()
                if self.config.mute_xiaoai:
                    await self.stop_if_xiaoai_is_playing()
                    # await asyncio.sleep(2)
                    # await self.do_tts("" + self._chatbot.name + "思考正在帮你解答,你刚刚说的是"+query)
                    self.print_screen(query + ",关于这个问题" + self._chatbot.name + "正在帮你解答,请耐心等待")
                    await self.do_tts(query + ",关于这个问题" + self._chatbot.name + "正在帮你解答,请耐心等待",
                                      wait_for_finish=False)
                    # self.do_tts_asyncsend("" + self._chatbot.name + "思考中,稍后回答你", 1.4, False)
                else:

                    print("等待小爱同学回答完毕")
                    # waiting for xiaoai speaker done
                    # await asyncio.sleep(8)

                try:
                    print(
                        "以下是小爱的回答: ",
                        new_record.get("answers", [])[0].get("tts", {}).get("text"),
                    )
                except Exception as e:
                    print("小爱没回或需要等会才能获取到" + str(e))
                print("正在等待人工智能" + self.config.bot + "的回答: ", end="")
                try:
                    askresult: str = ""
                    if not self.config.enable_edge_tts:
                        async for message in self.ask_gpt(query + self.config.prompt):
                            askresult = message
                            beforequery = new_record.get("query", "").strip()
                            if not beforequery == query:
                                print(
                                    "忽略被打断的提问:" + query + "|现在提问:" + beforequery + "\n答案：" + beforequery)
                                continue
                            if (len(message.replace("\n", "").replace("\r\n", "").strip()) < 2):
                                await self.do_tts(message + " 抱歉，回答出现错误请重新提问", wait_for_finish=True)
                            else:
                                await self.do_tts(message, wait_for_finish=True)
                    else:
                        tts_lang = (
                                find_key_by_partial_string(EDGE_TTS_DICT, query)
                                or self.config.edge_tts_voice
                        )
                        async for message in self.ask_gpt(tts_lang + self.config.prompt):
                            askresult = message
                            beforequery = new_record.get("query", "").strip()
                            if not beforequery == query:
                                print(
                                    "忽略被打断的提问:" + query + "|现在提问:" + beforequery + "\n答案：" + beforequery)
                                continue
                            if (len(message.replace("\n", "").replace("\r\n", "").strip()) < 2):
                                await self.do_tts(message + " 抱歉，回答出现错误请重新提问", wait_for_finish=True)
                            else:
                                await self.do_tts(message, wait_for_finish=True)
                            await self.do_tts(message, wait_for_finish=True)
                        # tts with edge_tts
                        await self.edge_tts(askresult, tts_lang)
                    endtime: datetime = datetime.datetime.now()
                    # print((endtime - starttime).seconds)
                    print("回答完毕 -> 耗时(" + str((endtime - starttime).seconds) + "s)" + askresult)
                    if self.in_conversation:
                        await self.wakeup_xiaoai()
                except Exception as e:
                    traceback.print_exc()
                    # if self.config.detailverbose:
                    await self.do_tts("抱歉,人工智能回答出现了故障,请检查日志", wait_for_finish=True)
                    print(f"人工智能回答出错 ,详细日志请说开启调试{str(e)}")
                    if self.in_conversation:
                        print(f"继续对话, 或用`{self.config.end_conversation}`结束对话")
                        await self.wakeup_xiaoai()

    def test(self):
        loop = asyncio.get_event_loop()

        async def testloop():
            async with ClientSession() as session:
                await self.init_all_data(session)
                task = asyncio.create_task(self.poll_latest_ask())
                assert task is not None  # to keep the reference to task, do not remove this
                print("测试中11111111111111111111111111111111111111111111111111")
                # await self.stop_if_xiaoai_is_playing()
                self.do_tts_asyncsend("你3333333好", 5)
                print("xxx")

                # await self.wakeup_xiaoai()
                # await self.wakeup_xiaoai()

        loop.run_until_complete(testloop())

    def print_screen(self, message):
        self.toast.showToastForever(message)
        pass


pass
