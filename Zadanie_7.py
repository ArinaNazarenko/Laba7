import time
import math
from selenium import webdriver
driverChrome = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
link = "http://suninjuly.github.io/redirect_accept.html"
driverChrome.get(link)
time.sleep(5)

btn = driverChrome.find_elements_by_css_selector(".btn")
btn[0].click()
driverChrome.switch_to.window(driverChrome.window_handles[1])

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x = driverChrome.find_element_by_id("input_value").text
y = calc(x)

InputT= driverChrome.find_element_by_id("answer")
InputT.send_keys(y)

btnSubmit = driverChrome.find_element_by_css_selector(".btn") 
btnSubmit.click()

time.sleep(5)
driverChrome.quit()