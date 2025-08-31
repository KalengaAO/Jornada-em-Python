#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
@app.route("/")
def home():
	return "Bem vindo á minha primeira aplicação web!"

@app.route("/sobre")
def	sobre():
	return "Esta é a pagina sobre"

@app.route("/login")
def	login():
	return "Em breve partimos para esta parte!"

if __name__ == "__main__":

	app.run(debug=True, host="0.0.0.0", port=9000)
