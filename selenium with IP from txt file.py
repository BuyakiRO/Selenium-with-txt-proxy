from selenium import webdriver
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from fake_useragent import UserAgent
import random
from random import shuffle
import time

def load_proxies(PATH): # for loading the proxies
    return open(PATH).read().split('\n') 

def message(message):
    message = text

proxies = open("E:/ipp.txt", "r").readlines()
shuffle(proxies)

for i in range(0, len(proxies)):
    try:
      text = 'Starting script'
      print('{}'.format(text))
      print("Proxy selected: {}".format(proxies[i]))
      options = webdriver.ChromeOptions()
      options.add_argument('start-maximized')
      options.add_argument('--enable-javascript')
      options.add_argument('--proxy-server={}'.format(proxies[i]))
      ua = UserAgent()
      userAgent = ua.random
      print(userAgent)
      options.add_argument(f'user-agent={userAgent}')
      driver = webdriver.Chrome(options=options, executable_path=r"E:/chromedriver.exe")
      driver.get('http://svencrai.com/68Su')
      time.sleep(10)
      element = driver.find_element_by_xpath(r'//*[@id="skip_bu2tton"]').click()
      time.sleep(5)
      alert = driver.switch_to.alert()
      alert.accept()
      time.sleep(10)
      driver.switch_to.window(driver.window_handles[0])
      element = driver.find_element_by_xpath(r'/html/body/iframe').click()
      time.sleep(5)
      driver.switch_to.window(driver.window_handles[0])
      time.sleep(15)
      driver.quit()
    except Exception as e:
      print("something went wrong: "+repr(e))
      driver.quit()
print("Proxy Invoked")
