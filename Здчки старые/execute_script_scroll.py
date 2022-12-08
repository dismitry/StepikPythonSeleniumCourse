from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"

try:

    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    input = browser.find_element_by_id('answer')
    input.send_keys(y)

    # проскроллить на 100 пикселей
    browser.execute_script("window.scrollBy(0, 100);")

    option = browser.find_element_by_id('robotCheckbox')
    option.click()

    option = browser.find_element_by_id('robotsRule')
    option.click()

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
