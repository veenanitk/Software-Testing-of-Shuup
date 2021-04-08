from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox(executable_path='/home/veena/Downloads/geckodriver-v0.29.0-linux64/geckodriver')
browser.get("http://127.0.0.1:8000/sa/login/?next=/sa/") 
time.sleep(1)