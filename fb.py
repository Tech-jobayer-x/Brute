from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# ইউজার ইনপুট
email = input("Enter Facebook Email or Phone: ")
password = input("Enter Facebook Password: ")

# Chrome চালু করো (chromedriver একই ফোল্ডারে থাকতে হবে)
driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(3)

# ইমেইল ও পাসওয়ার্ড ফিল আপ
driver.find_element(By.ID, "email").send_keys(email)
driver.find_element(By.ID, "pass").send_keys(password)
driver.find_element(By.ID, "pass").send_keys(Keys.ENTER)

# কিছুক্ষণ অপেক্ষা করে চেক করো সফল কি না
time.sleep(5)
if "home.php" in driver.current_url:
    print("[✓] Login Successful ✅")
else:
    print("[✗] Login Failed ❌")

driver.quit()