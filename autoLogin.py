from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

import time
import pyautogui
import pyperclip

chrome_option = Options()

# 브라우저 꺼짐 방지
chrome_option.add_experimental_option("detach", True)
# 불필요한 에러 메시지 제거
chrome_option.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_option)

#페이지 로딩 대기시간
driver.implicitly_wait(5)
#페이지 풀스크린
driver.maximize_window()

driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/")

id = driver.find_element(By.CSS_SELECTOR, "#id")
id.click()
pyperclip.copy("")
pyautogui.hotkey("ctrl", "v")
time.sleep(2)

pw = driver.find_element(By.CSS_SELECTOR, "#pw")
pw.click()
pyperclip.copy("")
pyautogui.hotkey("ctrl", "v")
time.sleep(2)

loginBtn = driver.find_element(By.CSS_SELECTOR, "#log\.login")
loginBtn.click()