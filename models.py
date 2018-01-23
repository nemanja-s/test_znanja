"""Models."""


class Comment(object):
	"""Comment."""

	def __init__(self, text, date):
		"""Constructor."""
		self.text = text
		self.date = date

	def __repr__(self):
		"""Represent comment as string."""
		return "Text: {}, Date: {}".format(self.text, self.date)

COMMENTS = [
	Comment('Srecna nova godina', '2017-12-31'), 
	Comment('Srecan rodjendan', '2018-04-19'), 
	Comment('Ponestalo mi je ideja za komentar', '2018-01-23')
]

