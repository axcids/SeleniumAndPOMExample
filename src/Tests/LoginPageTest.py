from src.Pages.LoginPage import LoginPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest

class LoginPageTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.service = Service(executable_path=r'C:\Program Files\browser-drivers\chromedriver.exe')
        cls.options = webdriver.ChromeOptions()
        cls.driver = webdriver.Chrome(service=cls.service, options=cls.options)

        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        
    def positive_login_test(self):
        driver = self.driver
        self.driver.get("https://demowebshop.tricentis.com/login")
        login = LoginPage(driver)
        login.enter_email("useremail@domain.com")
        login.enter_password("123456")
        login.click_login_button()
        
        time.sleep(5)

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
            
    

