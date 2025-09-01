#!/usr/bin/env python3

from flask import Flask, request
from flask import jsonify

app = Flask(__name__)

tarefas = [{"id":1, "titulo": "Estudar Flask"},
			{"id":2, "titulo": "Fazer exercício do dia 2" }]

@app.route("/tarefas", methods=["GET", "POST"])
def gerenciar_tarefas():
	if request.method == "GET":
		return jsonify(tarefas)
	
	if request.method == "POST":
		dados = request.get_json()
		nova = {"id": len(tarefas) + 1, "titulo":dados["titulo"]}
		tarefas.append(nova)
		return jsonify(nova), 201

@app.errorhandler(404)
def pagin_not_found(error):
	return f'''<h1 style="color:red">Esta pagina não exite no nosso servidor</h1>
			<a href="/tarefas">clique aqui!</a>
		'''

if __name__ == "__main__":
	app.run(debug=True)
