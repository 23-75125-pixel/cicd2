from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

driver.get("http://localhost")

# Magdagdag ng wait time para siguradong loaded ang page
time.sleep(5) 

# I-print ang title at body para ma-debug sa Jenkins logs
print("Page Title:", driver.title)
print("Page Source:", driver.page_source[:500]) # I-print ang unang 500 characters

assert "Hello CI/CD World" in driver.page_source
print("Test Passed!")

driver.quit()
