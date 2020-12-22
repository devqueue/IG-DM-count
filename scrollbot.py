from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from conf import USERNAME, PASSWORD
from loginbot import insta_login
import time

# PATH = "/usr/bin/chromium"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome( options=options)
print(driver.title)
url = driver.command_executor._url  
session_id = driver.session_id

insta_login(driver, USERNAME, PASSWORD)

driver.get("https://www.instagram.com/direct/inbox/")
time.sleep(10)

select_dm = input("Press enter after selecting a user")
body_el = driver.find_element_by_css_selector('body')
select_dm = input("Press enter to start scrolling")

print(url)
print(session_id)
# Scrolling untill inturrupted manully
for i in range(2000):
    body_el.send_keys(Keys.PAGE_UP)
    time.sleep(2)
