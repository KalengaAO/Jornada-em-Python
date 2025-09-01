#!/usr/bin/env python3

from flask import Flask, request, jsonify

app = Flask(__name__)

tarefas = [
		{"id":1, "tarefa":"Estudar programção"},
		{"id":2, "tarefa":"Estudar rede"}]

@app.route("/tarefas", methods=["GET", "POST"])
def get_and_post_tarefas():
	if request.method == "GET":
		return jsonify(tarefas)
	elif request.method == "POST":
		data = request.get_json()
		novo_obj = {"id": len(tarefas) + 1, "tarefa":data["tarefa"]}
		tarefas.append(novo_obj)
		return jsonify(tarefas)

@app.route("/tarefas/<int:id_>", methods=["GET", "PUT", "DELETE"])
def gerenciador_tarefa(id_):
	tarefa = {"id": None, "titulo": None}
	for tarefa in tarefas:
		if tarefa["id"] == id_:
			break
	if request.method == "GET":
		return jsonify(tarefa)
	elif request.method == "PUT":
		dados = request.get_json()
		tarefa["tarefa"] = dados.get("tarefa", tarefa["tarefa"])
		return jsonify({"Mensagem": f"Tarefa com id {id_} actualiza!","tarefa":tarefa})
	elif request.method == "DELETE":
		tarefas.remove(tarefa)
		return jsonify(tarefas)

@app.errorhandler(404)
def pagina_not_found(error):
	return """
		<h1 style="color:red;">Página inexistente neste servidor!</h1>
		<a href="/tarefas" style="color:blue;">Clique aqui para uma página válida!</a>
		""", 404

if __name__ == "__main__":
	app.run(debug=True)
