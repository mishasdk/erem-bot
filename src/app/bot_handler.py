from utils import Utils

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

class BotHandler:
    def __init__(self, dispatcher):
        dispatcher.add_handler(CommandHandler('start', self.start))
        dispatcher.add_handler(CommandHandler('help', self.help))
        dispatcher.add_handler(MessageHandler(Filters.text, self.message))

    def start(self, update, context):
        update.message.reply_text('Привет всем, ребята!')

    def help(self, update, context):
        update.message.reply_text('Всегда готов помочь!))')

    def message(self, update, context):
        text = update.message.text
        if text == '/Кто лох?':
            update.message.reply_text('Есть тут один)))')
        else:    
            update.message.reply_text(
                Utils.random_answer_from_list((
                    "Круто!",
                    "Еее бой ))!1",
                    "Превосходно",
                    "Замечательно!",
                    "Ахахахахах ллоооол) ))00)0"
                ))
            )
