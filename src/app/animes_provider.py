from shikimory_client import ShikimoryClient
from utils import Utils
import threading
import time

UPDATE_TIMOUTE = 300

class AnimesProvider:
    _client = ShikimoryClient()
    _animes_data = []

    def __init__(self):
        self._update_thread = threading.Thread(target=self._update_animes_data_async)
        self._update_thread.setDaemon(True)
        self._update_thread.start()

    def provide(self):
        return Utils.choose_random(self._animes_data)

    def _update_animes_data_async(self):
        params = {
            'limit': 50,
            'page': 1,
            'score': 8,
            'kind': 'tv',
            'order': 'random'
        }
        # TODO: Think about to set _animes_data only on mainThread
        self._animes_data = self._client.get_animes_data(params)
        time.sleep(UPDATE_TIMOUTE)
