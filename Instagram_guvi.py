import time

import self
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v123 import browser
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/guviofficial/")

# The wait time so that entire window can load
time.sleep(5)

# Fetch popup close button through relative xpath
button_close = driver.find_element(By.XPATH,"//span[@class ='_9-_f _aa5a']")

# Close Instagram Login/Signup popup
button_close.click()
time.sleep(5)

# Fetching number of followers and following using relative xpath
followers = driver.find_element(By.XPATH,"//header[@class='x1qjc9v5 x78zum5 x1q0g3np x2lah0s x1n2onr6 x1qsaojo xc2v4qs x1xl8k2i x1ez9qw7 x1kcpa7z']//li[2]//button[1]")
following = driver.find_element(By.XPATH,"//header[@class='x1qjc9v5 x78zum5 x1q0g3np x2lah0s x1n2onr6 x1qsaojo xc2v4qs x1xl8k2i x1ez9qw7 x1kcpa7z']//li[3]//button[1]")

#Print number of followers and following on the Guvi official
print("Number of followers: ", followers.text)
print("Number of following: ", following.text)

# Close the window
driver.quit()

