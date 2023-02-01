# import os
# import PyPDF2
# import openpyxl
# import time
# import pandas as pd
#
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException
# from selenium.common import NoSuchElementException
#
# from consulta_pdi import regex, constants
#
# # CONSTANTS
# TAG_NAME = 'tag name'
#
# # Define Dataframe
# df = pd.DataFrame(columns=[
#     constants.RGI,
#     constants.CLIENTE,
#     constants.ENDERECO,
#     constants.EMISSAO,
#     constants.VALOR,
#     constants.VENCIMENTO,
#     constants.SITUACAO
# ])
#
# # list of keys
# key_list = ['0911757716', '0911755500', '0911755772']
#
# # iterate through the list of keys
# for key in key_list:
#     driver = webdriver.Firefox()
#     # navigate to the website
#     url = 'https://agenciavirtual.sabesp.com.br/minhas-faturas'
#     driver.get(url)
#
#     # wait for the page to load
#     time.sleep(1)
#
#     # find the checkbox element and select it
#     checkbox = driver.find_element(by='id', value="_dxpminhasfaturas_WAR_dxpminhasfaturas_:minhasFaturasForm:chkSVR")
#     checkbox.click()
#     # find the input element and enter the key
#     input_element = driver.find_element(by='id', value="_dxpminhasfaturas_WAR_dxpminhasfaturas_:minhasFaturasForm:pde")
#     input_element.send_keys(key)
#
#     time.sleep(4)
#     # wait for the user to submit the form manually
#     # input("Press Enter to continue...")
#
#     rows = None
#     # find the table element
#     try:
#         table_load = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME, 'criaTabelaDinamica')))
#         print("Page is ready!")
#     except TimeoutException:
#         print("Loading took too much time!")
#     finally:
#         table_load = 'Não encontrado'
#
#     if table_load:
#         table_div = driver.find_element(by='class name', value="criaTabelaDinamica")
#         childs_div = table_div.find_elements(by='xpath', value='./*')
#         if childs_div:
#             headers = [childs_div[0].text]
#             rows = [childs_div[1].text]
#         else:
#             rows = ['N/D']
#     else:
#         childs_div = 'N/D'
#
#     time.sleep(1)
#
#     checkbox_faturas = driver.find_element(by='id', value="chkTodos")
#     if checkbox_faturas:
#         checkbox_faturas.click()
#         time.sleep(1)
#
#         try:
#             checkbox_2via = driver.find_element(by='id', value="_dxpminhasfaturas_WAR_dxpminhasfaturas_:minhasFaturasForm:perg1:0")
#             if checkbox_2via:
#                 checkbox_2via.click()
#                 time.sleep(1)
#
#                 checkbox_envio = driver.find_element(by='id', value="_dxpminhasfaturas_WAR_dxpminhasfaturas_:minhasFaturasForm:perg2:3")
#                 checkbox_envio.click()
#             else:
#                 driver.save_screenshot(f'/home/anderdam/rgi/prints/{key}.png')
#             time.sleep(1)
#         except NoSuchElementException:
#             print('Element not found')
#         finally:
#             driver.save_screenshot(f'/home/anderdam/rgi/prints/{key}.png')
#     else:
#         driver.save_screenshot(f'/home/anderdam/rgi/prints/{key}.png')
#
#     df = df.append(
#         {
#             constants.RGI: key,
#             constants.DOCUMENTO: regex.find_doc(rows[0]),
#             constants.EMISSAO: regex.find_emi(rows[0]),
#             constants.VALOR: regex.find_value(rows[0]),
#             constants.VENCIMENTO: regex.find_venc(rows[0]),
#             constants.SITUACAO: regex.find_situation(rows[0])
#         }, ignore_index=True)
#
#     time.sleep(6)
#     # driver.close()
#     # time.sleep(5)
#
#     if regex.find_doc(rows[0]) != 'N/D':
#         # Define the path to the original file
#         original_file = "/home/anderdam/Downloads/Segunda Via.PDF"
#
#         df = df.append({'PDF': os.path.abspath(original_file)}, ignore_index=True)
#
#         # Loop through each page in the PDF
#         with open(original_file, "rb") as file:
#             reader = PyPDF2.PdfReader(file)
#             num_pages = len(reader.pages)
#             for i in range(num_pages):
#                 page = reader.pages[i]
#                 text = page.extract_text()
#                 lines = text.split('\n')
#
#             # Loop through each line of text
#             for line in lines:
#                 if "End:" in line:
#                     df = df.append({constants.ENDERECO: line}, ignore_index=True)
#                 else:
#                     df = df.append({constants.ENDERECO: 'N/D'}, ignore_index=True)
#                 if "constants.CLIENTE" in line:
#                     df = df.append({'constants.CLIENTE': line}, ignore_index=True)
#                 else:
#                     df = df.append({'constants.CLIENTE': 'N/D'}, ignore_index=True)
#     else:
#         df = df.append({constants.ENDERECO: 'N/D'}, ignore_index=True)
#
# print(df)
#
# file = "/home/anderdam/Documents/lista de rgi.xlsx"
# df.to_excel(file, engine='openpyxl', index=False)
#
# # Load the workbook
# wb = openpyxl.load_workbook(file)
# # Select the active worksheet
# ws = wb.active
#
# # Loop through all the columns in the worksheet
# for column_cells in ws.columns:
#     # Determine the maximum length of the cell contents in the column
#     max_length = 0
#     column = column_cells[0].column_letter
#     for cell in column_cells:
#         try:  # Necessary to avoid error on empty cells
#             if len(str(cell.value)) > max_length:
#                 max_length = len(cell.value)
#         except TypeError:
#             pass
#     # Set the column width based on the maximum length
#     adjusted_width = (max_length + 2) * 1.2
#     ws.column_dimensions[column].width = adjusted_width
#
# # Save the workbook
# wb.save(file)
