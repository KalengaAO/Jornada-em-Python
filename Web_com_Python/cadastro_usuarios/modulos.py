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
		json.dump(users, file, ensure_ascii=False, indent=4)

def novo_user(new_user):
	file = carregar()
	user = {"id": len(file) + 1, "nome": new_user['nome']}
	file.append(user)
	salvar(file)

def obter(id_):
	file = carregar()
	user = next((user for user in file if user['id'] == id_), None)
	if not user:
		return None
	return user

def atualizar(id_, nome=None):
	file = carregar()
	user = next((user for user in file if user['id'] == id_), None)
	if not user:
		return None
	if nome:
		user['nome'] = nome
	salvar(file)
	return user

def remover(id_):
	file = carregar()
	user = next((user for user in file if user['id'] == id_), None)
	if not user:
		return None
	file.remove(user)
	salvar(file)
	return user

def lista():
	file = carregar()
	if not file:
		return None
	return file
