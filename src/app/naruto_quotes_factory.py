import requests

from bs4 import BeautifulSoup
from random import randint
from utils import Utils


class NarutoQuotesFactory:
	def __init__(self): 
		self._naruto_url = 'https://citaty.info/anime/naruto-naruto'
		self._quoteData = []
		self._fetchData()		

	def get_quote(self):
		return Utils.random_from_data(self._quoteData)

	def _fetchData(self):
		for i in range(11):
			self._fetch_from_page(i)

	def _fetch_from_page(self, page):
		params = {'page': randint(0, page)}	
		responce = requests.get(self._naruto_url, params=params)
		soup = BeautifulSoup(responce.text, 'lxml')
		view_content = soup.find('div', {'class': 'view-content'})
		nodes = soup.findAll('div', {'class': 'node__content'})

		for node in nodes:
			text = node.find('p').text
			author = soup.find('a', {'title': 'Цитируемый персонаж'}).text
			self._quoteData.append((text, author))
