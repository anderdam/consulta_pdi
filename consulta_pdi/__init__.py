import shutil
import openpyxl
import time
import pandas as pd
import regex
from selenium import webdriver

# CONSTANTS
TAG_NAME = 'tag name'

# Define Dataframe
df = pd.DataFrame(columns=['RGI', 'Documento', 'Emissão', 'Valor', 'Vencimento', 'Situação'])

# list of keys
# rgi_list = ['0911757716', '0911755500', '0911755772']
rgi_list = []
parar = False
while not parar:
    rgi = str(input("Insira um rgi ou 0 para parar: "))
    if rgi == '0':
        parar = True
    else:
        rgi_list.append(rgi)

key_list = rgi_list

# iterate through the list of keys
for key in key_list:
    driver = webdriver.Firefox()
    # navigate to the website
    url = 'https://agenciavirtual.sabesp.com.br/minhas-faturas'
    driver.get(url)

    # wait for the page to load
    time.sleep(2)

    # find the checkbox element and select it
    checkbox = driver.find_element(by='id', value="_dxpminhasfaturas_WAR_dxpminhasfaturas_:minhasFaturasForm:chkSVR")
    checkbox.click()
    # find the input element and enter the key
    input_element = driver.find_element(by='id', value="_dxpminhasfaturas_WAR_dxpminhasfaturas_:minhasFaturasForm:pde")
    input_element.send_keys(key)

    time.sleep(5)
    # wait for the user to submit the form manually
    # input("Press Enter to continue...")

    # find the table element
    table_div = driver.find_element(by='class name', value="criaTabelaDinamica")
    childs_div = table_div.find_elements(by='xpath', value='./*')

    headers = [childs_div[0].text]
    rows = [childs_div[1].text]

    time.sleep(1)

    checkbox_faturas = driver.find_element(by='id', value="chkTodos")
    if checkbox_faturas:
        checkbox_faturas.click()
        time.sleep(1)

        checkbox_2via = driver.find_element(by='id', value="_dxpminhasfaturas_WAR_dxpminhasfaturas_:minhasFaturasForm:perg1:0")
        checkbox_2via.click()
        time.sleep(1)

        checkbox_envio = driver.find_element(by='id', value="_dxpminhasfaturas_WAR_dxpminhasfaturas_:minhasFaturasForm:perg2:3")
        checkbox_envio.click()
        time.sleep(1)
    else:
        driver.save_screenshot(f'/home/anderdam/rgi/prints/{key}.png')

    df = df.append(
        {
            'RGI': key,
            'Endereço': '',
            'Documento': regex.find_doc(rows[0]),
            'Emissão': regex.find_emi(rows[0]),
            'Valor': regex.find_value(rows[0]),
            'Vencimento': regex.find_venc(rows[0]),
            'Situação': regex.find_situation(rows[0])
        }, ignore_index=True)

    # specify the path of the file to be moved
    src_file = "/home/anderdam/Downloads/Segunda Via.PDF"

    # specify the path of the destination folder
    dst_folder = f"/home/anderdam/rgi/pdfs/{key}.pdf"

    shutil.move(src_file, dst_folder)

    time.sleep(5)
    driver.close()

print(df)

file = "/home/anderdam/Documents/lista de rgi.xlsx"
df.to_excel(file, engine='openpyxl', index=False)

# Load the workbook
wb = openpyxl.load_workbook(file)
# Select the active worksheet
ws = wb.active

# Loop through all the columns in the worksheet
for column_cells in ws.columns:
    # Determine the maximum length of the cell contents in the column
    max_length = 0
    column = column_cells[0].column_letter
    for cell in column_cells:
        try:  # Necessary to avoid error on empty cells
            if len(str(cell.value)) > max_length:
                max_length = len(cell.value)
        except TypeError:
            pass
    # Set the column width based on the maximum length
    adjusted_width = (max_length + 2) * 1.2
    ws.column_dimensions[column].width = adjusted_width

# Save the workbook
wb.save(file)
