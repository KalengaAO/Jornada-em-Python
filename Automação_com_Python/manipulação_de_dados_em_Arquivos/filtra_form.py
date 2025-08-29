import csv
import json
from pathlib import Path

while True:
	try:
		entrada = input("Digite o caminho do arquivo CSV: ").strip()
		arq_in = Path(entrada).expanduser().resolve()
		curso = input("Digite o curso a ser filtrado: ").strip().lower()
		saida = input("Digite o nome de arquivo de saida: ").strip().lower()
		if arq_in.exists():
			if arq_in.suffix != ".csv":
				print("Arquivo com formato inesperado: (ex: nome_do_arquivo.csv)")
			else:
				break
	except ValueError as vl:
		print(f"Error: Entrada inválida {vl}")

formato = ["csv", "json", "txt", "log"]
print(f"Escolha o formato do arquivo {saida}")
print(f"{formato}")

while True:
	form = input("(ex: log): ").strip().lower()
	if form in formato:
		break

arq_out = Path(f"{saida}.{form}")
arq_out.touch(exist_ok=True)

with open(arq_in, 'r', encoding='utf-8', newline='') as fd_in:
	leitor = csv.DictReader(fd_in)
	filtrado = []
	for dados in leitor:
		if dados['curso'].lower() == curso:
			filtrado.append({
				"name": dados['nome'],
				"idade": dados['idade'],
				"email": dados['email']
			})

if not filtrado:
	print(f"Não há estudante no curso de: {curso}")
	exit()

if arq_out.suffix == ".json":
	with open(arq_out, 'w', encoding='utf-8', newline='') as fd_out:
		json.dump(filtrado, fd_out, indent=2, ensure_ascii=False)

if arq_out.suffix == ".csv":
	with open(arq_out, 'w', encoding='utf-8', newline='') as fd_out:
		colunas = ['name', 'idade', 'email']
		escritor = csv.DictWriter(fd_out, fieldnames=colunas)
		escritor.writeheader()
		escritor.writerows(filtrado)

if arq_out.suffix in [".txt", ".log"]:
	with open(arq_out, 'w', encoding='utf-8', newline='') as fd_out:
		for item in filtrado:
			fd_out.writelines(f"{item['name']} - {item['idade']} - {item['email']}\n")

print(f"Dados salvos em {arq_out.resolve()}:")
