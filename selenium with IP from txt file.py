from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from fake_useragent import UserAgent
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import random
from random import shuffle
import time


def load_proxies(PATH): # for loading the proxies
    return open(PATH).read().split('\n') 


proxies = open("proxies.txt", "r").readlines()
shuffle(proxies)


for i in range(0, len(proxies)):
    try:
      print("Proxy selected: {}".format(proxies[i]))
      options = webdriver.ChromeOptions()
      options.add_argument('start-maximized')
      options.add_argument('--enable-javascript')
      options.add_argument('--proxy-server={}'.format(proxies[i]))
      ua = UserAgent()
      userAgent = ua.random
      print(userAgent)
      options.add_argument(f'user-agent={userAgent}')
      driver = webdriver.Chrome(options=options, executable_path=r"path to chromedriver")
      do.staff()
    except Exception as e:
      print("something went wrong: "+repr(e))
      driver.quit()
