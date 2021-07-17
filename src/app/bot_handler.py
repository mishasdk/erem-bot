from quotes_repo import QuotesRepo, QuoteData
from random import randint
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from utils import Utils


class BotHandler:
    def __init__(self, dispatcher):
        self._setup_handelers(dispatcher)
        self._quote_repo = QuotesRepo()

    def start(self, update, context):
        update.message.reply_text('Привет всем, ребята!')

    def help(self, update, context):
        update.message.reply_text('Всегда готов помочь!))')

    def roll(self, update, context):
        update.message.reply_text(str(randint(1, 100)))

    def naruto(self, update, context):
        data = self._quote_repo.get_naruto_quote()
        answer = '{}\n\n©{}'.format(data.text, data.author)
        update.message.reply_text(answer)

    def message(self, update, context):
        text = update.message.text
        if text == '/Кто лох?':
            update.message.reply_text('Есть тут один)))')
        else:    
            update.message.reply_text(
                Utils.random_from_data((
                    "Круто!",
                    "Еее бой ))!1",
                    "Превосходно",
                    "Замечательно!",
                    "Ахахахахах ллоооол) ))00)0"
                ))
            )

    def _setup_handelers(self, dispatcher):
        handelers = [
            CommandHandler('start', self.start),
            CommandHandler('help', self.help),
            CommandHandler('roll', self.roll),
            CommandHandler('naruto', self.naruto),
            MessageHandler(Filters.text, self.message)
        ]
        for handler in handelers:
            dispatcher.add_handler(handler)
