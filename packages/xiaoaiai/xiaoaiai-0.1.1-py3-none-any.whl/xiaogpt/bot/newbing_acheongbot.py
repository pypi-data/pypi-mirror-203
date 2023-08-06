from __future__ import annotations

import re

import asyncio
from EdgeGPT import Chatbot, ConversationStyle
from xiaogpt.utils import split_sentences

_reference_link_re = re.compile(r"\[\d+\]: .+?\n+")


class NewBingAcheongBot:

    def __init__(
            self,
            bing_cookie_path: str = "",
            bing_cookies: dict | None = None,
            proxy: str | None = None,
    ):
        self.history = []
        self.name: str = "新必应"
        if (not proxy == None and len(proxy) == 0):
            proxy = None
        self._bot = Chatbot(
            cookiePath=bing_cookie_path, cookies=bing_cookies, proxy=proxy
        )

    # https: // github.com / acheong08 / EdgeGPT
    @staticmethod
    def clean_text(s):
        s = s.replace("**", "")
        s = _reference_link_re.sub("", s)
        s = re.sub(r"\[[\^\d]+\]", "", s)
        return s.strip()

    async def ask(self, query, **options):
        kwargs = {"conversation_style": ConversationStyle.balanced, **options}
        # completion = await self._bot.ask(prompt=query, **kwargs)
        try:
            completion = await self._bot.ask(prompt=query, conversation_style=ConversationStyle.creative,
                                             wss_link="wss://sydney.bing.com/sydney/ChatHub")
            text = self.clean_text(completion["item"]["messages"][1]["text"])
        except Exception as e:
            print("提问失败," + query + "," + str(e))
        print(text)
        text = text.replace("你好，我是必应。", "") \
            .replace("这里是必应", "") \
            .replace("我是必应", "") \
            .replace("必应", "").replace("。", "").replace("，", "")
        return text

        # await self._bot.close()

    async def ask_stream(self, query, **options):
        kwargs = {"conversation_style": ConversationStyle.balanced, **options}
        completion = self._bot.ask_stream(prompt=query, **kwargs)

        async def text_gen():
            current = ""
            async for final, resp in completion:
                if final:
                    break
                text = self.clean_text(resp)
                if text == current:
                    continue
                diff = text[len(current):]
                print(diff, end="")
                # if (not self.proyprint == None):
                #     self.proyprint(diff)
                yield diff
                current = text

        try:
            async for sentence in split_sentences(text_gen()):
                yield sentence
        finally:
            print()
