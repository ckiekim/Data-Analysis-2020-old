import time
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('./chromedriver')
# 웹드라이버 실행 경로 chromedriver는 폴더가 아니라 파일명입니다.
driver.get('http://www.google.com/');   	# 구글에 접속
time.sleep(2)				# 2초간 동작하는 걸 봅시다
search_box = driver.find_element_by_name('q')   # element name이 q인 곳을 찾아
search_box.send_keys('ChromeDriver')	# 키워드를 입력하고
search_box.submit()			# 실행합니다.
time.sleep(2)				# 2초간 동작하는 걸 봅시다

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
search_result = soup.select_one('#search')
results = search_result.select('.g')
h3 = results[1].find('h3')
print(h3.get_text())
span = results[1].select_one('.aCOpRe')
print(span.get_text())

sr = driver.find_element_by_css_selector('#search')
results = sr.find_elements_by_css_selector('.g')
print(len(results))

#driver.quit()