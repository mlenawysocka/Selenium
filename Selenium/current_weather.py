import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.google.pl')

# buttonAccept = driver.find_element('id', 'L2AGLb')
buttonAccept = driver.find_element(By.ID, 'L2AGLb')
buttonAccept.click()

searchInput = driver.find_element(By.NAME, 'q')
searchInput.send_keys('Aktualna pogoda we Wroclawiu')
searchInput.send_keys(Keys.ENTER)

# buttonSearch = driver.find_element('name', 'btnK')
# buttonSearch.click()

# driver.get_screenshot_as_file('screen_z_ekranu.png')

print("I'm in the middle of the code")

time.sleep(50)
driver.quit()

print("I'm at the end of the code")