from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

options = Options()
# চাইলে headless চালাতে পারো (background এ): options.add_argument('--headless')

driver = webdriver.Firefox(options=options)
driver.get("https://www.google.com")
time.sleep(3)

print("✅ ব্রাউজার টাইটেল:", driver.title)
driver.quit()