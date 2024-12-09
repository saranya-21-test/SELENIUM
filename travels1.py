from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Edge("c:\\Drivers\\edgedriver_win64\\msedgedriver.exe")
driver.get("https://travelsystem.org/login")
'''driver.find_element(By.NAME,"email").send_keys("admin@phptravels.com")
driver.find_element(By.NAME,"password").send_keys("demoadmin")
driver.find_element(By.ID,"submitBTN").click()'''
'''driver.find_element(By.NAME,"email").send_keys("user@phptravels.com")
driver.find_element(By.NAME,"password").send_keys("demouser")
driver.find_element(By.ID,"submitBTN").click()'''
'''driver.find_element(By.NAME,"email").send_keys("agent@phptravels.com")
driver.find_element(By.NAME,"password").send_keys("demoagent")
driver.find_element(By.ID,"submitBTN").click()'''
driver.find_element(By.NAME,"email").send_keys("supplier@phptravels.com")
driver.find_element(By.NAME,"password").send_keys("demosupplier")
driver.find_element(By.ID,"submitBTN").click()
time.sleep(10)