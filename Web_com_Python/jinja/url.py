#!/usr/bin/env python3

from flask import Flask, url_for , redirect

app = Flask(__name__)

@app.route("/")
def home():
	return redirect("/redir")

@app.route("/redir")
def redirecion():
	return f"<a href='{url_for('perfil')}'>Ir para o perfil</a>"

@app.route("/perfil")
def perfil():
	return '''<h1 style="color:green">Perfil do usuaŕio</h1>'''

if __name__ == "__main__":
	app.run(debug=True)
