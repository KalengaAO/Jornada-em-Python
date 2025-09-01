#!/usr/bin/env python3

from flask import Flask, request, jsonify, Blueprint
import models

bp = Blueprint("usuários", __name__)

@bp.route("/user", methods=["GET", "POST"])
def lista_criar():
	if request.method == "GET":
		return jsonify(models.lista()), 200
	elif request.method == "POST":
		dados = request.get_json()
		if not dados or "nome" not in dados or "email" not in dados:
			return jsonify({"error": "Campos 'nome' e 'email' são obrigatórios"}), 400
		novo = models.criar(dados["nome"], dados["email"])
		return jsonify(novo), 201

@bp.route("/user/<int:id_>", methods=["GET", "PUT", "DELETE"])
def gerenciar(id_):
	if request.method == "GET":
		user = models.obter(id_)
		if not user:
			return jsonify({"error": "Usuários não encontrado"}), 404
		return jsonify(user), 200
	elif request.method == "PUT":
		dados = request.get_json()
		if not dados:
			return jsonify({"Erro": "envie os dados para actualizar"})
		user = models.atualizar(id_, dados.get("nome"), dados.get("email"))
		if not user:
			return jsonify({"erro": "usuarios não encontrado"}), 404
		return jsonify(user), 200
	elif request.method == "DELETE":
		user = models.remover(id_)
		if not user:
			return jsonify({"erro": "usuario não encontrado"}), 404
		return jsonify({"mesagem": f"IDUS {id_} removido"}), 200
