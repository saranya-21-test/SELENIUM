import time


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By




class Test_login_class:

    def test_login_sauce_demo(self):
        driver=webdriver.Edge("c:\\Drivers\\edgedriver_win64\\msedgedriver.exe")
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID,"user-name").send_keys("problem_user")
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        driver.find_element(By.ID,"login-button").click()
        time.sleep(6)
        assert True

    def test_login_facebook(self):
        driver=webdriver.Edge("c:\\Drivers\\edgedriver_win64\\msedgedriver.exe")
        driver.maximize_window()
        driver.get("https://www.facebook.com/")
        driver.find_element(By.ID,"email").send_keys("tharunmeeniga@gmail.com")
        driver.find_element(By.ID,"pass").send_keys("tharun@123")
        driver.find_element(By.NAME,"login").submit()
        time.sleep(8)
        assert True

    '''def test_instagram_login(self):
        driver=webdriver.Edge("c:\\Drivers\\edgedriver_win64\\msedgedriver.exe")
        driver.maximize_window()
        driver.get("https://www.instagram.com/accounts/login/?hl=en")
        driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[1]/div/label/input").send_keys("tharun_meeniga")
        driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[2]/div/label/input").send_keys("tharun@21")
        driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[3]").submit()
        time.sleep(10)
        assert True'''


    '''def test_instagram_login(self):
        driver=webdriver.Edge("c:\\Drivers\\edgedriver_win64\\msedgedriver.exe")
        driver.maximize_window()
        driver.get("https://www.instagram.com/accounts/login/?hl=en")
        driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[5]/button/div/div[2]").click()
        time.sleep(10)
        assert True'''


    '''def test_github(self):
        driver=webdriver.Edge("c:\\Drivers\\edgedriver_win64\\msedgedriver.exe")
        driver.maximize_window()
        driver.get("https://github.com/")
        driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/header/div/div[2]/div[3]/deferred-side-panel/include-fragment/react-partial-anchor/button/span/span/img").click()
        time.sleep(15)
        assert True'''

    def test_login_phptravels(self):
        driver = webdriver.Edge("c:\\Drivers\\edgedriver_win64\\msedgedriver.exe")
        driver.maximize_window()
        driver.get("https://app.phptravels.com/login")
        driver.find_element(By.ID, "email").send_keys("saranya.dwaram@gmail.com")
        driver.find_element(By.ID, "password").send_keys("428838")
        driver.find_element(By.XPATH, "//*[@id='submit']").click()
        assert True
        time.sleep(5)

    def test_login_msmfclasses(self):
        driver = webdriver.Edge("c:\\Drivers\\edgedriver_win64\\msedgedriver.exe")
        driver.maximize_window()
        driver.get("https://digitalcampus.msmfclasses.com:90/")
        driver.find_element(By.ID, "inputUsername").send_keys("20AT1A05I3")
        driver.find_element(By.ID, "inputpassword").send_keys("1234")
        driver.find_element(By.ID, "Button2").click()
        assert True
        time.sleep(5)

    def test_login_digitalcampus(self):
        driver = webdriver.Edge("c:\\Drivers\\edgedriver_win64\\msedgedriver.exe")
        driver.maximize_window()
        driver.get("https://digitalcampus.msmfclasses.com:94/")
        driver.find_element(By.ID, "username").send_keys("20at1a05h5@gpcet")
        driver.find_element(By.ID, "password").send_keys("GPCET@2020")
        driver.find_element(By.XPATH, "//*[@id='LinkButton2']/span[1]").click()
        assert True
        time.sleep(5)


