#!/usr/bin/env python3

from flask import Flask, jsonify
import routes

app = Flask(__name__)
app.register_blueprint(routes.bp)

@app.errorhandler(404)
def pagina_not_found(error):
	return jsonify({"Erro": "Endpoint não encontrado!"}), 404

@app.errorhandler(500)
def erro_interno(error):
	return jsonify({"erro": "Erro interno no servidor"}), 500

if __name__ == "__main__":
	app.run(debug=True)
