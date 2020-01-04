import time
import math
from selenium import webdriver
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/get_attribute.html"
driverChrome = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
driverChrome.get(link)
people_radio = driverChrome.find_element_by_id("treasure")
x_element = people_radio.get_attribute("valuex")
x = x_element
y = calc(x)
inputT = driverChrome.find_element_by_id('answer')
inputT.send_keys(y)
chkIRobot = driverChrome.find_element_by_id("robotCheckbox")
chkIRobot.click()
RobotsRule = driverChrome.find_element_by_id("robotsRule")
RobotsRule.click()

btnSubmit = driverChrome.find_element_by_tag_name('button')
btnSubmit.submit()
time.sleep(5)
driverChrome.quit()