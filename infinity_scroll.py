from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


import time

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager


chrome_option = Options()

# 브라우저 꺼짐 방지
chrome_option.add_experimental_option("detach", True)
# 불필요한 에러 메시지 제거
chrome_option.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_option)

driver.get("https://www.naver.com")
driver.implicitly_wait(5)
driver.maximize_window()


shopping = driver.find_element(By.CSS_SELECTOR, "#shortcutArea > ul > li:nth-child(4) > a")
shopping.click()
time.sleep(3)

# 새로운 창 바라보기
new_window = driver.window_handles[1]
driver.switch_to.window(new_window)

searchInput = driver.find_element(By.CSS_SELECTOR, "#gnb-gnb > div._gnb_header_area_150KE > div > div._gnbLogo_gnb_logo_3eIAf > div > div._gnbSearch_gnb_search_3O1L2 > form > div._gnbSearch_inner_2Zksb > div > input")
searchInput.click()
searchInput.send_keys("아이폰15")
searchInput.send_keys(Keys.ENTER)

# 스크롤 전 높이 확인하기
beforeHight = driver.execute_script("return window.scrollY")

#최하단으로 스크롤 내리기
while True:
    driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)

    time.sleep(1)

    afterHight = driver.execute_script("return window.scrollY")

    if afterHight == beforeHight:
        break
    
    beforeHight = afterHight

productList = driver.find_elements(By.CSS_SELECTOR, ".product_info_area__xxCTi")

for item in productList:
    name = item.find_element(By.CSS_SELECTOR, ".product_title__Mmw2K").text
    try:
        price = item.find_element(By.CSS_SELECTOR, ".price_num__S2p_v").text
    except:
        price = "판매중단"
    link = item.find_element(By.CSS_SELECTOR, ".product_title__Mmw2K > a").get_attribute("href")

    print(name, price, link)