#!/usr/bin/env python3

from flask import Flask
from curso.routes import curso_bp

app = Flask(__name__)
app.secret_key = "1234"
app.register_blueprint(curso_bp)

@app.errorhandler(404)
def not_found(error):
	return '''
		<h1 style="color:red;">Página não existe!</h1>
		'''

@app.errorhandler(500)
def erro_interno(error):
	return '''
			<h1 style="color:green;">Error interno do servidor!</h1>
		'''

if __name__ == "__main__":
	app.run(debug=True)
