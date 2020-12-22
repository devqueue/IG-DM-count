from selenium import webdriver
from conf import USERNAME, PASSWORD
import time

def insta_login()
    # PATH = "./assets/chromedriver"
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(2)

    # Enter login details
    username_el = driver.find_element_by_name("username")
    username_el.send_keys(USERNAME)

    password_el = driver.find_element_by_name("password")
    password_el.send_keys(PASSWORD)

    # click submit button
    time.sleep(1.5)
    submit_btn_el = driver.find_element_by_css_selector('button[type=submit]')
    submit_btn_el.click()

    # click save login info
    time.sleep(10)
    save_info = driver.find_element_by_css_selector('button[type=button]')
    save_info.click()

    # click not now for notifications
    time.sleep(5)
    not_now_xpath = '/html/body/div[4]/div/div/div/div[3]/button[2]'
    deny_notification = driver.find_element_by_xpath(not_now_xpath)
    deny_notification.click()

    time.sleep(3)
    driver.get("https://www.instagram.com/direct/inbox/")
    time.sleep(10)








