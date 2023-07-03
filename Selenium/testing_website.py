# from selenium import webdriver
# import time
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.get('https://www.w3schools.com/')
# #driver.set_window_size(1200, 1000)
# driver.maximize_window()
# accept = driver.find_element('id', 'accept-choices')
# accept.click()
# menu = driver.find_element('id', 'navbtn_tutorials')
# webdriver.ActionChains(driver).move_to_element(menu).perform()
# webdriver.ActionChains(driver).move_to_element(menu).click().perform()
#
# #time.sleep(5)
# HTMLtutu = driver.find_element('xpath', '//*[@id="nav_tutorials"]/div/div/div[2]/a[1]')
# HTMLtutu.click()
# #time.sleep(8)
# HTMLAtributs = driver.find_element('xpath', '//*[@id="w3-exerciseform"]/div/div')
# HTMLAtributs.click()
#
# HTMLnext = driver.find_element('xpath', '//*[@id="main"]/div[3]/table/tbody/tr[32]/td[1]/a')
# HTMLnext.click()
#
#
#
# # w3-bar-item w3-button
#
# time.sleep(100)
# driver.close()

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
import time
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10, 0.5, NoSuchElementException)
driver.get('https://www.w3schools.com/')
print(driver.title)
time.sleep(5)
driver.maximize_window()
accept = driver.find_element("id", "accept-choices")
accept.click()
menu = driver.find_element("id", "navbtn_tutorials")
webdriver.ActionChains(driver).move_to_element(menu).perform()
webdriver.ActionChains(driver).move_to_element(menu).click().perform()

HTMLtutu = driver.find_element('xpath', '//*[@id="nav_tutorials"]/div/div/div[2]/a[1]')
HTMLtutu.click()
wait.until(expected_conditions.visibility_of_element_located(('xpath', '//*[@id="leftmenuinnerinner"]/a[64]')))
#wait.until(lambda x: len(x.find_elements('xpath', '//*[@id="leftmenuinnerinner"]/a[64]')))

HTMLAtributs = driver.find_element('xpath', '//*[@id="leftmenuinnerinner"]/a[64]')
HTMLAtributs.click()
#driver.find_element('xpath', '//*[@id="leftmenuinnerinner"]/a[64]').click()driver.find_element('xpath', '//*[@id="main"]/div[3]/table/tbody/tr[32]/td[1]/a').click()driver.find_element('xpath', '//*[@id="main"]/div[5]/a').click()

print(driver.title)

currentWindowName = driver.current_window_handle

windowNames = driver.window_handles

for window in windowNames:
    if window != currentWindowName:
        driver.switch_to.window(window)
        print(driver.title)

driver.find_element('xpath', '//*[@id="runbtn"]').click()
driver.switch_to.frame(driver.find_element('id', 'iframeResult'))
firstName = driver.find_element('id', 'fname')

if firstName.is_enabled():
    firstName.send_keys('Kleopatra')
else:
    print('Nie da się wpisać tekstu')

firstName.clear()
firstName.send_keys('Natalia')
driver.close()

driver.switch_to.window(currentWindowName)
print(driver.title)
driver.back()
driver.back()
driver.find_element('xpath', '//*[@id="leftmenuinnerinner"]/a[41]').click()
driver.find_element('xpath', '//*[@id="main"]/div[13]/a').click()
currentWindowName = driver.current_window_handle
windowNames = driver.window_handles
for window in windowNames:
    if window != currentWindowName:
        driver.switch_to.window(window)
        print(driver.title)

driver.switch_to.frame(driver.find_element('id', 'iframeResult'))
boat = driver.find_element('id', 'vehicle3')
boat.click()
driver.close()
driver.switch_to.window(currentWindowName)

time.sleep(500)
driver.quit()