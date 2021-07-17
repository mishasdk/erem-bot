from bot_handler import BotHandler
from telegram.ext import Updater, CommandHandler, MessageHandler


class App: 
    def __init__(self, tg_token):
        self._updater = Updater(tg_token, use_context=True)
        self._bot_handler = BotHandler(self._updater.dispatcher)

    def run(self):
        self._updater.start_polling()
        self._updater.idle()
