import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driverChrome = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
link = "http://suninjuly.github.io/explicit_wait2.html"
driverChrome.get(link)
#  стоимость не стнет равной $100
waitPrice = WebDriverWait(driverChrome, 12).until(
        EC.text_to_be_present_in_element((By.ID,"price"), "$100")
    )
btnBook = driverChrome.find_elements_by_id("book")
btnBook[0].click()
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x = driverChrome.find_element_by_id("input_value").text
y = calc(x)

InputT = driverChrome.find_element_by_id("answer")
InputT.send_keys(y)

btnSubmit = driverChrome.find_element_by_id("solve") 
btnSubmit.click()

time.sleep(5)
driverChrome.quit()