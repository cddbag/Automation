import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

from appium.options.android import UiAutomator2Options


#capabilities = dict(
#    platformName='Android',
#    platformVersion='14',
#    app="/Users/aquinas/Downloads/SSG.COM_3.5.6_Apkpure.apk",
#    ensureWebviewsHavePages= True,
#    nativeWebScreenshot= True,
#    newCommandTimeout= 3600,
#    connectHardwareKeyboard=True
#)

#appium_server_url="http://127.0.0.1:4723/wd/hub"



class Common_Login():

#    def setUp(self) -> None:
#        options = UiAutomator2Options()
#        options.load_capabilities(capabilities)
#        self.driver = webdriver.Remote(appium_server_url, options=options)

    def Login(self) -> None:
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnMySSG').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/etUserId').send_keys('cddbag')
        self.driver.find_element(By.ID, 'kr.co.ssg:id/etUserPw').send_keys('Qa1324!@#')
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnLogin').click()
        self.driver.implicitly_wait(5)
        
