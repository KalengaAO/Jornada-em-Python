#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)
visita = []

@app.route("/visitas", methods=["GET", "POST"])
def visitas():
	if request.method == "POST":
		nome = request.form.get("nome", "anónimo")
		mensagem = request.form.get("mensagem", "sem mensagem")
		visita.append(f"{nome}: {mensagem}")

	lista_html = "<br>".join(visita)
	return f"""
		<h2>Livro de visitas</h2>
		<form method="POST">
		Nome: <input name="nome"><br>
		Mensagem: <input name="mensagem"><br>
		<input type="submit" value="Assinar">
		</form>
		<h3>Visitantes:</h3>
		<p>{lista_html}</p>
	"""

@app.errorhandler(404)
def pagin_not_found(error):
	return f'''<h1 style="color:red">
			Pagina esta pagina não existe neste servidor{error}</h1>'''

if __name__ == "__main__":
	app.run(debug=True)
