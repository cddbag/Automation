import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from SSG_APP_AOS.Common_splash import Common_splash
from SSG_APP_AOS.Common_Login import Common_Login


from appium.options.android import UiAutomator2Options


capabilities = dict(
    platformName='Android',
    platformVersion='14',
    #appActivity='kr.co.ssg.activity.etc.MainActivity',
    app="/Users/aquinas/Downloads/SSG.COM_3.5.1_Apkpure.apk",
    ensureWebviewsHavePages= True,
    nativeWebScreenshot= True,
    newCommandTimeout= 3600,
    connectHardwareKeyboard=True
)

appium_server_url="http://127.0.0.1:4723/wd/hub"

class TestAppium(unittest.TestCase):
    # def setUp(self) -> None:
    #     self.driver = webdriver.Remote(appium_server_url, capabilities)
    def setUp(self) -> None:
        options = UiAutomator2Options()
        options.load_capabilities(capabilities)
        self.driver = webdriver.Remote(appium_server_url, options=options)


    def test_case_01(self) -> None:
        Common_splash.Splash(self)
        Common_Login.Login(self)
        assert self.driver.find_element(By.XPATH, '//android.view.View[@content-desc="김덕환 님"]').is_displayed(), "회원명 확인 실패"
        # 회원명 노출 확인(로그인 성공)


    def test_case_02(self) -> None:
        sleep(3)
        Common_splash.splash(self)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnMySSG').click()
        # 신세계 유니버스 클럽 가입 계정정보
        self.driver.find_element(By.ID, 'kr.co.ssg:id/etUserId').send_keys('cddbag')
        self.driver.find_element(By.ID, 'kr.co.ssg:id/etUserPw').send_keys('Qa1324!@#')
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnLogin').click()
        self.driver.implicitly_wait(5)
        # 신세계 유버 클럽 뱃지 노출 확인
        assert self.driver.find_element(By.XPATH, '//android.view.View[@content-desc="신세계 유니버스 클럽 뱃지"]').is_displayed(), "신세계 유니버스 클럽 뱃지 노출 확인 실패"

    def test_case_03(self) -> None:
        sleep(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnConfirm').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnYes').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/ivHeader').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcClose').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnMySSG').click()
        # 신세계 유니버스 클럽 가입 계정정보
        self.driver.find_element(By.ID, 'kr.co.ssg:id/etUserId').send_keys('cddbag')
        self.driver.find_element(By.ID, 'kr.co.ssg:id/etUserPw').send_keys('Qa1324!@#')
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnLogin').click()
        self.driver.implicitly_wait(5)
        # 신유클 관리 페이지 랜딩 확인
        self.driver.find_element(By.XPATH, '//android.view.View[@content-desc="신세계 유니버스 클럽 뱃지"]').click()
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/tvTitle').is_displayed(), "신세계 유니버스 클럽 관리 페이지 랜딩 확인 실패"


    def test_case_04(self) -> None:
        sleep(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnConfirm').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnYes').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/ivHeader').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcClose').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnMySSG').click()
        # 신세계 유니버스 클럽 가입 계정정보
        self.driver.find_element(By.ID, 'kr.co.ssg:id/etUserId').send_keys('cddbag')
        self.driver.find_element(By.ID, 'kr.co.ssg:id/etUserPw').send_keys('Qa1324!@#')
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnLogin').click()
        self.driver.implicitly_wait(5)
        # 회원 등급 뱃지 노출 확인
        assert self.driver.find_element(By.XPATH, '//android.view.View[@content-desc="VIP 등급 뱃지"]').is_displayed(), "등급 뱃지 노출 확인 실패"


    def test_case_05(self) -> None:
        sleep(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnConfirm').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnYes').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/ivHeader').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcClose').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnMySSG').click()
        # 신세계 유니버스 클럽 가입 계정정보
        self.driver.find_element(By.ID, 'kr.co.ssg:id/etUserId').send_keys('cddbag')
        self.driver.find_element(By.ID, 'kr.co.ssg:id/etUserPw').send_keys('Qa1324!@#')
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnLogin').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, '//android.view.View[@content-desc="VIP 등급 뱃지"]').click()
        self.driver.implicitly_wait(5)
        # 유니버스 클럽 스탬프 페이지 랜딩 확인
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/tvTitle').is_displayed(), "유니버스 클럽 스탬프 페이지 랜딩 실패"

  

    def test_case_06(self) -> None:
        sleep(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnConfirm').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnYes').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/ivHeader').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcClose').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnMySSG').click()
        # 신세계 유니버스 클럽 가입 계정정보
        self.driver.find_element(By.ID, 'kr.co.ssg:id/etUserId').send_keys('cddbag')
        self.driver.find_element(By.ID, 'kr.co.ssg:id/etUserPw').send_keys('Qa1324!@#')
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnLogin').click()
        self.driver.implicitly_wait(5)
        # 멤버십 쿠폰 버튼 노출 확인
        assert self.driver.find_element(By.XPATH, '//android.view.View[@content-desc="멤버십쿠폰"]').is_displayed(), "멤버십쿠폰 노출 확인 실패"
        

    def test_case_07(self) -> None:
        sleep(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnConfirm').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnYes').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/ivHeader').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcClose').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnMySSG').click()
        # 신세계 유니버스 클럽 가입 계정정보
        self.driver.find_element(By.ID, 'kr.co.ssg:id/etUserId').send_keys('cddbag')
        self.driver.find_element(By.ID, 'kr.co.ssg:id/etUserPw').send_keys('Qa1324!@#')
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnLogin').click()
        self.driver.implicitly_wait(5)
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/sdvBlurBackground2').is_displayed(), "신유클 배경 미노출"
        # 신유클 배경 노출 확인

    def test_case_08(self) -> None:
        sleep(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnConfirm').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnYes').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/ivHeader').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcClose').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnMySSG').click()
        # 신세계 유니버스 클럽 가입 계정정보
        self.driver.find_element(By.ID, 'kr.co.ssg:id/etUserId').send_keys('cddbag')
        self.driver.find_element(By.ID, 'kr.co.ssg:id/etUserPw').send_keys('Qa1324!@#')
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnLogin').click()
        self.driver.implicitly_wait(5)
        assert self.driver.find_element(By.XPATH, '//android.view.View[@content-desc="고객님께 1년동안 멤버십VIP 혜택이 유지됩니다."]').is_displayed(), "신유클 공지사항 미노출"
        # 신유클 공지사항 노출 확인

    def test_case_09(self) -> None:
        sleep(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnConfirm').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnYes').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/ivHeader').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcClose').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnMySSG').click()
        # 신세계 유니버스 클럽 가입 계정정보
        self.driver.find_element(By.ID, 'kr.co.ssg:id/etUserId').send_keys('cddbag')
        self.driver.find_element(By.ID, 'kr.co.ssg:id/etUserPw').send_keys('Qa1324!@#')
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnLogin').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, '//android.view.View[@content-desc="고객님께 1년동안 멤버십VIP 혜택이 유지됩니다."]').click()
        self.driver.implicitly_wait(3)
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/tvTitle').is_displayed(), "유니버스 클럽 스탬프 페이지 랜딩 실패"
        # 유니버스 클럽 스탬프 페이지 랜딩 확인


    def test_case_10(self) -> None:
        sleep(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnConfirm').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnYes').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/ivHeader').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcClose').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnMySSG').click()
        # 신세계 유니버스 클럽 가입 계정정보
        self.driver.find_element(By.ID, 'kr.co.ssg:id/etUserId').send_keys('cddbag')
        self.driver.find_element(By.ID, 'kr.co.ssg:id/etUserPw').send_keys('Qa1324!@#')
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnLogin').click()
        self.driver.implicitly_wait(5)
        el = self.driver.find_element(By.ID, 'm_content')
        text = el.text
        assert 'SSG에서' in text
        ###추가작업 필요


        # assert self.driver.find_element(By.XPATH, '//android.view.View[@content-desc="SSG에서 이번달 18,676원 혜택을 받았어요 "]').is_displayed(), "쇼핑 안내 문구 미노출"
        # 쇼핑 안내 문구 노출 확인


    def test_case_11(self) -> None:
        sleep(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnConfirm').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnYes').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/ivHeader').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcClose').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnMySSG').click()
        # 신세계 유니버스 클럽 가입 계정정보
        self.driver.find_element(By.ID, 'kr.co.ssg:id/etUserId').send_keys('cddbag')
        self.driver.find_element(By.ID, 'kr.co.ssg:id/etUserPw').send_keys('Qa1324!@#')
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnLogin').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'SSG').click()
        self.driver.implicitly_wait(3)
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/tvTitle').is_displayed(), "나의 신세계 유니버스 클럽 헤택 페이지 랜딩 실패"
        # 쇼핑 안내 문구 노출 확인
        ###추가작업 필요


    def test_case_12(self) -> None:
        sleep(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnConfirm').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnYes').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/ivHeader').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcClose').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/vSearchQuery').click()
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="검색")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="kr.co.ssg:id/etSearchQuery")
        el4.send_keys("우유")
        el5 = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView")
        el5.click()
        self.driver.implicitly_wait(3)
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/rvKeyword').is_displayed(), "연관검색어 로딩 실패"
        # 연관검색어 노출 확인

    
    def test_case_13(self) -> None:
        sleep(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnConfirm').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnYes').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/ivHeader').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcClose').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/vSearchQuery').click()
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="검색")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="kr.co.ssg:id/etSearchQuery")
        el4.send_keys("우유")
        el5 = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView")
        el5.click()
        self.driver.implicitly_wait(3)
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/rvKeyword').is_displayed(), "연관검색어 로딩 실패"
        # 연관검색어 노출 확인


    def test_case_14(self) -> None:
        sleep(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnConfirm').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnYes').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/ivHeader').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcClose').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/vSearchQuery').click()
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="검색")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="kr.co.ssg:id/etSearchQuery")
        el4.send_keys("우유")
        el5 = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView")
        el5.click()
        self.driver.implicitly_wait(3)
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/rvUpper').is_displayed(), "배송유형 로딩 실패"
        # 배송유형필터 노출 확인


    def test_case_15(self) -> None:
        sleep(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnConfirm').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnYes').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/ivHeader').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcClose').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/vSearchQuery').click()
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="검색")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="kr.co.ssg:id/etSearchQuery")
        el4.send_keys("우유")
        el5 = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView")
        el5.click()
        self.driver.implicitly_wait(3)
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/rvLower').is_displayed(), "상품유형 로딩 실패"
        # 상품유형필터 노출 확인
        

    def test_case_16(self) -> None:
        sleep(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnConfirm').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnYes').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/ivHeader').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcClose').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/vSearchQuery').click()
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="검색")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="kr.co.ssg:id/etSearchQuery")
        el4.send_keys("우유")
        el5 = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView")
        el5.click()
        self.driver.implicitly_wait(3)
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/btnSort').is_displayed(), "정렬필터 로딩 실패"
        # 정렬필터 노출 확인


    def test_case_17(self) -> None:
        sleep(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnConfirm').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnYes').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/ivHeader').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcClose').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/vSearchQuery').click()
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="검색")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="kr.co.ssg:id/etSearchQuery")
        el4.send_keys("우유")
        el5 = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView")
        el5.click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="가격 필터"]/android.widget.TextView').click()
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/lyTab').is_displayed(), "바텀시트 검색 필터 로딩 실패"
        # 바텀시트 검색 필터 노출 확인


    def test_case_18(self) -> None:
        sleep(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnConfirm').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnYes').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/ivHeader').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcClose').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/vSearchQuery').click()
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="검색")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="kr.co.ssg:id/etSearchQuery")
        el4.send_keys("우유")
        el5 = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView")
        el5.click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="가격 필터"]/android.widget.TextView').click()
        assert self.driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView').is_displayed(), "바텀시트 가격 필터 로딩 실패"
        # 바텀시트 검색 필터 노출 확인


    def test_case_19(self) -> None:
        sleep(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnConfirm').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnYes').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/ivHeader').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcClose').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/vSearchQuery').click()
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="검색")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="kr.co.ssg:id/etSearchQuery")
        el4.send_keys("우유")
        el5 = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView")
        el5.click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="가격 필터"]/android.widget.TextView').click()
        assert self.driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView').is_displayed(), "바텀시트 혜택 필터 로딩 실패"
        # 바텀시트 혜택 필터 노출 확인


    def test_case_20(self) -> None:
        sleep(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnConfirm').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnYes').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/ivHeader').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcClose').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/vSearchQuery').click()
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="검색")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="kr.co.ssg:id/etSearchQuery")
        el4.send_keys("우유")
        el5 = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView")
        el5.click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="가격 필터"]/android.widget.TextView').click()
        assert self.driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.TextView').is_displayed(), "바텀시트 카테고리 필터 로딩 실패"
        # 바텀시트 카테고리 필터 노출 확인
    

    def test_case_21(self) -> None:
        sleep(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnConfirm').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnYes').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/ivHeader').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcClose').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/vSearchQuery').click()
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="검색")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="kr.co.ssg:id/etSearchQuery")
        el4.send_keys("우유")
        el5 = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView")
        el5.click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="가격 필터"]/android.widget.TextView').click()
        assert self.driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[4]/android.widget.TextView').is_displayed(), "바텀시트 배송유형 필터 로딩 실패"
        # 바텀시트 배송유형 필터 노출 확인
    

    def test_case_22(self) -> None:
        sleep(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnConfirm').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnYes').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/ivHeader').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcClose').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/vSearchQuery').click()
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="검색")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="kr.co.ssg:id/etSearchQuery")
        el4.send_keys("우유")
        el5 = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView")
        el5.click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="가격 필터"]/android.widget.TextView').click()
        assert self.driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[5]/android.widget.TextView').is_displayed(), "바텀시트 상품유형 필터 로딩 실패"
        # 바텀시트 상품유형 필터 노출 확인



    def test_case_23(self) -> None:
        sleep(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnConfirm').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnYes').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/ivHeader').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcClose').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/vSearchQuery').click()
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="검색")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="kr.co.ssg:id/etSearchQuery")
        el4.send_keys("우유")
        el5 = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView")
        el5.click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="가격 필터"]/android.widget.TextView').click()
        assert self.driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[6]/android.widget.TextView').is_displayed(), "바텀시트 브랜드 필터 로딩 실패"
        # 바텀시트 브랜드 필터 노출 확인

    def test_case_24(self) -> None:
        sleep(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnConfirm').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnYes').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/ivHeader').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcClose').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/vSearchQuery').click()
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="검색")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="kr.co.ssg:id/etSearchQuery")
        el4.send_keys("우유")
        el5 = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView")
        el5.click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="가격 필터"]/android.widget.TextView').click()
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/etMin').is_displayed(), "바텀시트 최소금액 필터 로딩 실패"
        # 바텀시트 가격 필터 내 최소금액 필터 노출 확인


    def test_case_25(self) -> None:
        sleep(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnConfirm').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnYes').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/ivHeader').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcClose').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/vSearchQuery').click()
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="검색")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="kr.co.ssg:id/etSearchQuery")
        el4.send_keys("우유")
        el5 = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView")
        el5.click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="가격 필터"]/android.widget.TextView').click()
        self.driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.TextView').click()
        assert self.driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout[2]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView[1]').is_displayed(), "카테고리 추천 필터 로딩 실패"
        # 바텀시트 카테고리 필터 내 추천 카테고리 필터 노출 확인


    def test_case_26(self) -> None:
        sleep(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnConfirm').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnYes').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/ivHeader').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcClose').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/vSearchQuery').click()
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="검색")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="kr.co.ssg:id/etSearchQuery")
        el4.send_keys("우유")
        el5 = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView")
        el5.click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="특징 필터"]').click()
        self.driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout[2]/androidx.recyclerview.widget.RecyclerView/androidx.recyclerview.widget.RecyclerView[1]/android.widget.Button[1]').click()
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/bcName').is_displayed(), "검색필터 히스토리 확인 실패"
        # 검색 필터 적용 시 히스토리 노출 확인 


    def test_case_27(self) -> None:
        sleep(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnConfirm').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnYes').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/ivHeader').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcClose').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/vSearchQuery').click()
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="검색")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="kr.co.ssg:id/etSearchQuery")
        el4.send_keys("우유")
        el5 = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView")
        el5.click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="특징 필터"]').click()
        self.driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout[2]/androidx.recyclerview.widget.RecyclerView/androidx.recyclerview.widget.RecyclerView[1]/android.widget.Button[1]').click()
        assert self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="특징 필터"]').is_selected(), "배경 특징 필터 활성화 확인 실패"
        # 바텀시트 특징 필터 적용 시 배경 특징 필터 활성화 확인 
    

    def test_case_28(self) -> None:
        sleep(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnConfirm').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnYes').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/ivHeader').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcClose').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/vSearchQuery').click()
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="검색")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="kr.co.ssg:id/etSearchQuery")
        el4.send_keys("우유")
        el5 = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView")
        el5.click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="해제 상태 쓱배송 필터"]/android.widget.ImageView').click()
        assert self.driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="선택 상태 쓱배송 필터"]/android.widget.ImageView').is_selected(), "쓱배송 필터 활성화 확인 실패"
        # 쓱배송 필터 클릭시 활성화 확인


    def test_case_29(self) -> None:
        sleep(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnConfirm').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnYes').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/ivHeader').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcClose').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/vSearchQuery').click()
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="검색")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="kr.co.ssg:id/etSearchQuery")
        el4.send_keys("우유")
        el5 = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView")
        el5.click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="해제 상태 쓱배송 필터"]/android.widget.ImageView').click()
        assert self.driver.find_element(By.XPATH, '(//android.widget.Button[@content-desc="배송유형 필터"]/android.widget.TextView').is_selected(), "쓱배송 필터 적용시 배송유형 바닥필터 노출 확인 실패"
        # 쓱배송 필터 클릭시 배송유형 바닥필터 활성화 확인


    def test_case_30(self) -> None:
        sleep(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnConfirm').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnYes').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/ivHeader').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcClose').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/vSearchQuery').click()
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="검색")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="kr.co.ssg:id/etSearchQuery")
        el4.send_keys("우유")
        el5 = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView")
        el5.click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="해제 상태 쓱배송 필터"]/android.widget.ImageView').click()
        assert self.driver.find_element(By.XPATH, '(//android.widget.LinearLayout[@content-desc="쓱배송 안내 버튼"])[1]/android.widget.ImageView').is_displayed(), "쓱배송 필터 적용 확인 실패"
        # 쓱배송 필터 클릭시 쓱배송 상품 노출 확인


    def test_case_31(self) -> None:
        sleep(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnConfirm').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnYes').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/ivHeader').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcClose').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/vSearchQuery').click()
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="검색")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="kr.co.ssg:id/etSearchQuery")
        el4.send_keys("티셔츠")
        el5 = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView")
        el5.click()
        self.driver.implicitly_wait(3)
        assert self.driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="해제 상태 선물포장 필터"]/android.widget.Button/android.widget.TextView').is_displayed(), "의류 검색 결과 선물포장 필터 노출 확인 실패"
        # 의류 검색 시 선물포장 필터 노출 확인


    def test_case_32(self) -> None:
        sleep(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnConfirm').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnYes').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/ivHeader').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcClose').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/vSearchQuery').click()
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="검색")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="kr.co.ssg:id/etSearchQuery")
        el4.send_keys("티셔츠")
        el5 = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView")
        el5.click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="해제 상태 선물포장 필터"]/android.widget.Button/android.widget.TextView').click()
        assert self.driver.find_element(By.XPATH, '(//android.widget.TextView[@content-desc="선물포장 상품"])[1]').is_displayed(), "선물포장 필터 적용 확인 실패"
        # 선물포장 필터 클릭시 선물포장 상품 노출 확인


    def test_case_33(self) -> None:
        sleep(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnConfirm').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnYes').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/ivHeader').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcClose').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/vSearchQuery').click()
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="검색")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="kr.co.ssg:id/etSearchQuery")
        el4.send_keys("티셔츠")
        el5 = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView")
        el5.click()
        self.driver.implicitly_wait(3)
        assert self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="스타일 필터"]').is_displayed(), "의류 검색 시 스타일 필터 노출 확인 실패"
        # 의류 검색시 스타일 필터 노출 확인


    def test_case_34(self) -> None:
        sleep(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnConfirm').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnYes').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/ivHeader').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcClose').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/vSearchQuery').click()
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="검색")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="kr.co.ssg:id/etSearchQuery")
        el4.send_keys("티셔츠")
        el5 = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView")
        el5.click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="스타일 필터"]').click()
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/vpContent').is_displayed(), "바닥필터 스타일 필터 클릭 시 바텀시트 스타일 필터 노출 확인 실패"
        # 바닥필터 스타일 필터 클릭 시 바텀시트 스타일 필터 노출 확인


    


    def test_case_35(self) -> None:
        sleep(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnConfirm').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnYes').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/ivHeader').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcClose').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/vSearchQuery').click()
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="검색")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="kr.co.ssg:id/etSearchQuery")
        el4.send_keys("티셔츠")
        el5 = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView")
        el5.click()
        self.driver.implicitly_wait(3)
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/btnSort').is_displayed(), "정렬필터 확인 실패"
        # 검색결과 페이지에 정렬필터 노출 확인


    def test_case_36(self) -> None:
        sleep(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnConfirm').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnYes').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/ivHeader').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcClose').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/vSearchQuery').click()
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="검색")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="kr.co.ssg:id/etSearchQuery")
        el4.send_keys("티셔츠")
        el5 = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView")
        el5.click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnSort').click()
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/rvList').is_displayed(), "바텀시트 정렬필터 확인 실패"
        # 검색결과 페이지의 정렬필터 클릭 시, 바텀시트 정렬필터 노출 확인


    def test_case_37(self) -> None:
        sleep(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnConfirm').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnYes').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/ivHeader').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcClose').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/vSearchQuery').click()
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="검색")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="kr.co.ssg:id/etSearchQuery")
        el4.send_keys("티셔츠")
        el5 = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView")
        el5.click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnSort').click()
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/bcInfo').is_displayed(), "바텀시트 추천순 정렬 안내 아이콘 확인 실패"
        # 바텀시트 정렬필터에 추천순 필터 안내 아이콘 노출 확인

    
    def test_case_38(self) -> None:
        sleep(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnConfirm').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnYes').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/ivHeader').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcClose').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/vSearchQuery').click()
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="검색")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="kr.co.ssg:id/etSearchQuery")
        el4.send_keys("티셔츠")
        el5 = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView")
        el5.click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnSort').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcInfo').click()
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/tvMessage').is_displayed(), "추천순 안내 메시지 확인 실패"
        # 바텀시트 정렬필터에 추천순 필터 안내 아이콘 클릭 시 안내 메시지 팝업 노출 확인


    def test_case_39(self) -> None:
        sleep(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnConfirm').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnYes').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/ivHeader').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcClose').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/vSearchQuery').click()
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="검색")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="kr.co.ssg:id/etSearchQuery")
        el4.send_keys("티셔츠")
        el5 = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView")
        el5.click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnSort').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcInfo').click()
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/btnPositive').is_displayed, "추천순 안내팝업 확인버튼 확인 실패"
        # 추천순 안내 메시지 팝업 내 확인 버튼 노출 확인


    def test_case_40(self) -> None:
        sleep(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnConfirm').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnYes').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/ivHeader').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcClose').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/vSearchQuery').click()
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="검색")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="kr.co.ssg:id/etSearchQuery")
        el4.send_keys("티셔츠")
        el5 = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView")
        el5.click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnSort').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcInfo').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnPositive').click()
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/bcInfo').is_enabled, "추천순 안내팝업 확인버튼 닫기 동작 확인 실패"
        # 추천순 안내 메시지 팝업 내 확인 버튼 클릭 시 팝업 닫힘 동작 확인


    
    def test_case_41(self) -> None:
        sleep(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnConfirm').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnYes').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/ivHeader').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcClose').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/vSearchQuery').click()
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="검색")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="kr.co.ssg:id/etSearchQuery")
        el4.send_keys("우유")
        el5 = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView")
        el5.click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="카테고리 필터"]').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/tvRecomCtg').click()
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/cbArray').is_selected(), "추천카테고리 클릭 동작 확인 실패"
        # 바텀시트 추천 카테고리 클릭 시 자동 선택 확인

    

    def test_case_42(self) -> None:
        sleep(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnConfirm').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnYes').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/ivHeader').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcClose').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/vSearchQuery').click()
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="검색")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="kr.co.ssg:id/etSearchQuery")
        el4.send_keys("티셔츠 "+"\n")
        self.driver.press_keycode(66)
        #el5 = self.driver.find_element(by=AppiumBy.ID, value="kr.co.ssg:id/tvKeyword")
        #el5.click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="브랜드 필터"]').click()
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/tvBadge').is_displayed(), "브랜드필터 인기 뱃지 확인 실패"
        # 바텀시트 브랜드 필터 인기 브랜드 뱃지 노출 확인


    def tearDown(self) -> None:
        if self.driver:
           self.driver.quit()

if __name__ == '__main__':
    unittest.main()



# from appium.options.android import UiAutomator2Options

# class TestAppium(unittest.TestCase):
#     def setUp(self) -> None:
#         options = UiAutomator2Options()
#         options.load_capabilities(capabilities)
#         self.driver = webdriver.Remote(appium_server_url, options=options)