import requests

from bs4 import BeautifulSoup
from random import randint
from utils import Utils


class NarutoQuotesProvider:
	_url = 'https://citaty.info/anime/naruto-naruto'
	_quotes = []

	def __init__(self): 
		self._fetch_data()		

	def provide(self):
		return Utils.choose_random(self._quotes)

	def _fetch_data(self):
		for i in range(11):
			self._fetch_from_page(i)

	def _fetch_from_page(self, page):
		responce = requests.get(self._url, params={'page': page})
		soup = BeautifulSoup(responce.text, 'lxml')

		for node in soup.findAll('div', {'class': 'node__content'}):
			text = node.find('p').text
			author = soup.find('a', {'title': 'Цитируемый персонаж' }).text
			self._quotes.append({'text': text, 'author': author})
