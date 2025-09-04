#!/usr/bin/env python3

from flask import Blueprint, request, redirect, flash, url_for
from flask import render_template as template

user_bp = Blueprint("user", __name__, template_folder="templates")

users = []

@user_bp.route("/cadastro", methods=["GET", "POST"])
def	cadastro():
	if request.method == "POST":
		nome = request.form.get("nome")
		email = request.form.get("email")
		idade = request.form.get("idade")

		error = []
		if not nome:
			error.append("O campo nome é obrigatório.")
		if not email:
			error.append("Digite o email válido.")
		if not idade.isdigit():
			error.append("A idade de ver um digito.")
		if not int(idade) >= 15:
			error.append("Só é permitido idade igual ou superior a 15 anos de idade.")
		if error:
			for er in error:
				flash(er, "erro")
		else:
			user = {"nome": nome, "email": email, "idade": idade}
			users.append(user)
			flash("usuário cadastrado com sucesso!", "sucesso")
			return redirect(url_for("user.lista"))
	return template("cadastro.html")

@user_bp.route("/lista")
def lista():
	return template("lista.html", users=users)
