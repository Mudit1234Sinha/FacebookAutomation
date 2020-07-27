# This code will automatically fill all your information when you are creating a new account on facebook
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By  # These 3 are for explicit wait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path = "C:/Users/ADMIN/Desktop/chromedriver.exe"
browser = webdriver.Chrome(path)
browser.get("https://facebook.com")

firstName = browser.find_element_by_id("u_0_m")
firstName.send_keys("Mudit")
lastName = browser.find_element_by_id("u_0_o")
lastName.send_keys("Sinha")
email = browser.find_element_by_id("u_0_r")
email.send_keys("persiaprince857@gmail.com")
time.sleep(2)
email2 = browser.find_element_by_id("u_0_u")
email2.send_keys("persiaprince857@gmail.com")

password = browser.find_element_by_id("password_step_input")
password.send_keys("13579even")

gender = browser.find_element_by_id("u_0_7")
verify_gender = gender.is_selected()
if verify_gender != True:
    gender = browser.find_element_by_id("u_0_7")
    gender.click()

day = Select(browser.find_element_by_id("day"))
# Select by visible text
day.select_by_visible_text("4")

month = Select(browser.find_element_by_id("month"))
# Select by Index
month.select_by_index(7)

year = Select(browser.find_element_by_id("year"))
# Select by Value
year.select_by_value("1998")





# Below code is for getting name of the months
"""
month1 = Select(browser.find_element_by_id("month"))
print(len(month1.options))

for option in month1.options:
    print(option.text)
"""