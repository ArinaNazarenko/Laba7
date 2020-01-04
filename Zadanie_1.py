import time
import math

from selenium import webdriver
driver = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
driver.get("http://suninjuly.github.io/math.html")
time.sleep(1)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = driver.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

inputT = driver.find_element_by_id("answer")
inputT.send_keys(y)

time.sleep(1)

chkIRobot = driver.find_elements_by_id("robotCheckbox")
chkIRobot[0].click()

time.sleep(1)

rbnRobotsRule = driver.find_elements_by_id("robotsRule")
rbnRobotsRule[0].click()

time.sleep(1)

btnSubmit = driver.find_element_by_css_selector(".btn") 
btnSubmit.click()

time.sleep(5)
driver.quit()