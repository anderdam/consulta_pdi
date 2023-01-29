from selenium import webdriver
import time
import pandas as pd

# list of keys
pdi_list = []
parar = False
while not parar:
    pdi = int(input("Insira um PDI ou 0 para parar: "))
    if pdi == 0:
        parar = True
    pdi_list.append(pdi)

key_list = pdi_list

# create a new Firefox driver
driver = webdriver.Firefox()

# navigate to the website
url = 'https://agenciavirtual.sabesp.com.br/minhas-faturas'
driver.get(url)

# wait for the page to load
time.sleep(5)

# find the checkbox element and select it
checkbox = driver.find_element(by='id', value="checkbox-id")
checkbox.click()

# iterate through the list of keys
for key in key_list:
    # find the input element and enter the key
    input_element = driver.find_element(by='', value="_dxpminhasfaturas_WAR_dxpminhasfaturas_:minhasFaturasForm:chkSVR")
    input_element.send_keys(key)

    # wait for the user to submit the form manually
    input("Press Enter to continue...")

    # find the table element
    table = driver.find_element(by='class', value="criaTabelaDinamica")
    # create an empty dataframe
    df = pd.DataFrame()
    # add the 'Key' column to the dataframe
    df['Key'] = key
    # find the table headers
    headers = [th.text for th in table.find_elements(by='tag_name', value="th")]
    # iterate through each row
    for i, row in enumerate(table.find_elements(by='tag_name', value="tr")):
        # find all columns in the row
        columns = row.find_elements(by='tag_name', value="td")
        for j, column in enumerate(columns):
            # add the data to the corresponding column
            df.at[i, headers[j]] = column.text
    print(df)

# close the browser
#driver.close()
