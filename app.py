"""Flask."""

from flask import Flask
from models import Comment
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
	"""Home route handler."""
	page = """
	<!DOCTYPE = html>
	<html>

	<head>
		<title>Nemanja</title>
	</head>

	<body>
		<h1>Welcome!</h1>
	</body>

	</html>
	"""
	return page

@app.route("/comments")
def comments():
	return render_template('comments.html')
