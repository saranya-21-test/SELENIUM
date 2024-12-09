from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Edge("c:\\Drivers\\edgedriver_win64\\msedgedriver.exe")

driver.get("https://www.actnowcloud.com/#/actnowcloud/student-registration")
driver.find_element(By.ID,"mat-input-0").send_keys("Dvaram")
driver.find_element(By.ID,"mat-input-1").send_keys("saranya")
driver.find_element(By.ID,"mat-input-2").send_keys("saranya.dwaram@gmail.com")
driver.find_element(By.ID,"mat-input-3").send_keys("9121743133")
driver.find_element(By.ID,"mat-input-4").send_keys("Saru@143")
driver.find_element(By.ID,"mat-input-5").send_keys("Saru@143")
driver.find_element(By.ID,"mat-input-6").send_keys("KPHB")
driver.find_element(By.ID,"mat-input-7").send_keys("Hyderabad")
driver.find_element(By.ID,"mat-input-8").send_keys("Telangana")
driver.find_element(By.ID,"mat-input-9").send_keys("India")
driver.find_element(By.ID,"mat-input-10").send_keys("518401")
driver.find_element(By.CLASS_NAME,"submit-container").submit()


time.sleep(10)