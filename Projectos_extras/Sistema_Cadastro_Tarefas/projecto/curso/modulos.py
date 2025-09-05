#!/usr/bin/env python3

from pathlib import Path
import json

arquivo = Path("cadastrado.json")
num_id = 0

def carregar():
	if not arquivo.exists():
		arquivo.touch(exist_ok=True)
	try:
		with arquivo.open(mode='r', encoding='utf-8') as file:
			return json.load(file)
	except json.JSONDecodeError:
		return []

def salvar(novo_cadastro):
	cadastro = carregar()
	cadastro.append(novo_cadastro)
	with arquivo.open(mode='w', encoding='utf-8') as file:
		json.dump(cadastro, file, ensure_ascii=False, indent=4)

def criar_cadastro(nome = None, email = None, idade = None,
			tel = None, morada = None):
	file = carregar()
	global num_id
	num_id += 1
	if not morada:
		morada = "desconhecido"
	novo_cadastro = { 
				"id": num_id,
				"nome": nome,
				"email":email,
				"idade":idade,
				"tel": tel,
				"morada": morada}
	salvar(novo_cadastro)
	return novo_cadastro

def	listar():
	return carregar()

def buscar(id_):
	cadastro = carregar()
	for user in cadastro:
		if user["id"] == id_:
			return user;

def normaliza_id(id_):
    try:
        return int(str(id_).strip())
    except (ValueError, TypeError):
        return str(id_)

def remover(id_):
	cadastro = carregar()
	alvo = normaliza_id(id_)
	for user in cadastro:
		if user["id"] == alvo:
			cadastro.remove(user)
			break;
	salvar(cadastro)

def atualizar(id_ = None, nome = None, email = None,
 idade = None, tel = None, morada = None):
	cadastro = carregar()
	for user in cadastro:
		if user["id"] == id_:
			if nome:
				user["nome"] = nome
			if email:
				user["eamil"] = email
			if idade:
				user["idade"] = idade
			if tel:
				user["user"] = tel
			if morada:
				user["morada"] = morada
			salvar(user)
			return True

	return False
