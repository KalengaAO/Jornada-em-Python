#!/usr/bin/env python3

from selenium import webdriver
from selenium.commom.by import By
from selenium.webdriver.chrome.options import Options
from selenium.commom.exception import WebDriverExeception
from selenium.webdriver.commom.ui import WebDriverWait
from 

def	capturar_titulo(url)
try:

	options = Option()
	options.add_argument(--headless)
	driver = webdriver.Chrome(option=options)

	WebDriverWait(driver, 5)
	drive.get(url)
	print (f"Título da página: {driver.title}")
	
except WEbDriverException as e:
	print (f"Erro ao iniciar o navegador")

finally:
	driver.quit()
