#!/usr/bin/env python3

from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def	home():
	return redirect("/outra")

@app.route("/outra")
def outra_rota():
	return "<h2>Agora você está na rota /outra</h2>"

if __name__ == "__main__":
	app.run(debug=True)
