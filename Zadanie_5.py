import time
import math
import os 

from selenium import webdriver
driverChrome = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
driverChrome.get("http://suninjuly.github.io/file_input.html")

textInputFirstName = driverChrome.find_elements_by_css_selector("[name='firstname']")
textInputFirstName[0].send_keys("Arina")
textInputLastName = driverChrome.find_elements_by_css_selector("[name='lastname']")
textInputLastName[0].send_keys("Nazarenko")
textInputEmail = driverChrome.find_elements_by_css_selector("[name='email']")
textInputEmail[0].send_keys("nazarenko_arisha@mail.ru")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'Bay.txt') 

btnSubmit = driverChrome.find_element_by_tag_name('button')
btnSubmit.submit()

time.sleep(2)
driverChrome.quit()