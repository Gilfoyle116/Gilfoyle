from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

Opt = Options()
service = Service(r"D:\py\chromedriver.exe")

# Opening the website
driver = webdriver.Chrome(service=service, options=Opt)
driver.get("https://www.testmuai.com/selenium-playground/")

# Clicking the Simple Form Demo
wait = WebDriverWait(driver, 10)
click_text = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Simple Form Demo")))
click_text.click()

# Inputting information
message_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-message"]')))
message_input.send_keys("Adding two magnitudes")

# Inputting two numbers
input_text1 = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="sum1"]')))
input_text1.send_keys("64")

input_text2 = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="sum2"]')))
input_text2.send_keys("36")

# Finding the sum button
get_sum = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Get Sum"]')))
# Scrolling to the button position firstly
driver.execute_script("arguments[0].scrollIntoView(true);", get_sum)
time.sleep(0.5)
# JS clicks
driver.execute_script("arguments[0].click();", get_sum)


# Getting the result by JS
result_text = driver.execute_script("""
const sum1Val = document.getElementById('sum1').value;
const sum2Val = document.getElementById('sum2').value;
return Number(sum1Val)+Number(sum2Val);
""")
print("Result: ", result_text)

time.sleep(2)
driver.quit()