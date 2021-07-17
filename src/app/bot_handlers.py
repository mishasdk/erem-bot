from naruto_quotes_provider import NarutoQuotesProvider
from random import randint
from telegram.ext import CommandHandler, MessageHandler, Filters
from utils import Utils


class BotHandlers:
    _naruto_quotes_provider = NarutoQuotesProvider()

    def __init__(self):
        self._handlers = (
            CommandHandler('start', self._start),
            CommandHandler('help', self._help),
            CommandHandler('roll', self._roll),
            CommandHandler('naruto', self._naruto)
        )

    def handlers(self):
        return self._handlers

    def _start(self, update, context):
        update.message.reply_text('Привет всем, ребята!')

    def _help(self, update, context):
        update.message.reply_text('Всегда готов помочь!))')

    def _roll(self, update, context):
        update.message.reply_text(str(randint(1, 100)))

    def _naruto(self, update, context):
        quote = self._naruto_quotes_provider.provide()
        message = f"{quote['text']}\n\n©{quote['author']}"
        update.message.reply_text(message)
