# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 23:14:32 2019

@author: Илья
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

text = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR")
    )
button = browser.find_element_by_id("book").click()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)

input = browser.find_element_by_id("answer").send_keys(y)
button = browser.find_element_by_id("solve").click()
