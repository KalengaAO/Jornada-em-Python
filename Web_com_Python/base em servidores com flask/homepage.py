#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicial():
	return	'''<h2 style="color:blue;">Bem vindo</h2>'''

@app.route("/menu")
def menu():
	return '''
			<h2>Menu</h2>
			<lu>
				<li><a href="/">Inicio</a></li>
				<li><a href="/">Sobre</a></li>
				<li><a href="/">Saudação</a></li>
				<li><a href="/">Hello</a></li>
				<li><a href="/">Api info</a></li>
			</lu>
		'''

@app.errorhandler(404)
def pagin_not_found(error):
	return f'''
		<h1 style="color:red;">Error 404</h1>
		<p style="color:blue;">A página que procuras não existe!</p>
		<a href="/">Voltar ao inicio</a>
	'''

if __name__ == "__main__":
	app.run(debug=True)
