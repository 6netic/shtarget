from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/")
def index():
	""" Homepage of the application """

	return render_template("index.html")


@app.route("/ten")
def tenmeters():
	""" View for 10 meters calculation """

	return render_template("tenmeters.html")


