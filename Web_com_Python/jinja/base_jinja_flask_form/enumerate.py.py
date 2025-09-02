#!/usr/bin/env python3

from flask import Flask
from flask import render_template as template

app = Flask(__name__)

@app.route("/")
def home():
	lista = ["Flask", "Jinja2", "Apis", "Banco de dados", "Deploy"]
	return template("enumerate.html", lista=lista)

if __name__ == "__main__":
	app.run(debug=True)
