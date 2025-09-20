#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def bemvind():
	return f'''
		<form action="saudacao" method="GET">
		<h3>Bem vindo !</h3>
		<input type="submit" value="redirecionar">
		</form>
		'''

@app.route("/sisifo")
def sesifivo():
	return f'''
		<form action="saudacao" method="GET">
		<h1> came back again Sísifo! </h1>
		<input type="submit" value ="redirecionar">
		</form>
		'''

@app.route("/saudacao", methods=["GET", "POST"])
def saudacao():
	if request.method == "POST":
		nome = request.form.get("nome", "visitante")
		return f''' 
			<form action="sisifo">
				<h3>Olá {nome}!</h3>
				Retornar: <input type="submit" value="redirecionar">
			</form>
			'''
	return '''
		<form method="POST"> 
			<h2>Digite o nome</h2>
			Nome: <input name="nome">
			<input type="submit" value="enviar">
		</form>
		'''
@app.errorhandler(404)
def pagina_not_found(e):
	return (f"<h2>Página não encontrada T_T 404</h2>\n<p>{e}</p>")
if __name__ == "__main__":

	app.run(debug=True)
