#!/usr/bin/env python3

from flask import Flask
from flask import render_template as template

app = Flask(__name__)

@app.route("/")
def home():
	nome = "António Pedro Kalenga"
	return template("index.html", nome=nome)

if __name__ == "__main__":
	app.run(debug=True)
