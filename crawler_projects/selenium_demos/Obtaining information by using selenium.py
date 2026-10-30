from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


Opt = Options()
service = Service(r"D:\py\chromedriver.exe")

driver = webdriver.Chrome(service=service, options=Opt)
driver.get("https://073-m.web-12.com/")

driver.maximize_window()
time.sleep(1)

box = driver.find_element(By.XPATH, '//*[@id="mokuai_1_13"]/div[2]/a[1]/img')
box.click()
time.sleep(1)

data_content = driver.find_elements(By.XPATH, '//*[@id="pro_detail"]/p')
text_list = [data.text for data in data_content]
print(text_list)
time.sleep(1)

picture = driver.find_element(By.XPATH, '//*[@id="slider2"]/li/a/img')
print(picture.get_attribute("src"))
time.sleep(1)

driver.quit()
time.sleep(1)
