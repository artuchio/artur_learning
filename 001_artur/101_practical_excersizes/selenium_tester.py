from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def capture_element_screenshot(driver, xpath, filename):
    try:
        element_to_capture = driver.find_element(By.XPATH, xpath)
        element_to_capture.screenshot(filename)
        print(f"Screenshot of element saved as {filename}")
    except Exception as e:
        print(f"Failed to capture element screenshot: {str(e)}")

driver = webdriver.Chrome()
driver.get('http://saucedemo.com')

time.sleep(5)

username_input = driver.find_element(By.XPATH, '//*[@id="user-name"]')
username_input.send_keys('standard_user')

password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
password_input.send_keys('secret_sauce')

login = driver.find_element(By.XPATH, '//*[@id="login-button"]')
login.click()

add_backpack = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
add_backpack.click()

add_bikelight = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
add_bikelight.click()

add_t_shirt = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
add_t_shirt.click()

cart_view = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
cart_view.click()

checkout = driver.find_element(By.XPATH, '//*[@id="checkout"]')
checkout.click()

client_input = driver.find_element(By.XPATH, '//*[@id="first-name"]')
client_input.send_keys('Secret Buyer')

client_input_s = driver.find_element(By.XPATH, '//*[@id="last-name"]')
client_input_s.send_keys('Secret')

client_input_z = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
client_input_z.send_keys('10111')

conti = driver.find_element(By.XPATH, '//*[@id="continue"]')
conti.click()

# Capture a screenshot of the specified element and save it to a file
capture_element_screenshot(driver, '//*[@id="page_wrapper"]', 'purchase3.png')

# Save the main page screenshot
driver.save_screenshot('purchase1.png')

time.sleep(20)
driver.quit()
