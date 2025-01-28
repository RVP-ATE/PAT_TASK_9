from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

url = "https://www.saucedemo.com"

driver = webdriver.Chrome()
# Open the webpage to url
driver.get(url)
sleep(5)

#maximise window
driver.maximize_window()

#title of page
page_title = driver.title
print("Page Title: ", page_title)

#Finding the web element for user-name input
webelement_of_username_input = driver.find_element(By.XPATH,'//input[@id="user-name"]')
#After Finding send user-name as input
webelement_of_username_input.send_keys("standard_user")

sleep(5)

webelement_of_password_input = driver.find_element(By.XPATH,'//input[@id="password"]')
webelement_of_password_input.send_keys("secret_sauce")

sleep(5)

submit_button = driver.find_element(By.XPATH, '//input[@id="login-button"]')

submit_button.click()

sleep(5)

#Current URL of the page
current_url = driver.current_url
print("Current URL: ", current_url)

# The Entire page contents
page_content = driver.page_source

# Save the page contents to a text file
with open("Webpage_task_11.txt", "w", encoding="utf-8") as file:
    file.write(page_content)

sleep(5)

# Close the browser
driver.quit()