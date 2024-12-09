from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Edge("c:\\Drivers\\edgedriver_win64\\msedgedriver.exe")
driver.get("https://phptravels.com/demo/")
driver.find_element(By.NAME,"first_name").send_keys("Dvaram")
driver.find_element(By.NAME,"last_name").send_keys("saranya")
driver.find_element(By.NAME,"whatsapp").send_keys("9121743133")
driver.find_element(By.NAME,"business_name").send_keys("transport")
driver.find_element(By.NAME,"email").send_keys("saranya.dwaram@gmail.com")
#driver.find_element(By.ID,"number").send_keys("8")
driver.find_element(By.ID,"demo").click()
time.sleep(10)