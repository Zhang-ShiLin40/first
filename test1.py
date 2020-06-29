from selenium import webdriver
from selenium.webdriver.common.by import By
import time


dr = webdriver.Chrome()

dr.get("https://www.baidu.com")
time.sleep(3)
#dr.find_element_by_id("kw").send_keys("selenium")
dr.find_element(By.ID, "kw").send_keys("ramin karimloo")
