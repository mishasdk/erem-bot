class UsersStorage:
    _chats = {}

    def try_save_user(self, user, chat_id):
        if chat_id not in self._chats:
            self._chats[chat_id] = {}

        self._chats[chat_id][user.id] = user.username

    def get_usernames(self, chat_id):
        if chat_id not in self._chats:
            return ()

        return [name for name in self._chats[chat_id].values()]
