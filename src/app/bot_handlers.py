from naruto_quotes_provider import NarutoQuotesProvider
from random import randint
from telegram.ext import CommandHandler, MessageHandler, Filters
from users_storage import UsersStorage 

class BotHandlers:
    _naruto_quotes_provider = NarutoQuotesProvider()
    _users_storage = UsersStorage()

    def __init__(self):
        self._handlers = (
            CommandHandler('start', self._start),
            CommandHandler('help', self._help),
            CommandHandler('roll', self._roll),
            CommandHandler('naruto', self._naruto),
            CommandHandler('who_is_dumb', self._poll_dumb),
            CommandHandler('hello', self._hello)
        )

    def handlers(self):
        return self._handlers

    def _start(self, update, context):
        self._save_username(update)

        update.message.reply_text('Здарова всем, ребята!!!')

    def _help(self, update, context):
        self._save_username(update)

        update.message.reply_text('Всегда готов помочь!))')

    def _roll(self, update, context):
        self._save_username(update)

        update.message.reply_text(str(randint(1, 100)))

    def _naruto(self, update, context):
        self._save_username(update)

        quote = self._naruto_quotes_provider.provide()
        message = f"{quote['text']}\n\n©{quote['author']}"
        update.message.reply_text(message)

    def _poll_dumb(self, update, context):
        self._save_username(update)

        chat_id = update.effective_chat.id        
        username = BotHandlers._username_by_user(update.effective_user)

        usernames = self._users_storage.get_usernames(chat_id)
        if len(usernames) < 2:
            context.bot.send_message(chat_id, f'Не могу начать голосование, я еще не достаточно вас знаю!')
            return

        context.bot.send_message(chat_id, f'{username} начинает голосование!')
        context.bot.send_poll(
            chat_id,
            'Кто пидор?',
            usernames,
            is_anonymous=True,
            allows_multiple_answers=True,
            open_period=300
        )

    def _hello(self, update, context):
        chat_id = update.effective_chat.id
        user = update.effective_user
        username = user.username
        firstname = user.first_name
        usernames = self._users_storage.get_usernames(chat_id)
        if not username in self._users_storage.get_usernames(chat_id):
            context.bot.send_message(chat_id, f'Я с незнакомцами, не знакомлюсь!')
        else:
            update.message.reply_text('Здарова ' + f'{firstname}!' + ' Как делишки?))0)')

    def _save_username(self, update):
        chat_id = update.effective_chat.id        
        self._users_storage.try_save_user(update.effective_user, chat_id)

    @staticmethod
    def _username_by_user(user):
        username = ''
        if not user.first_name:
            username = user.username
        else:
            if user.first_name:
                username = user.first_name 
            if user.last_name:
                username += f" {user.last_name}"
        return username
