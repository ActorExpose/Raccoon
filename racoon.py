from fake_useragent import UserAgent
from lib.raccoon.utils.coloring import COLOR


def intro():
    print("""{}
      _____                _____    _____    ____     ____    _   _ 
     |  __ \      /\      / ____|  / ____|  / __ \   / __ \  | \ | |
     | |__) |    /  \    | |      | |      | |  | | | |  | | |  \| |
     |  _  /    / /\ \   | |      | |      | |  | | | |  | | | . ` |
     | | \ \   / ____ \  | |____  | |____  | |__| | | |__| | | |\  |
     |_|  \_\ /_/    \_\  \_____|  \_____|  \____/   \____/  |_| \_|

    {}
    """.format(COLOR.RED, COLOR.RESET))


def main():
    UA = UserAgent()
    # tasks = [
    #     asyncio.ensure_future()),
    #     asyncio.ensure_future(),
    # ]
    # run_until_complete(asyncio.wait(tasks))
    pass
