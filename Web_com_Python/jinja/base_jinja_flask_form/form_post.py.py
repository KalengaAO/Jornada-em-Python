#!/usr/bin/env python3

from flask import Flask, request
from flask import render_template as template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
	if request.method == "POST":
		nome = request.form.get("nome", "anônimo")
		return f'''
			<h2 style="color:green">Olá, {nome}. <br>Recebi seu POST<h2>
			'''
	return template("form_form.html")

if __name__ == "__main__":
	app.run(debug=True)
