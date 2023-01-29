import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

pdi_list = []
parar = False

while not parar:
    pdi = int(input('Insira um PDI ou 0 para parar: '))
    if pdi == 0:
        parar = True
    else:
        pdi_list.append(pdi)

keys_list = pdi_list

# create a new Chrome browser instance
driver = webdriver.Firefox()

# navigate to the website
url = 'https://agenciavirtual.sabesp.com.br/minhas-faturas'
driver.get(url)

# find the checkbox element and select it
for key in keys_list:
    checkbox = driver.find_element(by='id', value='_dxpminhasfaturas_WAR_dxpminhasfaturas_:minhasFaturasForm:chkSVR')
    checkbox.click()

    # find the text field element and enter a number
    text_field = driver.find_element(by='id', value="_dxpminhasfaturas_WAR_dxpminhasfaturas_:minhasFaturasForm:pde")
    text_field.send_keys(key)
    wait = WebDriverWait(driver, 10)
    error_div = wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'alert')))
    error_message = error_div.text
    print(error_message)
    # driver.back()

# 54324564001