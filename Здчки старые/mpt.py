
from selenium import webdriver
import time
import unittest


class RegTest(unittest.TestCase):
    def test_reg1(self):

    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()

    browser.get(link)

    input1 = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[1]/input')
    input1.send_keys('first')

    input1 = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/input')
    input1.send_keys('second')

    input1 = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[3]/input')
    input1.send_keys('third')

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

    welcome_text_elt = browser.find_element_by_tag_name('h1')
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

if __name__ == "__main__":
    unittest.main()
