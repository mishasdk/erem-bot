import requests


class ShikimoryClient:
    _base_url = 'https://shikimori.one'
    _url = f'{_base_url}/api'

    def get_animes_data(self, params):
        url = f'{self._url}/animes'
        json = self._get(url, params)

        if len(json) is None:
            return ()

        return [{
            'name': anime['russian'], 
            'image': self._base_url + anime['image']['original'],
            'score': anime['score'], 
        } for anime in json]

    def _get(self, url, params):
        headers = { 'User-Agent': 'erem-bot' }
        return requests.get(url, headers=headers, params=params).json()
