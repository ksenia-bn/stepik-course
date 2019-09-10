import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
def test_lesson8(browser):
  
    browser.get(link)
    buttonAlert = browser.find_element_by_css_selector("button.btn")
    buttonAlert.click()
    confirm = browser.switch_to.alert
    confirm.accept() 
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text  
    print (x)   
    y = calc(x)
    inputX_element = browser.find_element_by_id("answer")
    inputX_element.send_keys(y)    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()




