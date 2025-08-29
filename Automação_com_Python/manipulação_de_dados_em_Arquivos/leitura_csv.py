import csv
from pathlib import Path

arquivo = Path("alunos.csv").resolve()

with arquivo.open(mode='r', newline='', encoding='utf-8') as file:
	leitor = csv.DictReader(file)
	for data in leitor:
		print (data)
