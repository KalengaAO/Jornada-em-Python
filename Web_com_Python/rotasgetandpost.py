#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def bemvind():
	return '''
			<form action="saudacao" method="GET">
			<input type="submit" value="redirecionar">
			</form>
		 '''

@app.route("/saudacao", methods=["GET", "POST"])
def saudacao():
	if request.method == "POST":
		print ("Dados recebidos:", request.form)
		nome = request.form.get("nome", "visitante")
		return (f"Olá, {nome}!")
	return '''
		<form method="POST"> 
			Nome: <input name="nome">
			<input type="submit" value="enviar">
		</form>
		'''
@app.errorhandler(404)
def pagina_not_found(e):
	return (f"<h1>Página não encontrada T_T 404</h2>\n<p>{e}</p>")
if __name__ == "__main__":

	app.run(debug=True)
