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
        text = text.replace("这里是必应", "")
        text = text.replace("我是必应", "")
        text = text.replace("必应", "")
        text = text.replace("。", "")
        text = text.replace("，", "")
        return text

        # await self._bot.close()

    async def ask_stream(self, query, **options):

        completion = self._bot.ask(query)

        async def text_gen():
            current = ""
            yield diff
            current = completion
            async for final, resp in completion:
                if final:
                    break
                text = self.clean_text(resp)
                if text == current:
                    continue
                diff = text[len(current):]
                print(diff, end="")
                yield diff
                current = text

        try:
            async for sentence in text_gen():
                yield sentence
        finally:
            print()
