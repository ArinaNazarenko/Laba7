import time
import math

from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
driverChrome = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
driverChrome.get(link)

btnSubmit = driverChrome.find_element_by_tag_name('button')
btnSubmit.submit()

x_element = driverChrome.find_element_by_id('input_value')
x = x_element.text
y = calc(x)

inputT = driverChrome.find_element_by_id('answer')
inputT.send_keys(y)

btnSubmit = driverChrome.find_element_by_tag_name('button')
btnSubmit.submit()
time.sleep(1)
driverChrome.quit()