"""
# Filename: run_selenium.py
"""

search_query = "breaking bad"
login = "yes"
password = "yes"

## Run selenium and chrome driver to scrape data from cloudbytes.dev
import time
import os.path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

## Setup chrome options
chrome_options = Options()
chrome_options.add_argument("--headless") # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")

# Set path to chromedriver as per your configuration
homedir = os.path.expanduser("~")
webdriver_service = Service(f"{homedir}/chromedriver/stable/chromedriver")

# Choose Chrome Browser
browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Get page
browser.get("https://www.netflix.com/login")

email = browser.find_element(By.XPATH, "//*[@id=\"id_userLoginId\"]")
for c in login:
    email.send_keys(c)

password = browser.find_element(By.XPATH, "//*[@id=\"id_password\"]")
for c in password:
    password.send_keys(c)

submit = browser.find_element(By.XPATH, "//*[@id=\"appMountPoint\"]/div/div[3]/div/div/div[1]/form/button")
submit.click()

time.sleep(5)

profile = browser.find_element(By.XPATH, "//*[@id=\"appMountPoint\"]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[2]/div/a")
profile.click()

time.sleep(5)

search_button = browser.find_element(By.CSS_SELECTOR, "button.searchTab")
search_button.click()

time.sleep(1)

search_field = browser.find_element(By.CSS_SELECTOR, 'input[data-uia="search-box-input"]')
for c in search_query:
    search_field.send_keys(c)

time.sleep(5)

card = browser.find_element(By.XPATH, "//*[@id=\"title-card-0-0\"]/div[1]").get_attribute("data-ui-tracking-context")
processed = card.split(",")
for i in processed:
    if ("%22video_id%22" in i):
        id = i[-8:]
        print(f"https://www.netflix.com/watch/{id}")

#Wait for 10 seconds
time.sleep(10)
browser.quit()