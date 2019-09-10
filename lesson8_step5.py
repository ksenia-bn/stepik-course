from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
def test_lesson8_step5(browser):   
    browser.get(link)
    element_present = EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    WebDriverWait(browser, 12).until(element_present)      
    buttonBoot = browser.find_element_by_id("book")
    buttonBoot.click()
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text  
    print (x)   
    y = calc(x)
    inputX_element = browser.find_element_by_id("answer")
    inputX_element.send_keys(y)    
    button = browser.find_element_by_id("solve")
    button.click()




