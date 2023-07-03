from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://www.saucedemo.com')
print(driver.title)

user = driver.find_element('name', 'user-name')
user.send_keys('standard_user')

haslo = driver.find_element('name', 'password')
haslo.send_keys('secret_sauce')

logmein = driver.find_element('name', 'login-button')
logmein.click()

time.sleep(60)
driver.quit()

