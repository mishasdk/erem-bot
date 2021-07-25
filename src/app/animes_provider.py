from shikimory_client import ShikimoryClient
from threading import Timer
from utils import Utils

UPDATE_TIMOUTE = 10

class AnimesProvider:
    _client = ShikimoryClient()
    _animes_data = []
    _timer = None

    def __init__(self):
        self._update_animes_data()

    def provide(self):
        if not self._timer or not self._timer.is_alive():
            self._restart_timer()

        return Utils.choose_random(self._animes_data)

    def _restart_timer(self):
        self._timer = Timer(UPDATE_TIMOUTE, self._update_animes_data)
        self._timer.setDaemon(True)
        self._timer.start()

    def _update_animes_data(self):
        params = {
            'limit': 50,
            'page': 1,
            'score': 8,
            'kind': 'tv',
            'order': 'random'
        }
        # TODO: Think about to set _animes_data only on mainThread
        self._animes_data = self._client.get_animes_data(params)
