from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import platform
import time
import json


def setup_driver():
    """
    Chrome WebDriver 설정
    """
    chrome_options = Options()
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--lang=ko_KR')
    
    # M1/M2 Mac 확인 및 설정
    if platform.system() == 'Darwin' and platform.processor() == 'arm':
        driver_path = ChromeDriverManager().install()
        import os
        os.chmod(driver_path, 0o755)
        service = Service(driver_path)
    else:
        service = Service(ChromeDriverManager().install())
    
    return webdriver.Chrome(service=service, options=chrome_options)

def close_popup_if_present(driver):
    """
    팝업이 존재할 경우 닫기 버튼을 클릭하는 함수
    팝업의 locator는 실제 팝업의 HTML 구조에 맞게 수정해야 합니다.
    """
    try:
        # 팝업 닫기 버튼을 찾는다. (예시: 클래스명이 popup-close 인 요소)
        wait = WebDriverWait(driver, 5)
        popup_close_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="commonNoticeDialog"]/div/div[3]/a[1]/span'))
        )
        popup_close_button.click()
        print("팝업 닫기 완료")
    except TimeoutException:
        # 팝업이 나타나지 않은 경우 TimeoutException 발생 → 그냥 넘어감
        print("팝업 없음")
    except Exception as e:
        print(f"팝업 닫기 처리 중 오류 발생: {e}")

def save_order_number(ordNo):
    """주문번호를 JSON 파일에 저장"""
    with open("order_data.json", "w") as f:
        json.dump({"ordNo": ordNo}, f)

def Front():
    """
    SSG 로그인 자동화 (엔터키 사용)
    """
    try:
        # WebDriver 초기화
        driver = setup_driver()
        print("브라우저 실행 완료")
        
        # 페이지 로드 타임아웃 설정
        driver.set_page_load_timeout(30)
        driver.implicitly_wait(10)
        
        # SSG QA 사이트 접속
        url = "https://qa-www.ssg.com"
        driver.get(url)
        print("사이트 접속 완료")

        close_popup_if_present(driver)
        
        # 로그인 버튼 클릭
        wait = WebDriverWait(driver, 10)
        login_button = wait.until(
            EC.element_to_be_clickable((By.ID, "loginBtn"))
        )
        login_button.click()
        print("초기 로그인 버튼 클릭 완료")
        
        # 창 전환 처리
        wait.until(lambda x: len(x.window_handles) > 1)
        windows = driver.window_handles
        driver.switch_to.window(windows[-1])  # 새로 열린 창으로 전환
        print("로그인 창으로 전환 완료")
        
        # 아이디 입력
        id_field = wait.until(
            EC.presence_of_element_located((By.ID, "mem_id"))
        )
        id_field.clear()
        id_field.send_keys("cddbag")
        print("아이디 입력 완료")
        
        # 비밀번호 입력 후 엔터
        pw_field = wait.until(
            EC.presence_of_element_located((By.ID, "mem_pw"))
        )
        pw_field.clear()
        pw_field.send_keys("Qa1324!@#")
        pw_field.send_keys(Keys.RETURN)  # 엔터키 입력
        print("비밀번호 입력 및 엔터키 입력 완료")
        
        # 로그인 완료 대기
        time.sleep(3)

        #wait.until(lambda x: len(x.window_handles) > 1)
        windows = driver.window_handles
        driver.switch_to.window(windows[0])  # 새로 열린 창으로 전환
        print("로그인 창으로 전환 완료")
        
        url = "https://qa-www.ssg.com/item/itemView.ssg?itemId=0000008333613&siteNo=6001&salestrNo=2087"
        driver.get(url)
        print("상품 페이지 접속 완료")
        wait = WebDriverWait(driver, 10)
        Payment_button = wait.until(
            EC.element_to_be_clickable((By.ID, "actionPayment"))
        )
        Payment_button.click()
        print("바로구매 버튼 클릭 완료")

        #Table_select1 = wait.until(
        #    EC.element_to_be_clickable((By.XPATH, '//*[@id="div_multi_section_1"]/div[1]/div[2]/div/div[4]/table/tbody/tr[2]/td[1]/span/label'))
        #    timeout=2 
        #)
        #Table_select1.click()
        #print("타임테이블 첫 배송일 1차 선택 완료")
        
        
        #elements = wait.until(
        #    EC.element_to_be_clickable((By.XPATH, "//*[Text()='예약가능']")))
        #if len(elements) > 1:
        #    elements[1].click()
        #    print("타임테이블 가장 빠른 차수 클릭 완료")
        #else:
        #    PurchaseAdd = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="div_multi_section_1"]/div[1]/div[2]/div/div[4]/table/tbody/tr[2]/td[1]/div/span/label')))
        #    PurchaseAdd.click()
        #    print("주문더하기 클릭 완료")
        xpaths = [
            '//*[@id="div_multi_section_1"]/div[1]/div[2]/div[1]/div[4]/table/tbody/tr[3]/td[1]/span',
            '//*[@id="div_multi_section_1"]/div[1]/div[2]/div[1]/div[4]/table/tbody/tr[3]/td[1]/span/label',
            '//*[@id="div_multi_section_1"]/div[1]/div[2]/div[1]/div[4]/table/tbody/tr[4]/td[1]/span',
            '//*[@id="div_multi_section_1"]/div[1]/div[2]/div[1]/div[4]/table/tbody/tr[4]/td[1]/span/label',
            '//*[@id="div_multi_section_1"]/div[1]/div[2]/div[1]/div[4]/table/tbody/tr[5]/td[1]/span',
            '//*[@id="div_multi_section_1"]/div[1]/div[2]/div[1]/div[4]/table/tbody/tr[5]/td[1]/span/label',
            '//*[@id="div_multi_section_1"]/div[1]/div[2]/div[1]/div[4]/table/tbody/tr[6]/td[1]/span',
            '//*[@id="div_multi_section_1"]/div[1]/div[2]/div[1]/div[4]/table/tbody/tr[6]/td[1]/span/label'
        ]

        is_clicked = False
        for xpath in xpaths:
            try:
                element = driver.find_element(By.XPATH, xpath)
                if element.text == "예약가능":
                    element.click()
                    print(f"'{xpath}' 경로의 '예약가능' 요소를 클릭했습니다.")
                    is_clicked = True
                    break
            except Exception as e:
                print(f"'{xpath}' 경로 검색 중 오류 발생: {e}")
                continue  # 이 XPath에서 오류가 발생해도 다음 XPath로 계속 진행

        if not is_clicked:
            print("모든 XPath를 시도했지만 '예약가능' 요소를 찾거나 클릭하지 못했습니다.")

        saveShppInfo = wait.until(
            EC.element_to_be_clickable((By.ID, "saveShppInfo"))
        )
        saveShppInfo.click()
        print("계속하기 선택 완료")

        #SsgMoneyUse = wait.until(
        #    EC.element_to_be_clickable((By.NAME, "btSsgMoneyUseAll"))
        #)
        #SsgMoneyUse.click()
        #print("쓱머니 전체사용 선택 완료")

        if len(driver.find_elements(By.NAME, "btSsgMoneyUseAll")) > 0:
            SsgMoneyUse = wait.until(EC.element_to_be_clickable((By.NAME, "btSsgMoneyUseAll")))
            SsgMoneyUse.click()
            print("쓱머니 전체사용 클릭 완료")
        else:
            AddSsgMoney = wait.until(EC.element_to_be_clickable((By.NAME, "btnUseAllSubPay")))
            AddSsgMoney.click()
            print("주문더하기 쓱머니 사용 클릭 완료")
        
        #Pay = wait.until(
        #    EC.element_to_be_clickable((By.NAME, "processOrderButton"))
        #)
        #Pay.click()
        #print("결제하기 선택 완료")
            
        if len(driver.find_elements(By.NAME, "processOrderButton")) > 0:
            Pay = wait.until(EC.element_to_be_clickable((By.NAME, "processOrderButton")))
            Pay.click()
            print("결제하기 클릭 완료")
        else:
            AddPay = wait.until(EC.element_to_be_clickable((By.NAME, "btnAddOrdProcess")))
            AddPay.click()
            print("주문더하기 결제 클릭 완료")
            time.sleep(3)
        
        #PurchaseComplete = wait.until(
        #    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "고객님 주문이 완료되었습니다."))
        #)
        global ordNo    
        PurchaseComplete = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "codr_top_odrinfo"))
        )
        PurchaseComplete
        print("결제 완료")
        
        order_info_text = PurchaseComplete.text
        print("주문정보:", order_info_text)

        # "주문번호는" 이후의 텍스트 추출
        import re
        match = re.search(r"주문번호는\s*([0-9a-zA-Z]+)", order_info_text)

        if match:
            ordNo = match.group(1)  # 주문번호 추출
            print("주문번호(ordNo):", ordNo)

            # 📌 주문번호 저장 추가 
            save_order_number(ordNo)  

        else:
            print("주문번호를 찾을 수 없습니다.")
        
    except Exception as e:
        print(f"오류 발생: {str(e)}")

    
    finally:
        # 브라우저 종료
        driver.quit()
        print("브라우저 종료 완료")

if __name__ == "__main__":
    Front()
    