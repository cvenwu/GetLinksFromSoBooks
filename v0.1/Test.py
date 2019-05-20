# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get("http://www.baidu.com")

# bookName = '红果'
# print("{0}".format(bookName))

import bs4
import requests
import openpyxl
from selenium import webdriver

URL = "http://www.sivan.tech"

while True:
    browser = webdriver.Chrome()
    browser.get(URL)
    browser.close()
