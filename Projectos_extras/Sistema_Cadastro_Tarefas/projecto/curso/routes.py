#!/usr/bin/env python3

from flask import Flask, request, redirect, flash, Blueprint, url_for
from flask import render_template as template
import curso.modulos as modulo

curso_bp = Blueprint("curso", __name__, template_folder="templates")

@curso_bp.route("/")
def home():
	return template("index.html")

@curso_bp.route("/lista")
def lista():
	lista = []
	cadastro = modulo.listar()
	if not cadastro:
		flash("Sem cadastro!", "info")
		return redirect(url_for("curso.cadastrar"))
	for user in cadastro:
		lista.append(user)
	return template("lista.html", cadastro=lista)

@curso_bp.route("/cadastro")
def cadastrar():
	return template("cadastro.html")

@curso_bp.route("/registro", methods=["GET", "POST"])
def registrada_cada():
	if request.method == "POST":
		modulo.criar_cadastro(
				request.form.get("nome"),
				request.form.get("email"),
				request.form.get("idade"),
				request.form.get("tel"),
				request.form.get("morada"))
	return redirect(url_for("curso.home"))

@curso_bp.route("/remove", methods=["GET", "DELETE"])
def remover():
	if request.method == "DELETE":
		flash("Cadastro removido", "info")
		return redirect(url_for("curso.home"))
	elif request.method == "GET":
		id_ = request.form.get("id")
		modulo.remover(id_)
		flash("Envia o ID para remover o Cadastro", "info")
		return template("remover.html")
