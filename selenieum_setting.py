from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

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