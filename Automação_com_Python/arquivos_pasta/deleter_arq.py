from pathlib import Path
from datetime import datetime, timedelta 

caminho = input("Digite o caminho da pasta a limpar: ")
dias = int(input("Apagar arquivos com mais de quantos dias?: ")) 
pasta = Path("..") / caminho

if not pasta.exists() or not pasta.is_dir(): 
	print("Caminho inválido ou não é uma pasta")
	exit()

limite = datetime.now() - timedelta(days=dias) 
arquivos = []
ext = input("filtrar por extensão (ex: .log ENTER para tudo): ").strip() 

for item in pasta.iterdir():
	if item.is_file():
		tempo_mod = datetime.fromtimestamp(item.stat().st_mtime) 
		if (tempo_mod < limite):
			if (ext == "" or item.suffix == ext):
				arquivos.append(item)
			else:
				print("Arquivo com extensão não encontrado: ", ext)
				exit()
	if not arquivos:
		print("Sem para arquivos para apagar")
		exit()
	print(len(arquivos), "arquivos para exclusão:\n") 

for i, a in enumerate(arquivos, 1):
	mod_data = datetime.fromtimestamp(a.stat().st_mtime).strftime('%Y-%m-%d')
	print(f"{i}. {a.name} (Modificados em {mod_data})")
	resposta = input(f"\nDeseja apagar estes arquivos {arquivos}: ").lower().strip()
	if resposta != 's':
		print("Operação cancelada")
		exit()

relatorio = pasta / "relatorio_de_arquivos_excluido.log"
relatorio.touch(exist_ok=True)

with open(relatorio, 'w') as f:
	f.write(f"Arquivos apagados: ({len(arquivos)}):\n\n")
	for arq in arquivos:
		arq.unlink()
		f.write(f"- {arq.name}\n")

print(f"Arquivos apagados com sucessso.")
print(f"Relatorio salvo em: {relatorio.resolve()}")
