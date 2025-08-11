#!/usr/bin/env python3

from pathlib import Path
import sys

def	criar_arq(name):

	arq = Path(name).expanduser().resolve()
	if not arq.exists():
		arq.write_text("#!/usr/bin/env python3\n")
		print (f"Arquivo criado com sucesso em: {arq.resolve()}")
	else:
		print ("Arquivos existente!")
		sys.exit(0)

if __name__ == "__main__":

	if len(sys.argv) == 2:
		criar_arq(sys.argv[1])
	else:
		print ("Uso: python3 script.py <nome_do_arquivos>")	
