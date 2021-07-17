from argparse import ArgumentParser
from bot_handlers import BotHandlers
from telegram.ext import Updater


class BotApp: 
    _bot_handlers = BotHandlers()

    def __init__(self, tg_token):
        self._updater = Updater(tg_token)

        for handler in self._bot_handlers.handlers():
            self._updater.dispatcher.add_handler(handler)

    def run(self):
        self._updater.start_polling()
        self._updater.idle()


def main(args):
    BotApp(args.tg_token).run()


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--tg_token')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    main(args)
