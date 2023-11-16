# (venv) Abhisheks-MacBook-Pro:artur_learning abhishekmathur$ pip3 freeze
# source venv bin activate
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get('http://google.com')
time.sleep(5)

reject = driver.find_element('id', 'W0wltc')
reject.click()

# search = driver.find_element('xpath', '//*[@id="APjFqb"]')
# search.send_keys('Selenium Documentation')
# search.send_keys(Keys.ENTER)
# time.sleep(2)
# # search.clear()
# driver.back()
# time.sleep(3)
# driver.forward()
# time.sleep(3)
# driver.refresh()
# time.sleep(2)
# print(search.is_enabled())
# print(search.is_selected())
# print(search.is_displayed())
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# driver.get('http://google.com')
# def waiter(timeout, selector, value):
#     try:
#         element = WebDriverWait(driver, timeout).until(
#         EC.presence_of_element_located((selector, value))
#     )
#     except:
#         print('ERROR')
#         return None
#     else:
#         return element
#
#
# reject = waiter(10, By.ID, 'W0wltc')
# print(reject.parent)
#  print(driver.title) #.pagesource .current_url
# # time.sleep(5)
# # driver.close()
# # driver.quit()
# time.sleep(5)
# //*[@id="APjFqb"]
# /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea lichse smotret po id takaka ego menshe menjajut
# width = driver.get_window_size().get('width')
# height = driver.get_window_size().get('height')
# print(width, height)
#
# driver.set_window_size(1920, 1080)
# driver.set_window_position(-5, -5)
#
#
# print(driver.get_window_rect(100, 100, 400, 900))
# driver.fullscreen_window()
# time.sleep(3)
# driver.minimize_window()
# time.sleep(3)

# driver.save_screenshot('image.png')
# el = driver.find_element('css selector', 'body' > div.gb_Dd)
# el.screentshot('element.png')

google = driver.current_window_handle
driver.switch_to.new_window('tab')
driver.get('http://github.com')
github = driver.current_window_handle
time.sleep(2)
driver.switch_to.window(google)
# time.sleep(2)
# driver.close()
print(driver.window_handles)
#print(driver.