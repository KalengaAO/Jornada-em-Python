#!/usr/bin/env python3

from pathlib import Path
import json

arquivo = Path("usuarios.json")

def carregar():
	if arquivo.exists():
		try:
			with arquivo.open(mode='r', encoding='utf-8') as file:
				return json.load(file)
		except json.JSONDecodeError:
			return []
	return []

def salvar(users):
	with arquivo.open(mode='w', encoding='utf-8') as file:
		json.dump(users, file, ensure_ascii=False, indent=2)

def lista():
	return carregar()

def obter(id_):
	users = carregar()
	return next((u for u in users if u["id"] == id_), None)

def criar(nome, email):
	users = carregar()
	novo = {"id":len(users) + 1, "nome": nome, "email": email}
	users.append(novo)
	salvar(users)
	return novo

def atualizar(id_, nome=None, email=None):
	users = carregar()
	user = next((u for u in users if u["id"] == id_), None)
	if not user:
		return None
	if nome:
		user["nome"] = nome
	if email:
		user["email"] = email
	salvar(users)
	return user 

def remover(id_):
	users = carregar()
	user = next((u for u in users if u["id"] == id_), None)
	if not user:
		return None
	users.remove(user)
	return user
