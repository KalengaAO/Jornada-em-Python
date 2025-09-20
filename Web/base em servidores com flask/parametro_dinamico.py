#!/usr/bin/env python

from flask import Flask, request

app = Flask(__name__)

@app.route("/hello/<nome>")
def hello(nome):
	return f"<h2>Olá, {nome.capitalize()}</h2>"

@app.errorhandler(404)
def paginanotfout(error):
	return f"<h3>Esta pagina não esta no nosso servidor<br>{error}</h2>"

if __name__ == "__main__":

	app.run(debug=True)
