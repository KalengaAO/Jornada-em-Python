#!/usr/bin/env python3

from flask import Flask, request
from flask import render_template as template

app = Flask(__name__)

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
	user = None
	if request.method == "POST":
		nome = request.form.get("nome", "anônimo")
		email = request.form.get("email", "não informado")
		idade = request.form.get("idade", "0")
		user = {"nome": nome, "email": email, "idade": idade}
		return 	template("cadastro.html", user=user)
	return template("cadastro.html")


@app.errorhandler(404)
def not_found(error):
	return f'''
		<p style="color:red" >error a pagina solicitada não existe</p>
		'''
if __name__ == "__main__":
	app.run(debug=True)
