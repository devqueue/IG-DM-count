from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from conf import USERNAME, PASSWORD
from loginbot import insta_login
import time

# PATH = "/usr/bin/chromium"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
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


# paste this line by line in the terminal
'''
# xpath for dm group
laya_dm_Xpath = '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/*'
dms_el_list = driver.find_elements_by_xpath(laya_dm_Xpath)
print(len(dms_el_list))
'''
