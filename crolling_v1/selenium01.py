from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "다운받은 크롬 드라이버의 경로를 넣어주세요"
naver_url = "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"
naver_id = "아이디"
naver_pw = "비번"

browser = webdriver.Chrome()
browser.get(naver_url)  # 네이버 메인 화면 띄우기

#browser.find_element(By.CSS_SELECTOR, "#account > div > a > i").click()  # "NAVER 로그인" 버튼 클릭해서 로그인 화면으로 넘어가기

browser.execute_script(f"document.getElementsByName('id')[0].value='{naver_id}'")  # id 입력
browser.execute_script(f"document.getElementsByName('pw')[0].value='{naver_pw}'")  # pw 입력

browser.find_element(By.CSS_SELECTOR ,"#log\.login").click()  # "로그인" 버튼 클릭해서 최종 로그인