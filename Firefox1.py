from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://jobmight.com/session/signin")
email: object = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.NAME, "email"))))
email.send_keys("svetlanabarban@yahoo.com")
password: object = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.NAME, "password"))))
password.send_keys("Ss2101989")
login = WebDriverWait(driver, 20).until((EC.element_to_be_clickable((By.XPATH, "//button[contains(@type,'submit')]"))))
login.click()