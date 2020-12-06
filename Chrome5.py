from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://jobmight.com/session/signin")
forgotpassword = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Forgot password?')]")))
forgotpassword.click()
email: object = WebDriverWait(driver, 60).until((EC.visibility_of_element_located((By.XPATH, "//input[@type='email']"))))
email.send_keys("svetlanabarban@yahoo.com")
reset_password = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Reset Password')]")))
reset_password.click()
confirmation = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, "//form[contains(text(),'Email successfully sent. If you have registered an')]")))
