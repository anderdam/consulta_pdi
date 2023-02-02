from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common import NoSuchElementException


def wait_table_load(browser, wait_time, table):
    return WebDriverWait(browser, wait_time).until(ec.presence_of_element_located((By.CLASS_NAME, table)))
