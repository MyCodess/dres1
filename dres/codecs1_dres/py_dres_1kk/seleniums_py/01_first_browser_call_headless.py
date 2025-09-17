# -see: examples/python/tests/getting_started/first_script.py  , https://www.selenium.dev/documentation/webdriver/getting_started/first_script/
#   BUT headless ! (no browser-GUI reuired) ! modifed of above url to avoid browser-GUI requirement!

from selenium import webdriver
from selenium.webdriver.common.by import By

# func to make pause to view the steps! rewrite it to go through! :
def pause1(msg1: str = "--- next-setp ---"): print(msg1)   # -stop is NOT required, since headless!  input(msg1)

# set up ChromeOptions for headless call / no-GUI:
options = webdriver.ChromeOptions()

# add headless Chrome option
options.add_argument("--headless=new")

# set up Chrome in headless mode
driver = webdriver.Chrome(options=options)

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title
driver.implicitly_wait(0.5)

text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

text_box.send_keys("test11-txt")
pause1()
submit_button.click()
pause1()

message = driver.find_element(by=By.ID, value="message")
text1 = message.text
pause1("_______________")
pause1("- message received after submit-button-click:   " + text1)
print(f"- Page URL:       {driver.current_url}")
print(f"- Page Title:     {driver.title}")
pause1("_______________")

driver.quit()

