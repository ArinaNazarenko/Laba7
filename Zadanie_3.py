import math
import time
from selenium import webdriver
link = "http://suninjuly.github.io/selects1.html"
driverChrome = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
driverChrome.get(link)

def calc(x,y):
  return str((int(x)+int(y)))

x = driverChrome.find_element_by_id("num1").text
y = driverChrome.find_element_by_id("num2").text

z = calc(x,y)

driverChrome.find_element_by_tag_name("select").click()
driverChrome.find_element_by_css_selector("[value='" + z + "']").click()
time.sleep(1)
btnSubmit = driverChrome.find_element_by_tag_name('button')
btnSubmit.submit()
time.sleep(3)
driverChrome.quit()