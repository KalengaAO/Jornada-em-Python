#!/usr/bin/env python3

from flask import Flask, request
from pathlib import Path
from datetime import datetime
import json

app = Flask(__name__)
arquivo = Path("visitas.json").resolve()

def open_file():
	if arquivo.exists():
		try:
			with open(arquivo, mode='r+', newline='', encoding='utf-8') as file:
				return json.load(file)
		except json.JSONDecodeError:
			return []
	return []

def salvar_visitas(visitas):
	with arquivo.open(mode='w', encoding='utf-8') as file:
		json.dump(visitas, file, ensure_ascii=False, indent=2)

@app.route("/visitas", methods=["GET", "POST"])
def lista_visitas():
	visitas = open_file()

	if request.method == "POST":
		nome = request.form.get(f"nome", "anomimo")
		mensagem = request.form.get(f"mensagem", "campo vazio")
		now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

		visitas.append({"nome": nome, "mensagem": mensagem, "data": now})
		salvar_visitas(visitas)

	lista_html = "<br>".join(
			[f"{v['data']} - {v['nome']}: {v['mensagem']}" for v in visitas]
		)
	return f"""
			<h2>Livros de visitas</h2>
			<form method="POST">
				Name: <input type="text" name="nome"><br>
				Mensagem: <input type="text" name="mensagem"><br>
				<input type="submit" value="assinar">
			</form>
			<h3>Visitantes:</h3>
			<p>{lista_html}</p>
		"""

@app.errorhandler(404)
def pagina_not_found(error):
	return f"""
		<h1 style="color:red;">Erro 404</h1>
		<p>A página não existe no servidor.</p>
		<a href="/visitas">Voltar ao livro de visitas</a>
		""", 404

def main():
	app.run(debug=True)

if __name__ == "__main__":
    main()
