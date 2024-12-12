from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import time



driver=webdriver.Edge("c:\\Drivers\\edgedriver_win64\\msedgedriver.exe")
#driver=webdriver.Edge(executable_path="C:/Drivers/edgedriver_win64/msedgedriver.exe")
#driver.implicitly_wait(10)
#driver.maximize_window()


driver.get("http://meettheminds.com/signup")
#driver.implicitly_wait(10)
#driver.maximize_window()


driver.find_element(By.ID,"mat-input-0").send_keys("Dvaram")
driver.find_element(By.ID,"mat-input-1").send_keys("venkata")
driver.find_element(By.ID,"mat-input-2").send_keys("Saranya")
driver.find_element(By.ID,"mat-input-3").send_keys("9876543212")
driver.find_element(By.ID,"mat-input-4").send_keys("saranya.dwaram@gmail.com")
driver.find_element(By.ID,"mat-input-5").send_keys("Student")
driver.find_element(By.ID,"mat-input-6").send_keys("KPHB")
driver.find_element(By.ID,"mat-input-7").send_keys("Hyderabad")
#driver=webdriver.Edge(executable_path="C:/Drivers/edgedriver_win64/msedgedriver.exe")
#driver.implicitly_wait(10)
#driver.maximize_window()
#dropdown=Select(driver.find_element_by_xpath("//*[@id='mat-select-value-1']/span"))
#dropdown=Select(driver.find_element(By.XPATH,"//*[@id="mat-select-value-1"]/span"))
#dropdown.select_by_visible_text("India")
#dropdown.select_by_index(0)
#dropdown=Select(driver.find_element_by_class_name("mat-mdc-select-placeholder mat-mdc-select-min-line ng-tns-c3393473648-15 ng-star-inserted"))
#dropdown.select_by_visible_text("India")
driver.find_element(By.ID,"mat-input-8").send_keys("518401")
driver.find_element(By.ID,"mat-input-9").send_keys("saranya.dwaram@gmail.com")
driver.find_element(By.ID,"mat-input-10").send_keys("Saru@143")
driver.find_element(By.ID,"mat-input-11").send_keys("Saru@143")
driver.find_element(By.CLASS_NAME,"submit-container").submit()





time.sleep(10)