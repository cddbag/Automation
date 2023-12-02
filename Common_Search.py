import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

from appium.options.android import UiAutomator2Options

capabilities = dict(
    platformName='Android',
    platformVersion='14',
    app="/Users/aquinas/Downloads/SSG.COM_3.5.1_Apkpure.apk",
    ensureWebviewsHavePages= True,
    nativeWebScreenshot= True,
    newCommandTimeout= 3600,
    connectHardwareKeyboard=True
)

appium_server_url="http://127.0.0.1:4723/wd/hub"

class Common_Search():

    def setUp(self) -> None:
        options = UiAutomator2Options()
        options.load_capabilities(capabilities)
        self.driver = webdriver.Remote(appium_server_url, options=options)

    def Search_Milk(self) -> None:
        self.driver.find_element(By.ID, 'kr.co.ssg:id/vSearchQuery').click()
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="검색")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="kr.co.ssg:id/etSearchQuery")
        el4.send_keys("우유")
        self.driver.press_keycode(66)
        self.driver.implicitly_wait(3)

    def Search_Clothes(self) -> None:
        self.driver.find_element(By.ID, 'kr.co.ssg:id/vSearchQuery').click()
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="검색")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="kr.co.ssg:id/etSearchQuery")
        el4.send_keys("티셔츠")
        self.driver.press_keycode(66)
        self.driver.implicitly_wait(3)
