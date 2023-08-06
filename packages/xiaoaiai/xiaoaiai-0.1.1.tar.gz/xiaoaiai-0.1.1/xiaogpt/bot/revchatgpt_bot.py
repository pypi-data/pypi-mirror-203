from __future__ import annotations

import re

from xiaogpt.utils import split_sentences

_reference_link_re = re.compile(r"\[\d+\]: .+?\n+")


class RevChatgpt:
    def __init__(
            self,
            access_token: str | None = None,
            proxy: str | None = None,
    ):
        self.history = []
        self.name: str = "傻妞"
        from ChatGPT.src.revChatGPT.V1 import Chatbot

        # self._robot = Chatbot(config={
        #     "email": "qssq521@gmail.com",
        #     "password": "Luozheng123",
        #     "proxy": "http://127.0.0.1:7890",
        # })
        self._robot: Chatbot = Chatbot(config={
            "access_token": access_token,

            "proxy": proxy
        })
        self.conversation_id: str = ""
        self.parent_id: str = ""

    @staticmethod
    def clean_text(s):
        s = s.replace("**", "")
        s = _reference_link_re.sub("", s)
        s = re.sub(r"\[[\^\d]+\]", "", s)
        return s.strip()

    async def ask(self, query, **options):
        # prompt = input("Enter your want ask: ")
        # print(prompt)
        response = ""
        for data in self._robot.ask(
                prompt=query,
                conversation_id=self.conversation_id,
                parent_id=self.parent_id,
        ):
            response = data["message"]
            self.conversation_id = data["conversation_id"]
            self.parent_id = data["parent_id"]
        return response

    async def ask_stream(self, query, **options):
        completion = self._robot.ask(
            conversation_id=self.conversation_id,
            parent_id=self.parent_id,
            prompt=query
        )

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
                yield diff
                current = text

        try:
            async for sentence in split_sentences(text_gen()):
                yield sentence
        finally:
            print()
