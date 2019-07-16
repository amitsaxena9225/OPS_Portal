import xlrd
import time
from selenium import webdriver
import xlwt
#import openpyxl
import selenium
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement


def func_edit_xpath_send_keys(context: object, var1: object, var2: object) -> object:
    driver = context.driver
    element = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, var1)))
    print(element.text)
    element.send_keys(var2)
    #print(a)

def func_click_xpath(context,var1) -> object:
    driver = context.driver
    element = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, var1)))
    element.click()

def func_clear(context,var1):
    driver = context.driver

    element =WebDriverWait(driver,120).until(EC.element_to_be_clickable(By.XPATH,var1))

    element.clear()









