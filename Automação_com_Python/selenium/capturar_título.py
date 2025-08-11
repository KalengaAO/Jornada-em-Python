#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
import sys

def	capturar_titulo(url):
	while True:
		if not url.endswith(".com"):
			url = str(input("Entre com uma url valida: \
(ex: https://example.com)\nUrl: ")).lower().strip()
		else:
			break
	try:
		opt = Options()
		opt.add_argument("--headless=new")

		driver = webdriver.Chrome(options=opt)
		driver.get(url)
		print (f"O titulo do site aberdo no modo headless: {driver.title}")

	except WebDriverException as e:
		print (f"Error ao inicializar o navegador")

	finally:
		if driver:
			driver.quit()

if __name__ == "__main__":

	if len(sys.argv) == 2:
		capturar_titulo(sys.argv[1])
	else:
		print ("Uso: python3 script.py <url>")
