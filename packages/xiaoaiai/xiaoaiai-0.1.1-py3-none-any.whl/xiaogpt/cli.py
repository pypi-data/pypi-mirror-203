import argparse
import asyncio
import sys

from xiaogpt.config import Config
from xiaogpt.xiaogpt import MiGPT


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--hardware",
        dest="hardware",
        help="小爱 hardware",
    )
    parser.add_argument(
        "--account",
        dest="account",
        help="xiaomi account",
    )
    parser.add_argument(
        "--password",
        dest="password",
        help="xiaomi password",
    )
    parser.add_argument(
        "--openai_key",
        dest="openai_key",
        help="openai api key",
    )
    parser.add_argument(
        "--proxy",
        dest="proxy",
        help="http proxy url like http://localhost:8080",
    )
    parser.add_argument(
        "--cookie",
        dest="cookie",
        help="xiaomi cookie",
    )
    parser.add_argument(
        "--stream",
        dest="stream",
        action="store_true",
        default=None,
        help="GPT stream mode",
    )
    parser.add_argument(
        "--use_command",
        dest="use_command",
        action="store_true",
        default=None,
        help="use command to tts",
    )
    parser.add_argument(
        "--mute_xiaoai",
        dest="mute_xiaoai",
        action="store_true",
        default=None,
        help="try to mute xiaoai answer",
    )
    parser.add_argument(
        "--verbose",
        dest="verbose",
        action="store_true",
        default=None,
        help="show info",
    )
    parser.add_argument(
        "--enable_edge_tts",
        dest="enable_edge_tts",
        action="store_true",
        default=None,
        help="if use edge tts",
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--use_gpt3",
        dest="bot",
        action="store_const",
        const="gpt3",
        help="if use openai gpt3 api",
    )
    group.add_argument(
        "--use_chatgpt_api",
        dest="bot",
        action="store_const",
        const="chatgptapi",
        help="if use openai chatgpt api",
    )
    group.add_argument(
        "--use_newbing",
        dest="bot",
        action="store_const",
        const="newbing",
        help="if use newbing",
    )
    parser.add_argument(
        "--bing_cookie_path",
        dest="bing_cookie_path",
        help="new bing cookies path if use new bing",
    )
    group.add_argument(
        "--bot", dest="bot", help="bot type", choices=["gpt3", "chatgptapi", "newbing"]
    )
    parser.add_argument(
        "--config",
        dest="config",
        help="config file path",
    )
    # args to change api_base
    parser.add_argument(
        "--api_base",
        dest="api_base",
        help="specify base url other than the OpenAI's official API address",
    )
    # color1.append('white')
    currentarg = sys.argv[1:]
    if len(currentarg) == 0:
        options = ""
        print("platform:"+sys.platform)
        options = parser.parse_args(["--config", "config1.json"])
        # options = parser.parse_args()
    else:
        print("sys argv len:" + str(len(currentarg)))
        options = parser.parse_args()
    config = Config.from_options(options)

    miboy = MiGPT(config)
    loop = asyncio.get_event_loop()

    if config.test:
        miboy.test()

    loop.run_until_complete(miboy.run_forever())


if __name__ == "__main__":
    main()
