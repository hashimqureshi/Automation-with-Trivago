from selenium import webdriver
import time


browser = webdriver.Firefox()
browser.implicitly_wait(10)
browser.maximize_window()
browser.get('https://magazine.trivago.com')
subscribe = browser.find_element_by_xpath('//*[@id="app"]/div[3]/div/div[7]/section/div/div/div[2]/div[2]/div[1]/input').send_keys('triavago@test.com')
submit = browser.find_element_by_xpath('//*[@id="app"]/div[3]/div/div[7]/section/div/div/div[2]/div[2]/div[2]/button').click()



print('Test Passed Successfully')