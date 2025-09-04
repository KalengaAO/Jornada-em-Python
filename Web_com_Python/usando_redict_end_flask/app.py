#!/usr/bin/env python3

from flask import Flask
from user.routes import user_bp

app = Flask(__name__)
app.secret_key = "1234"
app.register_blueprint(user_bp)

@app.errorhandler(404)
def pag_not_found(error):
	return '''
			<h1 style="color:red">A pagina solicitada não existe</h1>
		'''

@app.errorhandler(500)
def error_interno(error):
	return '''
		<h2 style="color:red">Erro interno no servidor</h2>
		'''

if __name__ == "__main__":
	app.run(debug=True)
