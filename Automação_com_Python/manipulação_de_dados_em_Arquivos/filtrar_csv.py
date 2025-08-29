import csv
import sys
from pathlib import Path

entrada = str(input("Digite o caminho do arquivo csv a ser filtrado: "))
arquivo = Path(entrada).resolve()

if arquivo.is_file():
	if arquivo.suffix != ".csv":
		print(f"arquivo '{entrada}' com extensão invalida")
		sys.exit(1)
else:
	print("Arquivo inexistente:")
	sys.exit(1)
alunos_filtrado = []
print("CAMPOS: nome\tidade\tcurso\temail")
with open(arquivo, mode='r', newline='', encoding='utf-8') as filein:
	reader = csv.DictReader(filein)
	filtro = str(input("Digite o campo a ser filtrado: ")).strip().lower()
	for alunos in reader:
		if alunos['curso'].lower() == filtro:
			alunos_filtrado.append(alunos)

with open("filtro.csv", mode='w', newline='', encoding='utf-8') as fileout:
	colunas = ['nome', 'idade', 'curso', 'email']
	writer = csv.DictWriter(fileout, fieldnames=colunas)
	writer.writeheader()
	writer.writerows(alunos_filtrado)
	print (f"Arquivo com filtro criado em: {Path.cwd()}")
