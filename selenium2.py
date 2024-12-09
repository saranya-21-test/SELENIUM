from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Edge("c:\\Drivers\\edgedriver_win64\\msedgedriver.exe")
driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
driver.find_element(By.NAME,"session_key").send_keys("saranya.dwaram@gmail.com")
driver.find_element(By.NAME,"session_password").send_keys("Saranya_21")
driver.find_element(By.XPATH,"//*[@id='organic-div']/form/div[4]/button").click()
time.sleep(10)