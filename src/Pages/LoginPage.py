from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage():
    
    def __init__(self, driver):
        self.driver = driver
        self.loginEmailTextBox = "/html/body/div[4]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a"
        self.loginPasswordTextBox = "/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[3]/input"
        self.loginRememberMeCheckBox = "/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[4]/input[1]"
        self.loginForgetPasswordLink = "/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[4]/span/a"
        self.loginButton = "/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[5]/input"
        
        
    def enter_email(self, email):
        self.find_element(By.XPATH, self.loginEmailTextBox).clear()
        self.find_element(By.XPATH, self.loginEmailTextBox).send_keys(email)
        
    def enter_password(self, password):
        self.find_element(By.XPATH, self.loginPasswordTextBox).clear()
        self.find_element(By.XPATH, self.loginPasswordTextBox).send_keys(password)
        
    def click_login_button(self):
        self.find_element(By.XPATH, self.loginButton).click()

        
