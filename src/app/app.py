from bot_handler import BotHandler
from config import Config

from telegram.ext import Updater, CommandHandler, MessageHandler

class App: 
    def __init__(self):
        self.updater = Updater(Config.token(), use_context=True)
        self.bot_handler = BotHandler(self.updater.dispatcher)

    def start(self):
        self.updater.start_polling()
        self.updater.idle()
