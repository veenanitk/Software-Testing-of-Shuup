from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome(executable_path='/home/veena/Downloads/chromedriver_linux64 (1)/chromedriver')
browser.get("http://127.0.0.1:8000/sa/login/?next=/sa/") 
time.sleep(1)
username = browser.find_element_by_id("id_username")
password = browser.find_element_by_id("id_password")
username.send_keys("veena-staff-admin")
password.send_keys("bhumi123")
login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
login_attempt.submit()
time.sleep(1)
browser.get("http://127.0.0.1:8000/sa/campaignss/new/")