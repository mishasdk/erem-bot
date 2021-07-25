# coding: utf8

import requests
import random  

IMAGE_URL = 'https://shikimori.one'
URL = 'https://shikimori.one/api/'


def animes():
    url = URL + 'animes'
    headers = {
        'User-Agent': 'erem-bot'
    }
    params = {
       'limit': 50,
       'page': 1,
       'score': 8,
       'kind': 'tv',
    }
    return requests.get(url, headers=headers, params=params).json()


def random_anime():
    animes_data = animes()
    index = random.randint(0,49)
    return animes_data[index]


def get_anime():
    anime = random_anime()
    return {
        'name': anime['russian'], 
        'image': IMAGE_URL + anime['image']['original'],
        'score': anime['score'],    
    }



