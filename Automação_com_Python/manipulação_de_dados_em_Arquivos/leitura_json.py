import json
from pathlib import Path

arquivo = Path("alunos.json").resolve()

with arquivo.open(mode='r', newline='', encoding='utf-8') as file:
	dados = json.load(file)
	for i, aluno in enumerate(dados):
		print(f"{i + 1}. {aluno['nome']} - {aluno['idade']}, {aluno['curso']}")
