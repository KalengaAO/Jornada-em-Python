#!/usr/bin/env python3

from flask import Flask
from flask import render_template as template

app = Flask(__name__)

@app.route("/")
def home():
	user = [
			{"nome": "António", "idade":23, "cidade": "Luanda"},
			{"nome": "Maria", "idade":23, "cidade": "Lisboa"},
			{"nome": "João", "idade":27, "cidade": "Londres"}]
	return template("users.html", user=user)

if __name__ == "__main__":
	app.run(debug=True)
