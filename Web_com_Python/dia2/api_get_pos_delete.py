#!/usr/bin/env python3

from flask import Flask, request, jsonify

app = Flask(__name__)

tarefas = [
			{"id":1, "tarefas": "testando api"},
			{"id":2, "tarefas": "testando o metodo delete"}
		]

@app.route("/tarefas/<int:id_>", methods=["GET", "POST", "DELETE"])
def gerenciador_de_tarefa(id_):
	if not tarefas:
		return jsonify({"erro": "Tarefas não encontrada"}), 404
	for tarefa in tarefas:
		if tarefa["id"] == id_:
			break ;
		else:
			tarefa = {"id": None, "tarefa": None}
	if request.method == "GET":
		return jsonify(tarefa)
	elif request.method == "POST":
		dados = request.get_json()
		novo_obj = {"id": len(tarefas) + 1, "titulo": dados["titulo"]}
		tarefas.append(novo_obj)
		return jsonify(tarefas)
	elif request.method == "DELETE":
		if tarefa["id"] == None:
			return jsonify({"mensagem": f"Id {id_ } inválido"})
		tarefas.remove(tarefa)
		return jsonify({"mensagem": f"Tarefa {id_} removidas"})
	return jsonify({"mensagem": f"Tarefas {id_} não identificada"})

@app.errorhandler(404)
def	pagin_not_found(error):
	return f"""
			<h1 style="color:red;">Pagina inexistente neste servidor!</h1>
			<a href="/tarefas/2" style="color:blue;">
			clique aqui para uma pagina valida!</a>
		"""
if __name__ == "__main__":
	app.run(debug=True)
