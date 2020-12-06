from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import time
driver = webdriver.Chrome()
driver.get("http://jobmight.com/session/signup")
first_name: object = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.NAME, "firstName"))))
first_name.send_keys("Svetlana")
last_name: object = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.NAME, "lastName"))))
last_name.send_keys("Barban")
email: object = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.NAME, "email"))))
email.send_keys("uncasi@yahoo.com")
password: object = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.NAME, "password"))))
password.send_keys("1")
check_button = WebDriverWait(driver, 20).until((EC.element_to_be_clickable((By.NAME, "agreement"))))
check_button.click()
close_button = WebDriverWait(driver, 20).until(
    (EC.element_to_be_clickable((By.XPATH("//*[contains(text(),'Close')]")))))
close_button.click()
sign_in_button = WebDriverWait(driver, 20).until(
    (EC.element_to_be_clickable((By.XPATH("///*[contains(text(),'Sign in')]")))))
sign_in_button.click()
error_notification = WebDriverWait(driver, 60).until((EC.visibility_of_element_located((By.XPATH, "//p[contains(@class,'MuiFormHelperText-root MuiFormHelperText-contained Mui-error MuiFormHelperText-filled')]"))))
assert error_notification.text == "Password must contain a capital letter and symbol"