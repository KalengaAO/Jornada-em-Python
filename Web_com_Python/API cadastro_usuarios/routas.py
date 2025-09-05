#!/usr/bin/env python3

from flask import Flask, request, Blueprint, jsonify
import modulos

bp = Blueprint("/user",__name__)

@bp.route("/user", methods=["GET", "POST"])
def user():
	if request.method == "GET":
		users = modulos.lista()
		return jsonify(users), 200
	elif request.method == "POST":
		user = request.get_json()
		if not user or "nome" not in user or "id" not in user:
			return jsonify({"Erro": "entre com todos campos validos"}), 400
		modulos.novo_user(user)
		return jsonify(user), 201

@bp.route("/user/<int:id_>", methods=["GET", "PUT", "DELETE"])
def	gerencia(id_):
	if request.method == "GET":
		user_get = request.get_json()
		if not user_get or not "id" in user_get:
			return jsonify({"erro": "entrada inválida"}), 400
		user = modulos.obter(user_get.get("id"))
		return jsonify(user), 200
	elif request.method == "PUT":
		user_put = request.get_json()
		if not user_put or "nome" not in user_put or "id" not in user_put:
			return jsonify({"error": "entre com todos os campos "}), 400
		user = modulos.atualizar(user_put.get("id"), user_put.get("nome"))
		if not user:
				return jsonify({f"error": "nenhum usuario com este id: {id_}"}), 404
		return jsonify(user), 200
	elif request.method == "DELETE":
		user_del = request.get_json()
		if not user_del or "id" not in user_del:
			return jsonify({"erro": ""})
		user = modulos.remover(user_del.get("id"))
		if not user:
			return jsonify({"erro": "nenhum usuario com este id: {id_}"}), 404
		return jsonify(user), 200
