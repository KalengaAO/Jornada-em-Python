#!/usr/bin/env python3

from pathlib import Path
import json

arquivo = Path("usuarios.json")

def carregar():
	if arquivo.exists()
		try:
			with arquivo.open(mode='r', encoding'utf-8') as file:
			return json.load(file)

