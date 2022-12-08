from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/selects1.html"

try:
    browser.get(link)

    first_x = browser.find_element_by_id('num1')
    first_x = first_x.text
    second_y = browser.find_element_by_id('num2')
    second_y = second_y.text
    sum_x = int(first_x) + int(second_y)

    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(str(sum_x))

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
