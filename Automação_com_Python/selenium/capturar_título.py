#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
import sys

def	capturar_titulo(url):
	while True:
		if not url.endswith(".com"):
			print ("Entre com uma url valida (ex: https//:example.com)")
			url = str(input("ur: "))
		else:
			break
	try:

		options = Options()
		options.add_argument("--headless")
		driver = webdriver.Chrome(option=options)

		WebDriverWait(driver, 5)
		drive.get(url)
		print (f"Título da página: {driver.title}")
	
	except WebDriverException as e:
		print (f"Erro ao iniciar o navegador")

	finally:
		driver.quit()

if __name__ == "__main__":
	if len(sys.argv) == 2:
		capturar_titulo(sys.argv[1])
	else:
		print ("Uso: python3 script.py <url>")
		sys.exit(1)
