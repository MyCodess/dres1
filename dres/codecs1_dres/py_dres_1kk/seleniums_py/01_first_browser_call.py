# -see: examples/python/tests/getting_started/first_script.py  , https://www.selenium.dev/documentation/webdriver/getting_started/first_script/

from selenium import webdriver
from selenium.webdriver.common.by import By

# func to make pause to view the steps! rewrite it to go through! :
def pause1(msg1: str = "\n---pause1 ---\n"): input(msg1)

driver = webdriver.Chrome()

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
pause1(text1)

driver.quit()

