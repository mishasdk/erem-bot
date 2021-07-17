from naruto_quotes_factory import NarutoQuotesFactory


class QuoteData:
	def __init__(self, text, author):
		self.text = text
		self.author = author


class QuotesRepo:
	def __init__(self):
		self.naruto_quotes_factory = NarutoQuotesFactory()

	def get_naruto_quote(self):
		quote = self.naruto_quotes_factory.get_quote()
		return QuoteData(quote[0], quote[1])
