#!/usr/bin/env python3

from flask import Flask, request
from flask import render_template as template
from pathlib import Path
import json

app = Flask(__name__)

arquivo = Path("form_get.json")

def salvar(usr):
	with arquivo.open(mode='a', encoding='utf-8') as file:
		json.dump(usr, file, ensure_ascii=False, indent=4)

@app.route("/")
def home():
	nome = request.args.get("nome", "")
	salvar(nome)
	return template("form_get.html", nome=nome)

if __name__ == "__main__":
	app.run(debug=True)
