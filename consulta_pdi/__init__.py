from selenium import webdriver
import time
import pandas as pd
import pygsheets

# CONSTANTS
TAG_NAME = 'tag name'

# list of keys
pdi_list = []
parar = False
while not parar:
    pdi = int(input("Insira um PDI ou 0 para parar: "))
    if pdi == 0:
        parar = True
        pass
    else:
        pdi_list.append(pdi)

key_list = pdi_list

# create a new Firefox driver
driver = webdriver.Firefox()

# navigate to the website
url = 'https://agenciavirtual.sabesp.com.br/minhas-faturas'
driver.get(url)

# wait for the page to load
time.sleep(2)

# find the checkbox element and select it
checkbox = driver.find_element(by='id', value="_dxpminhasfaturas_WAR_dxpminhasfaturas_:minhasFaturasForm:chkSVR")
checkbox.click()

df = pd.DataFrame()

# iterate through the list of keys
for key in key_list:
    # find the input element and enter the key
    input_element = driver.find_element(by='id', value="_dxpminhasfaturas_WAR_dxpminhasfaturas_:minhasFaturasForm:pde")
    input_element.send_keys(key)

    time.sleep(2)
    # wait for the user to submit the form manually
    # input("Press Enter to continue...")

    # find the table element
    table_div = driver.find_element(by='class name', value="criaTabelaDinamica")
    childs_div = table_div.find_elements(by='xpath', value='./*')

    for child in childs_div:
        print(child.text)
    # add the 'Key' column to the dataframe
#     df['Key'] = key
#     # find the table headers
#     headers = [th.text for th in table.find_elements(by=TAG_NAME, value="th")]
#     # iterate through each row
#     for i, row in enumerate(table.find_elements(by=TAG_NAME, value="tr")):
#         # find all columns in the row
#         columns = row.find_elements(by=TAG_NAME, value="td")
#         for j, column in enumerate(columns):
#             # add the data to the corresponding column
#             df.at[i, headers[j]] = column.text
#
# print(df)
# df.to_excel("/home/anderdam/Documents/dataframe.xlsx", engine='openpyxl')

# close the browser
#driver.close()


# 0911757716