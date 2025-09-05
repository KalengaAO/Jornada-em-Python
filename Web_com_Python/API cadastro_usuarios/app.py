#!/usr/bin/env python3

from flask import Flask, jsonify
import routas

app = Flask(__name__)
app.register_blueprint(routas.bp)

@app.errorhandler(404)
def pagin_not_found(error):
	return jsonify({"erro": "rota não encontrada: {error}!"})

@app.errorhandler(500)
def erro_interno(error):
	return jsonify({"erro": "erro interno do servidor: {error}!"})

if __name__ == "__main__":
	app.run(debug=True)
