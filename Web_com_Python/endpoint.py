#!/usr/bin/env python3

from flask import jsonify, Flask, request
from pathlib import Path
import json

app = Flask(__name__)

arquivo = Path("log_filtro.json").resolve()


@app.route("/api/info")
def api_inf():
	with arquivo.open(mode='r', newline='', encoding='utf-8') as file:
		reader = json.load(file)
		return jsonify(reader)

@app.errorhandler(404)
def paginanotfound(error):
	return f"<h1>Pagina não encontrada {error}</h1>"

if __name__ == "__main__":
	app.run(debug=True)
