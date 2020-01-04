import time
import math
from selenium import webdriver
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/execute_script.html"
driverChrome = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
driverChrome.get(link)
x_element = driverChrome.find_element_by_id("input_value").text
x = x_element
y = calc(x)
inputT = driverChrome.find_element_by_id('answer')
inputT.send_keys(y)
chkIRobot = driverChrome.find_element_by_id("robotCheckbox")
chkIRobot.click()
time.sleep(1)
btnSubmit = driverChrome.find_element_by_tag_name('button')
driverChrome.execute_script("return arguments[0].scrollIntoView(true);", btnSubmit)
RobotsRule = driverChrome.find_element_by_id("robotsRule")
RobotsRule.click()
btnSubmit.submit()
time.sleep(3)
driverChrome.quit()