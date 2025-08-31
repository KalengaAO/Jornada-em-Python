import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/login")

"""search = driver.find_element(By.NAME, "q")"""
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
"""search.send_keys("automação Python Selenium PyAutoGUI", Keys.ENTER)"""

""" uma mistura de selenium com pyautogui para automação  """
""" o selenium abre o navegador com link, o pyautogui e posicionado
no em direção ao botão de login, cinco minutos depois do login 
reposiciono no botão de logout"""

time.sleep(5)
pyautogui.click(320, 550) 
time.sleep(5)
pyautogui.click(220, 400)
driver.quit()
