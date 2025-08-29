import csv
from pathlib import Path

arquivo = Path("alunos.csv").resolve()

with arquivo.open(mode='r', newline='', encoding='utf-8') as file:
	leitor = csv.DictReader(file)
	for i, data in enumerate(leitor):
		print (f"{i + 1}. {data['nome']}, {data['idade']}, {data['curso']}")
