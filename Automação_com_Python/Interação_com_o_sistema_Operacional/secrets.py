#!/usr/bin/env python3

import secrets
import string
import sys

if len(sys.argv) != 2:
	print (f"Uso: python3 scripy.py [tamanho da senha]")
	sys.exit(1)

tam = int(sys.argv[1])
car = string.ascii_letters + string.digits + string.punctuation
senha = ''.join(secrets.choice(car) for _ in range(tam))

print (f"senha gerada: {senha}")
