from selenium import webdriver
from selenium.webdriver.common import *
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def loginToGoogle(driver,gmailId,passWord):
    try:
        print('--Initializing login--')
        driver.get(r'https://accounts.google.com/signin/v2/identifier?continue='+\
        'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1'+\
        '&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
        time.sleep(3)
        print('--entering credentials--')
        loginBox = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
        loginBox.send_keys(gmailId)

        nextButton = driver.find_elements(By.XPATH,'//*[@id ="identifierNext"]')
        nextButton[0].click()
        time.sleep(3)
        passWordBox = driver.find_element(By.XPATH,
            '//*[@id ="password"]/div[1]/div / div[1]/input')
        passWordBox.send_keys(passWord)
        
        nextButton = driver.find_element(By.XPATH,'//*[@id ="passwordNext"]')
        nextButton.click()
        print('--processed credentials--')
        print('Please approve if notification came to your phone. Time: 10 seconds')
        print('--waiting for approval via device/redirecting--')
        element = WebDriverWait(driver, 60).until(
            EC.title_contains('Inbox')
        )
        print('Login Successful...!!')
    except Exception as e:
        print('Login Failed--->'+str(e))