from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException


from appium.options.android import UiAutomator2Options

class Common():

    def Splash(self) -> None:
        sleep(2)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnConfirm').click()
        self.driver.implicitly_wait(1)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnYes').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/ivHeader').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcClose').click()
        self.driver.implicitly_wait(1)

    def Login(self) -> None:
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnMySSG').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/etUserId').send_keys('cddbag')
        self.driver.find_element(By.ID, 'kr.co.ssg:id/etUserPw').send_keys('Qa1324!@#')
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnLogin').click()
        self.driver.implicitly_wait(5)

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

    def scroll_to_bottom(self):
    # TouchAction을 사용하여 스크롤 다운
        self.driver.swipe(150, 1400, 150, 200, 150)

    def scroll_to_bottom_search(self):
        el1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='검색')
        el2 = self.driver.find_element(By.XPATH, '(//android.widget.Button[@content-desc="좋아요"])[7]')
        self.driver.scroll(el2, el1, None)
        