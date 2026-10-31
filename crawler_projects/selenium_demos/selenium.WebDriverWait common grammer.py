"""
webdriverwait_cheatsheet.py
Selenium 4 — Full WebDriverWait & expected_conditions Complete Cheat Sheet
Contains all frequently used EC conditions, including alert, frame, window, staleness.
Reference: official expected_conditions
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


# Initialize wait object, reuse it
# Params: driver, timeout(seconds), poll_frequency, ignored_exceptions
service = Service(r"D:\py\chromedriver.exe")
Opt = Options()
driver = webdriver.Chrome(service=service, options=Opt)
wait = WebDriverWait(driver, timeout=10, poll_frequency=0.3)

# ==============================================
# 1. Element existence & visibility
# ==============================================

# 1.1 presence_of_element_located
# Only check the element exists in DOM. It may still be hidden.
elem = wait.until(EC.presence_of_element_located((By.ID, "sum1")))

# 1.2 presence_of_all_elements_located
# Return a list of all matched elements, wait until all appear in DOM
elem_list = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "item")))

# 1.3 visibility_of_element_located
# Element exists + visible (not hidden, display != none). Good for send_keys / read text.
elem = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-message"]')))

# 1.4 visibility_of_all_elements_located
# Wait for all matched elements to become visible
elem_list = wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, "li")))

# 1.5 invisibility_of_element_located
# Wait until element disappears. Common for loading spinner, popup mask.
wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "loading-spinner")))

# 1.6 element_to_be_clickable
# Visible + enabled + not covered. FIRST CHOICE for button / link click.
btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Get Sum"]')))

# 1.7 element_to_be_selected
# Wait for checkbox / radio to be selected
check_box = wait.until(EC.element_to_be_selected((By.ID, "agree")))

# 1.8 element_selection_state_to_be
# Wait until selected state equals expected value(True/False)
wait.until(EC.element_selection_state_to_be((By.ID, "agree"), True))

# 1.9 staleness_of
# Wait until element is stale (element removed / refreshed from DOM)
# Useful after page refresh / form submit
wait.until(EC.staleness_of(elem))


# ==============================================
# 2. Text & value matching
# ==============================================

# 2.1 text_to_be_present_in_element
# Wait for specified text inside the element (innerText)
wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div[contains(text(),'Result:')]"), "100"))

# 2.2 text_to_be_present_in_element_value
# Wait for value attribute of <input> tag
wait.until(EC.text_to_be_present_in_element_value((By.ID, "sum1"), "64"))

# 2.3 title_is
# Exact match page title
wait.until(EC.title_is("Selenium Playground"))

# 2.4 title_contains
# Partial match page title
wait.until(EC.title_contains("Playground"))


# ==============================================
# 3. Alert pop-up related
# ==============================================

# 3.1 alert_is_present
# Wait until javascript alert/confirm/prompt pops up
alert: Alert = wait.until(EC.alert_is_present())

alert.accept()       # Click OK
alert.dismiss()      # Click Cancel
alert.send_keys("input text")  # Input text for prompt alert
alert_text = alert.text        # Read alert message


# ==============================================
# 4. Iframe / Frame switch
# ==============================================

# 4.1 frame_to_be_available_and_switch_to_it
# Wait for iframe ready and automatically switch into it
wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "iframe-demo")))

# Switch back to main page
driver.switch_to.default_content()


# ==============================================
# 5. Window / Tab switch
# ==============================================

# 5.2 number_of_windows_to_be
# Wait until total browser tabs count equals target number
wait.until(EC.number_of_windows_to_be(2))

# 5.3 new_window_is_opened
# Wait for a new tab opened, return window handles
original_handles = driver.window_handles
new_handle = wait.until(EC.new_window_is_opened(original_handles))
driver.switch_to.window(new_handle[-1])


# ==============================================
# 6. Custom lambda wait (very flexible)
# ==============================================
# You can write your own judge condition
# Example: wait input value equal to 100
wait.until(lambda d: d.find_element(By.ID, "sum1").get_attribute("value") == "64")

# Example: wait url contains keyword
wait.until(lambda d: "simple-form-demo" in d.current_url)


# ==============================================
# Quick Selection Guide (Cheat Rule)
# ==============================================
"""
send_keys / read text      → visibility_of_element_located
click button / link        → element_to_be_clickable
only check html exists     → presence_of_element_located
wait loading disappear     → invisibility_of_element_located
wait alert popup           → alert_is_present()
wait iframe ready          → frame_to_be_available_and_switch_to_it
wait new tab               → new_window_is_opened
wait page refresh finish   → staleness_of(old_elem)
"""