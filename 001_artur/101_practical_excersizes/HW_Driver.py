from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get('http://saucedemo.com')

time.sleep(50)
username_input = driver.find_element('xpath', '//*[@id="user-name"]')
username_input.send_keys('standard_user')

password_input = driver.find_element('xpath', '//*[@id="password"]')
password_input.send_keys('secret_sauce')

login = driver.find_element('xpath', '//*[@id="login-button"]')
login.click()