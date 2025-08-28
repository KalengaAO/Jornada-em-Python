from pathlib import Path
import sys

entrada = str(input("Digite o caminho da pasta: ")).lower().strip()

base = Path(entrada).expanduser()

if not base.exists():
	print("Caminho inválido!")
	sys.exit(0)

with open("log_explorador.log", 'a') as log:
	for item in base.iterdir():
		if item.is_dir():
			log.write(f"pasta: {item}\n")
		elif item.is_file():
			log.write(f"ficheiro: {item}\n")

print(f"Director listado em: {base.resolve()}")
