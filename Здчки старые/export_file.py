from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"

try:

    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("I")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("P")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("S@s.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file.rtf"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element_by_id("file")
    element.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
