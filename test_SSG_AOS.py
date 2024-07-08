import unittest
import pytest
import allure
from allure_commons.types import Severity
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from Common import Common
from appium.options.android import UiAutomator2Options
from selenium.common.exceptions import NoSuchElementException


capabilities = dict(
    platformName='Android',
    platformVersion='14',
    app="/Users/aquinas/Downloads/SSG.COM_3.5.6_Apkpure.apk",
    ensureWebviewsHavePages= True,
    nativeWebScreenshot= True,
    newCommandTimeout= 3600,
    connectHardwareKeyboard=True
)

appium_server_url="http://127.0.0.1:4723/wd/hub"

class TestAppium(unittest.TestCase):
    
    def setUp(self) -> None:
        options = UiAutomator2Options()
        options.load_capabilities(capabilities)
        self.driver = webdriver.Remote(appium_server_url, options=options)

    @allure.title("로그인")
    @allure.description("로그인 > MY SSG > 회원명 노출 확인(로그인 성공)")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.CRITICAL)
    def test_case_01(self) -> None:
        Common.Splash(self)
        Common.Login(self)
        assert self.driver.find_element(By.XPATH, '//android.view.View[@content-desc="김덕환 님"]').is_displayed(), "회원명 확인 실패"
        # 회원명 노출 확인(로그인 성공)

    @allure.title("유니버스 클럽 뱃지 노출")
    @allure.description("로그인 > MY SSG > 신세계 유니버스 클럽 뱃지 노출 확인(신세계 유니버스 클럽 회원)")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.NORMAL)
    def test_case_02(self) -> None:
        Common.Splash(self)
        Common.Login(self)
        assert self.driver.find_element(By.XPATH, '//android.view.View[@content-desc="신세계 유니버스 클럽 뱃지"]').is_displayed(), "신세계 유니버스 클럽 뱃지 노출 확인 실패"
        # 신세계 유버 클럽 뱃지 노출 확인

    @allure.title("신세계 유니버스 클럽 관리 페이지 랜딩")
    @allure.description("로그인 > MY SSG > 신세계 유니버스 클럽 뱃지 클릭 > 신세계 유니버스 클럽 관리 페이지 랜딩 확인")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.CRITICAL)
    def test_case_03(self) -> None:
        Common.Splash(self)
        Common.Login(self)
        self.driver.find_element(By.XPATH, '//android.view.View[@content-desc="신세계 유니버스 클럽 뱃지"]').click()
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/tvTitle').is_displayed(), "신세계 유니버스 클럽 관리 페이지 랜딩 확인 실패"
        # 신유클 관리 페이지 랜딩 확인

    @allure.title("회원 등급 뱃지 노출")
    @allure.description("로그인 > MY SSG > 회원 등급 뱃지 노출 확인(VIP 회원)")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.NORMAL)
    def test_case_04(self) -> None:
        Common.Splash(self)
        Common.Login(self)
        assert self.driver.find_element(By.XPATH, '//android.view.View[@content-desc="VIP 등급 뱃지"]').is_displayed(), "등급 뱃지 노출 확인 실패"
        # 회원 등급 뱃지 노출 확인

    @allure.title("유니버스 클럽 스탬프 페이지 랜딩")
    @allure.description("로그인 > MY SSG > 회원 등급 뱃지 클릭 > 유니버스 클럽 스탬프 페이지 랜딩 확인")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.CRITICAL)
    def test_case_05(self) -> None:
        Common.Splash(self)
        Common.Login(self)
        self.driver.find_element(By.XPATH, '//android.view.View[@content-desc="VIP 등급 뱃지"]').click()
        self.driver.implicitly_wait(2)
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/tvTitle').is_displayed(), "유니버스 클럽 스탬프 페이지 랜딩 실패"
        # 유니버스 클럽 스탬프 페이지 랜딩 확인

  
    @allure.title("멤버십 쿠폰 버튼 노출")
    @allure.description("로그인 > MY SSG > 멤버십 쿠폰 버튼 노출 확인(신유클 회원)")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.CRITICAL)
    def test_case_06(self) -> None:
        Common.Splash(self)
        Common.Login(self)
        assert self.driver.find_element(By.XPATH, '//android.view.View[@content-desc="멤버십쿠폰"]').is_displayed(), "멤버십쿠폰 노출 확인 실패"
        # 멤버십 쿠폰 버튼 노출 확인
        
    @allure.title("신세계 유니버스 클럽 전용 배경 노출")
    @allure.description("로그인 > MY SSG > 신유클 전용 배경 노출 확인(신유클 회원)")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.MINOR)
    def test_case_07(self) -> None:
        Common.Splash(self)
        Common.Login(self)
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/sdvBlurBackground2').is_displayed(), "신유클 배경 미노출"
        # 신유클 배경 노출 확인

    @allure.title("신세계 유니버스 클럽 공지사항 노출")
    @allure.description("로그인 > MY SSG > 신유클 공지사항 노출 확인(신유클 회원)")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.MINOR)
    def test_case_08(self) -> None:
        Common.Splash(self)
        Common.Login(self)
        self.driver.implicitly_wait(7)
        assert self.driver.find_element(By.XPATH, '//android.view.View[@content-desc="고객님께 1년동안 멤버십VIP 혜택이 유지됩니다."]').is_displayed(), "신유클 공지사항 미노출"
        # 신유클 공지사항 노출 확인

    @allure.title("신세계 유니버스 클럽 스탬프 페이지 랜딩")
    @allure.description("로그인 > MY SSG > 신유클 공지사항 클릭 > 유니버스 클럽 스탬프 페이지 랜딩 확인(신유클 회원)")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.CRITICAL)
    def test_case_09(self) -> None:
        Common.Splash(self)
        Common.Login(self)
        self.driver.find_element(By.XPATH, '//android.view.View[@content-desc="고객님께 1년동안 멤버십VIP 혜택이 유지됩니다."]').click()
        self.driver.implicitly_wait(3)
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/tvTitle').is_displayed(), "유니버스 클럽 스탬프 페이지 랜딩 실패"
        # 유니버스 클럽 스탬프 페이지 랜딩 확인

    @allure.title("나의 유니버스 클럽 혜택 메뉴 노출")
    @allure.description("로그인 > MY SSG > 페이지 하단 나의 유니버스 클럽 혜택 메뉴 노출 확인(신유클 회원)")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.CRITICAL)
    def test_case_10(self) -> None:
        Common.Splash(self)
        Common.Login(self)
        Common.scroll_to_bottom(self)
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='나의 유니버스 클럽 혜택').is_displayed()
        # MY SSG 페이지 하단 나의 유니버스 클럽 혜택 메뉴 노출 확인


    @allure.title("나의 신세계 유니버스 클럽 혜택 관리 페이지 랜딩")
    @allure.description("로그인 > MY SSG > 페이지 하단 나의 유니버스 클럽 혜택 메뉴 클릭 > 나의 신세계 유니버스 클럽 혜택 관리 페이지 랜딩 확인(신유클 회원)")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.CRITICAL)
    def test_case_11(self) -> None:
        Common.Splash(self)
        Common.Login(self)
        Common.scroll_to_bottom(self)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='나의 유니버스 클럽 혜택').click()
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/titlebar').is_displayed
        # MY SSG 페이지 하단 나의 유니버스 클럽 혜택 메뉴 클릭 시 나의 신세계 유니버스 클럽 혜택 확인 페이지 랜딩 확인

    @allure.title("연관검색어 노출")
    @allure.description("우유 검색 > 연관검색어 노출 확인")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.CRITICAL)
    def test_case_12(self) -> None:
        Common.Splash(self)
        Common.Search_Milk(self)
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/rvKeyword').is_displayed(), "연관검색어 로딩 실패"
        # 연관검색어 노출 확인

    @allure.title("연관검색어 검색 기능")
    @allure.description("우유 검색 > 연관검색어 클릭 > 연관검색어 검색 기능 확인")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.CRITICAL)
    def test_case_13(self) -> None:
        Common.Splash(self)
        Common.Search_Milk(self)
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/rvKeyword').is_displayed(), "연관검색어 로딩 실패"
        # 연관검색어 노출 확인

    @allure.title("배송유형필터 노출")
    @allure.description("우유 검색 > 배송유형필터 노출 확인")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.CRITICAL)
    def test_case_14(self) -> None:
        Common.Splash(self)
        Common.Search_Milk(self)
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/rvUpper').is_displayed(), "배송유형 로딩 실패"
        # 배송유형필터 노출 확인

    @allure.title("상품유형필터 노출")
    @allure.description("우유 검색 > 상품유형필터 노출 확인")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.CRITICAL)
    def test_case_15(self) -> None:
        Common.Splash(self)
        Common.Search_Milk(self)
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/rvLower').is_displayed(), "상품유형 로딩 실패"
        # 상품유형필터 노출 확인
        
    @allure.title("정렬필터 노출")
    @allure.description("우유 검색 > 정렬필터 노출 확인")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.CRITICAL)
    def test_case_16(self) -> None:
        Common.Splash(self)
        Common.Search_Milk(self)
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/btnSort').is_displayed(), "정렬필터 로딩 실패"
        # 정렬필터 노출 확인

    @allure.title("바텀시트 검색 필터 노출")
    @allure.description("우유 검색 > 바닥필터 클릭 > 바텀시트 검색 필터 노출 확인")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.CRITICAL)
    def test_case_17(self) -> None:
        Common.Splash(self)
        Common.Search_Milk(self)
        self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="가격 필터"]/android.widget.TextView').click()
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/lyTab').is_displayed(), "바텀시트 검색 필터 로딩 실패"
        # 바텀시트 검색 필터 노출 확인

    @allure.title("바텀시트 가격 필터 노출")
    @allure.description("우유 검색 > 바닥필터 클릭 > 바텀시트 가격 필터 노출 확인")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.NORMAL)
    def test_case_18(self) -> None:
        Common.Splash(self)
        Common.Search_Milk(self)
        self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="가격 필터"]/android.widget.TextView').click()
        # assert self.driver.find_element(By.ID, 'kr.co.ssg:id/lyTab').text("가격"), "가격 노출 실패"
        assert self.driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView').is_displayed(), "바텀시트 가격 필터 로딩 실패"
        # 바텀시트 가격 필터 노출 확인

    @allure.title("바텀시트 혜택 필터 노출")
    @allure.description("우유 검색 > 바닥필터 클릭 > 바텀시트 혜택 필터 노출 확인")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.NORMAL)
    def test_case_19(self) -> None:
        Common.Splash(self)
        Common.Search_Milk(self)
        self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="가격 필터"]/android.widget.TextView').click()
        assert self.driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView').is_displayed(), "바텀시트 혜택 필터 로딩 실패"
        # 바텀시트 혜택 필터 노출 확인

    @allure.title("바텀시트 카테고리 필터 노출")
    @allure.description("우유 검색 > 바닥필터 클릭 > 바텀시트 카테고리 필터 노출 확인")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.NORMAL)
    def test_case_20(self) -> None:
        Common.Splash(self)
        Common.Search_Milk(self)
        self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="가격 필터"]/android.widget.TextView').click()
        assert self.driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.TextView').is_displayed(), "바텀시트 카테고리 필터 로딩 실패"
        # 바텀시트 카테고리 필터 노출 확인
    
    @allure.title("바텀시트 배송유형 필터 노출")
    @allure.description("우유 검색 > 바닥필터 클릭 > 바텀시트 배송유형 필터 노출 확인")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.NORMAL)
    def test_case_21(self) -> None:
        Common.Splash(self)
        Common.Search_Milk(self)
        self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="가격 필터"]/android.widget.TextView').click()
        assert self.driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[4]/android.widget.TextView').is_displayed(), "바텀시트 배송유형 필터 로딩 실패"
        # 바텀시트 배송유형 필터 노출 확인
    
    @allure.title("바텀시트 상품유형 필터 노출")
    @allure.description("우유 검색 > 바닥필터 클릭 > 바텀시트 상품유형 필터 노출 확인")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.NORMAL)
    def test_case_22(self) -> None:
        Common.Splash(self)
        Common.Search_Milk(self)
        self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="가격 필터"]/android.widget.TextView').click()
        assert self.driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[5]/android.widget.TextView').is_displayed(), "바텀시트 상품유형 필터 로딩 실패"
        # 바텀시트 상품유형 필터 노출 확인


    @allure.title("바텀시트 브랜드 필터 노출")
    @allure.description("우유 검색 > 바닥필터 클릭 > 바텀시트 브랜드 필터 노출 확인")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.NORMAL)
    def test_case_23(self) -> None:
        Common.Splash(self)
        Common.Search_Milk(self)
        self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="가격 필터"]/android.widget.TextView').click()
        assert self.driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[6]/android.widget.TextView').is_displayed(), "바텀시트 브랜드 필터 로딩 실패"
        # 바텀시트 브랜드 필터 노출 확인

    @allure.title("최소금액 필터 노출")
    @allure.description("우유 검색 > 바닥필터 클릭 > 바텀시트 가격필터 > 최소금액 필터 노출 확인")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.NORMAL)
    def test_case_24(self) -> None:
        Common.Splash(self)
        Common.Search_Milk(self)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='가격 필터').click()
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='최소 금액 입력 란').is_displayed(), "바텀시트 최소금액 필터 로딩 실패"
        # 바텀시트 가격 필터 내 최소금액 필터 노출 확인

    @allure.title("추천카테고리 필터 노출")
    @allure.description("우유 검색 > 바닥필터 클릭 > 바텀시트 카테고리필터 > 추천카테고리 필터 노출 확인")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.NORMAL)
    def test_case_25(self) -> None:
        Common.Splash(self)
        Common.Search_Milk(self)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='카테고리 필터').click()
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/tvRecomCtg').is_displayed(), "카테고리 추천 필터 로딩 실패"
        # 바텀시트 카테고리 필터 내 추천 카테고리 필터 노출 확인

    @allure.title("검색 히스토리 노출")
    @allure.description("우유 검색 > 특징필터 클릭 > 바텀시트 필터 적용 > 히스토리 노출 확인")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.NORMAL)
    def test_case_26(self) -> None:
        Common.Splash(self)
        Common.Search_Milk(self)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='혜택 필터').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/cbArray').click()
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/rvHistory').is_displayed(), "검색필터 히스토리 확인 실패"
        # 검색 필터 적용 시 히스토리 노출 확인 

    @allure.title("바닥필터 실시간 적용")
    @allure.description("우유 검색 > 바텀시트 특징필터 적용 > 바닥필터 특징필터 활성화 확인")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.NORMAL)
    def test_case_27(self) -> None:
        Common.Splash(self)
        Common.Search_Milk(self)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='혜택 필터').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/cbArray').click()
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='혜택 필터').is_selected(), "배경 혜택 필터 활성화 확인 실패"
        # 바텀시트 특징 필터 적용 시 배경 특징 필터 활성화 확인 
    
    @allure.title("필터 적용")
    @allure.description("우유 검색 > 쓱배송 필터 클릭 > 쓱배송 필터 활성화 확인")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.NORMAL)
    def test_case_28(self) -> None:
        Common.Splash(self)
        Common.Search_Milk(self)
        self.driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="해제 상태 쓱배송 필터"]/android.widget.ImageView').click()
        assert self.driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="선택 상태 쓱배송 필터"]/android.widget.ImageView').is_selected(), "쓱배송 필터 활성화 확인 실패"
        # 쓱배송 필터 클릭시 활성화 확인

    @allure.title("바닥필터 활성화")
    @allure.description("우유 검색 > 쓱배송 필터 클릭 > 배송유형 바닥필터 활성화 확인")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.NORMAL)
    def test_case_29(self) -> None:
        Common.Splash(self)
        Common.Search_Milk(self)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='해제 상태 쓱배송 필터').click()
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='배송유형 필터').is_selected(), "쓱배송 필터 적용시 배송유형 바닥필터 노출 확인 실패"
        # 쓱배송 필터 클릭시 배송유형 바닥필터 활성화 확인

    @allure.title("필터 검색결과 실시간 반영")
    @allure.description("우유 검색 > 쓱배송 필터 클릭 > 쓱배송 상품 노출 확인(실시간 반영)")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.NORMAL)
    def test_case_30(self) -> None:
        Common.Splash(self)
        Common.Search_Milk(self)
        self.driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="해제 상태 쓱배송 필터"]/android.widget.ImageView').click()
        assert self.driver.find_element(By.XPATH, '(//android.widget.LinearLayout[@content-desc="쓱배송 안내 버튼"])[1]/android.widget.ImageView').is_displayed(), "쓱배송 필터 적용 확인 실패"
        # 쓱배송 필터 클릭시 쓱배송 상품 노출 확인

    @allure.title("선물포장 필터 노출")
    @allure.description("티셔츠 검색 > 선물포장 필터 노출 확인")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.NORMAL)
    def test_case_31(self) -> None:
        Common.Splash(self)
        Common.Search_Clothes(self)
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='해제 상태 선물포장 필터').is_displayed(), "의류 검색 결과 선물포장 필터 노출 확인 실패"
        # 의류 검색 시 선물포장 필터 노출 확인

    @allure.title("선물포장 필터 실시간 반영")
    @allure.description("티셔츠 검색 > 선물포장 필터 적용 > 선물포장 상품 노출 확인(실시간 반영)")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.NORMAL)
    def test_case_32(self) -> None:
        Common.Splash(self)
        Common.Search_Clothes(self)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='해제 상태 선물포장 필터').click()
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/rvTopMarkPm').is_displayed(), "선물포장 필터 적용 확인 실패"
        # 선물포장 필터 클릭시 선물포장 상품 노출 확인

    @allure.title("스타일 필터 노출")
    @allure.description("티셔츠 검색 > 스타일 필터 노출 확인")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.NORMAL)
    def test_case_33(self) -> None:
        Common.Splash(self)
        Common.Search_Clothes(self)
        assert self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="스타일 필터"]').is_displayed(), "의류 검색 시 스타일 필터 노출 확인 실패"
        # 의류 검색시 스타일 필터 노출 확인

    @allure.title("바텀시트 스타일 필터 노출")
    @allure.description("티셔츠 검색 > 스타일 필터 클릭 > 바텀시트 스타일 필터 노출 확인")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.NORMAL)
    def test_case_34(self) -> None:
        Common.Splash(self)
        Common.Search_Clothes(self)
        self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="스타일 필터"]').click()
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/vpContent').is_displayed(), "바닥필터 스타일 필터 클릭 시 바텀시트 스타일 필터 노출 확인 실패"
        # 바닥필터 스타일 필터 클릭 시 바텀시트 스타일 필터 노출 확인

    @allure.title("정렬필터 노출")
    @allure.description("티셔츠 검색 > 검색결과 페이지 정렬필터 노출 확인")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.NORMAL)
    def test_case_35(self) -> None:
        Common.Splash(self)
        Common.Search_Clothes(self)
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/btnSort').is_displayed(), "정렬필터 확인 실패"
        # 검색결과 페이지에 정렬필터 노출 확인

    @allure.title("바텀시트 정렬필터 노출")
    @allure.description("티셔츠 검색 > 검색결과 페이지 정렬필터 클릭 > 바텀시트 정렬필터 노출 확인")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.NORMAL)
    def test_case_36(self) -> None:
        Common.Splash(self)
        Common.Search_Clothes(self)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnSort').click()
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/rvList').is_displayed(), "바텀시트 정렬필터 확인 실패"
        # 검색결과 페이지의 정렬필터 클릭 시, 바텀시트 정렬필터 노출 확인

    @allure.title("추천순 필터 안내 아이콘 노출")
    @allure.description("티셔츠 검색 > 검색결과 페이지 정렬필터 클릭 > 바텀시트 정렬필터에 추천순 필터 안내 아이콘 노출 확인")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.MINOR)
    def test_case_37(self) -> None:
        Common.Splash(self)
        Common.Search_Clothes(self)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnSort').click()
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/bcInfo').is_displayed(), "바텀시트 추천순 정렬 안내 아이콘 확인 실패"
        # 바텀시트 정렬필터에 추천순 필터 안내 아이콘 노출 확인

    @allure.title("추천순 필터 안내 팝업 노출")
    @allure.description("티셔츠 검색 > 검색결과 페이지 정렬필터 클릭 > 바텀시트 정렬필터의 추천순 필터 안내 아이콘 클릭 > 안내 메시지 팝업 노출 확인")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.MINOR)
    def test_case_38(self) -> None:
        Common.Splash(self)
        Common.Search_Clothes(self)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnSort').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcInfo').click()
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/tvMessage').is_displayed(), "추천순 안내 메시지 확인 실패"
        # 바텀시트 정렬필터에 추천순 필터 안내 아이콘 클릭 시 안내 메시지 팝업 노출 확인

    @allure.title("추천순 필터 안내 팝업 내 확인버튼 노출")
    @allure.description("티셔츠 검색 > 검색결과 페이지 정렬필터 클릭 > 바텀시트 정렬필터의 추천순 필터 안내 아이콘 클릭 > 안내 메시지 팝업 내 확인 버튼 노출확인")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.MINOR)
    def test_case_39(self) -> None:
        Common.Splash(self)
        Common.Search_Clothes(self)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnSort').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcInfo').click()
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/btnPositive').is_displayed, "추천순 안내팝업 확인버튼 확인 실패"
        # 추천순 안내 메시지 팝업 내 확인 버튼 노출 확인

    @allure.title("추천순 필터 안내 팝업 내 확인버튼 동작")
    @allure.description("티셔츠 검색 > 검색결과 페이지 정렬필터 클릭 > 바텀시트 정렬필터의 추천순 필터 안내 아이콘 클릭 > 안내 메시지 팝업 내 확인 버튼 클릭 > 팝업 닫힘 동작 확인")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.NORMAL)
    def test_case_40(self) -> None:
        Common.Splash(self)
        Common.Search_Clothes(self)
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnSort').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/bcInfo').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/btnPositive').click()
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/bcInfo').is_enabled, "추천순 안내팝업 확인버튼 닫기 동작 확인 실패"
        # 추천순 안내 메시지 팝업 내 확인 버튼 클릭 시 팝업 닫힘 동작 확인


    @allure.title("추천 카테고리 클릭 시 카테고리 자동 선택")
    @allure.description("우유 검색 > 카테고리 필터 클릭 > 바텀시트 추천 카테고리 클릭 > 카테고리 자동 선택 확인")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.NORMAL)
    def test_case_41(self) -> None:
        Common.Splash(self)
        Common.Search_Milk(self)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='카테고리 필터').click()
        self.driver.find_element(By.ID, 'kr.co.ssg:id/tvRecomCtg').click()
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/cbArray').is_selected(), "추천카테고리 클릭 동작 확인 실패"
        # 바텀시트 추천 카테고리 클릭 시 자동 선택 확인

    @allure.title("인기 브랜드 뱃지 노출")
    @allure.description("티셔츠 검색 > 브랜드 필터 클릭 > 바텀시트 브랜드 필터 내 인기 브랜드 뱃지 노출 확인")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.MINOR)
    def test_case_42(self) -> None:
        Common.Splash(self)
        Common.Search_Clothes(self)
        self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="브랜드 필터"]').click()
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/tvBadge').is_displayed(), "브랜드필터 인기 뱃지 확인 실패"
        # 바텀시트 브랜드 필터 인기 브랜드 뱃지 노출 확인

    @allure.title("배송유형 필터 앵커링 동작")
    @allure.description("우유 검색 > 스크롤 다운 > 배송유형 필터 앵커링 동작 확인")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.NORMAL)
    def test_case_43(self) -> None:
        Common.Splash(self)
        Common.Search_Milk(self)
        Common.scroll_to_bottom_search(self)
        
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="해제 상태 쓱배송 필터")
        assert el3.is_displayed(), "쓱배송 필터 노출 확인 실패"
        # 스크롤 다운 후 배송유형 필터 앵커링 확인 
    
    @allure.title("필터 앵커링 동작")
    @allure.description("우유 검색 > 스크롤 다운 > 바닥 필터 앵커링 동작 확인")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.NORMAL)
    def test_case_44(self) -> None:
        Common.Splash(self)
        Common.Search_Milk(self)
        Common.scroll_to_bottom_search(self)
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="특징 필터")
        assert el3.is_displayed(), "바닥 필터 노출 확인 실패"
        # 스크롤 다운 후 바탁필터 앵커링 확인 

    @allure.title("필터 앵커링+활성화 동작")
    @allure.description("우유 검색 > 스크롤 다운 > 쓱배송 필터 클릭 > 쓱배송 필터 활성화 확인")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.NORMAL)
    def test_case_45(self) -> None:
        Common.Splash(self)
        Common.Search_Milk(self)
        Common.scroll_to_bottom_search(self)
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="해제 상태 쓱배송 필터")
        el3.click()
        assert el3.is_selected(), "쓱배송 필터 활성화 확인 실패"
        # 스크롤 다운 후 쓱배송 필터 클릭 시 활성화 확인 

    @allure.title("필터 앵커링+활성화 동작")
    @allure.description("우유 검색 > 스크롤 다운 > 쓱배송 필터 클릭 > 배송유형 필터 활성화 확인")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.NORMAL)
    def test_case_46(self) -> None:
        Common.Splash(self)
        Common.Search_Milk(self)
        Common.scroll_to_bottom_search(self)
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="해제 상태 쓱배송 필터")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="배송유형 필터")
        assert el4.is_selected(), "배송유형 필터 활성화 확인 실패"
        # 스크롤 다운 후 쓱배송 필터 클릭 시 배송유형 필터 활성화 확인

    @allure.title("필터 앵커링+최상단 이동 동작")
    @allure.description("우유 검색 > 스크롤 다운 > 쓱배송 필터 클릭 > 검색결과 화면 최상단으로 이동 확인")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.NORMAL)
    def test_case_47(self) -> None:
        Common.Splash(self)
        Common.Search_Milk(self)
        Common.scroll_to_bottom_search(self)
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="해제 상태 쓱배송 필터")
        el3.click()
        assert self.driver.find_element(By.XPATH, '(//android.widget.Button[@content-desc="좋아요"])[1]').is_displayed(), "검색결과 최상단 이동 확인 실패"
        # 스크롤 다운 후 쓱배송 필터 클릭 시 검색결과 최상단으로 이동 확인

    @allure.title("필터 앵커링+필터 적용 동작")
    @allure.description("우유 검색 > 스크롤 다운 > 쓱배송 필터 클릭 > 필터 적용(쓱배송 상품 노출) 확인")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.NORMAL)
    def test_case_48(self) -> None:
        Common.Splash(self)
        Common.Search_Milk(self)
        Common.scroll_to_bottom_search(self)
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="해제 상태 쓱배송 필터")
        el3.click()
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/pvDeliveryAndMallInfo').is_displayed(), "쓱배송 필터 적용 확인 실패"
        # 스크롤 다운 후 쓱배송 필터 클릭 시 필터 적용(쓱배송 상품 노출) 확인

    @allure.title("필터 앵커링+바텀레이어 팝업 노출")
    @allure.description("우유 검색 > 스크롤 다운 > 바닥 필터 클릭 > 바텀레이어 팝업 노출 확인")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.NORMAL)
    def test_case_49(self) -> None:
        Common.Splash(self)
        Common.Search_Milk(self)
        Common.scroll_to_bottom_search(self)
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="배송유형 필터")
        el3.click()
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/tvTitle').is_displayed(), "바텀레이어 팝업 노출 확인 실패"
        # 스크롤 다운 후 바닥필터 클릭 시 바텀레이어 팝업 노출 확인     

    @allure.title("가격필터 8자리 초과 입력")
    @allure.description("우유 검색 > 바텀레이어 가격 필터 > 직접입력 8자리 이상 입력 > 알럿 노출 확인")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.NORMAL)
    def test_case_50(self) -> None:
        Common.Splash(self)
        Common.Search_Milk(self)
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="가격 필터").click()
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="최소 금액 입력 란").click()
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="최소 금액 입력 란").send_keys('123123123')
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/lyContentPanel').is_displayed()

    @allure.title("가격필터 최소금액>최대금액 입력")
    @allure.description("우유 검색 > 바텀레이어 가격 필터 > 최소금액을 최대금액보다 높게 입력 > 알럿 노출 확인")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.NORMAL)
    def test_case_51(self) -> None:
        Common.Splash(self)
        Common.Search_Milk(self)
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="가격 필터").click()
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="최소 금액 입력 란").click()
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="최소 금액 입력 란").send_keys('10000')
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="최대 금액 입력 란").click()
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="최대 금액 입력 란").send_keys('1000')
        self.driver.press_keycode(66)
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/lyContentPanel').is_displayed()

    @allure.title("가격필터 직접입력 시 히스토리 동작")
    @allure.description("우유 검색 > 바텀레이어 가격 필터 > 금액 직접 입력 > 히스토리바 적용 확인")
    @allure.tag("SSG몰", "Android")
    @allure.severity(Severity.NORMAL)
    def test_case_52(self) -> None:
        Common.Splash(self)
        Common.Search_Milk(self)
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="가격 필터").click()
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="최소 금액 입력 란").click()
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="최소 금액 입력 란").send_keys('1000')
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="최대 금액 입력 란").click()
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="최대 금액 입력 란").send_keys('10000')
        self.driver.press_keycode(66)
        assert self.driver.find_element(By.ID, 'kr.co.ssg:id/rvHistory').is_displayed()



    def tearDown(self) -> None:
        if self.driver:
           self.driver.quit()

if __name__ == '__main__':
    unittest.main()
