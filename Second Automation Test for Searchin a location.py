from selenium import webdriver
import time


browser = webdriver.Firefox()
browser.implicitly_wait(10)
browser.maximize_window()
browser.get('https://magazine.trivago.com/')
browser.find_element_by_class_name('search-icon').click()
searchbar = browser.find_element_by_css_selector('input.search-input').send_keys('chicago')

from selenium.webdriver.common.keys import Keys

searchbar.send_keys(Keys.ENTER)


time.sleep(3)
browser.close()
browser.quit()

print('Test Passed Successfully')