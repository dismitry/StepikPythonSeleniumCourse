from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/get_attribute.html"

try:

    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_id('treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)
    input = browser.find_element_by_id('answer')
    input.send_keys(y)

    option = browser.find_element_by_id('robotCheckbox')
    option.click()

    option = browser.find_element_by_id('robotsRule')
    option.click()

    time.sleep(2)

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
