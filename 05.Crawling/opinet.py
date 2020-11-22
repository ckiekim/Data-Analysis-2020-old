import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
driver.get("http://www.opinet.co.kr/user/main/mainView.do")
time.sleep(2)

driver.find_element_by_css_selector('.ic_m1').click()

''' html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
gu_selector = soup.select_one('#SIGUNGU_NM0')
gu_list = gu_selector.find_all('option') '''
xpath = driver.find_element_by_xpath('//*[@id="SIGUNGU_NM0"]')
gu_list = xpath.find_elements_by_tag_name('option')
gu_names = [option.get_attribute('value') for option in gu_list]
print(gu_names)
del gu_names[0]

''' element = driver.find_element_by_css_selector('#SIGUNGU_NM0')
element.send_keys(gu_names[0])

xpath = driver.find_element_by_xpath('//*[@id="glopopd_excel"]/span')
xpath.click() '''

for gu in gu_names:
    element = driver.find_element_by_css_selector('#SIGUNGU_NM0')
    element.send_keys(gu)
    time.sleep(1)

    xpath = driver.find_element_by_xpath('//*[@id="glopopd_excel"]/span')
    xpath.click()
    time.sleep(1)