from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from conf import USERNAME, PASSWORD
from login import insta_login
import time

# PATH = "./assets/chromedriver"
driver = webdriver.Chrome()

insta_login(driver, USERNAME, PASSWORD)

driver.get("https://www.instagram.com/direct/inbox/")
time.sleep(10)

select_dm = input("Press enter after selecting a user")
body_el = driver.find_element_by_css_selector('body')
select_dm = input("Press enter to start scrolling")

# Scrolling untill inturrupted manully
while True:
    body_el.send_keys(Keys.PAGE_UP)
    time.sleep(2)
