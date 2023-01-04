from google import loginToGoogle
from selenium import webdriver
from selenium.webdriver.common import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

try:
    optionsx = Options()
    pathToData = input("Please enter path to your user data: ")
    if(pathToData == ''):
        print("Looking for older paths")
        with open('readme.txt') as f:
            lines = f.readlines()
        pathToData = lines[0]
    else:
        print("updating new path")
        with open('readme.txt', 'w') as f:
            f.write(pathToData)
        f.close()
    optionsx.add_argument("--user-data-dir="+pathToData)
    optionsx.add_experimental_option("detach", True)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=optionsx)
    try:  
        loginToGoogle(driver, '', '')
    except Exception as e:
        print('Login failed, maybe you are already logged in?--->'+str(e))
    finally:
        driver.get('https://mentor.crio.do/')
except Exception as e:
    print("OOPS SOMETHING WENT WRONG!!--->"+str(e))