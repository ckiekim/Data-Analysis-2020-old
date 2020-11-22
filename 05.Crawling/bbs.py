import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
driver.get("http://61.35.152.103:3000/login")
driver.find_element_by_id('uid').send_keys("djy")
driver.find_element_by_css_selector('#pwd').send_keys("1234")
driver.find_element_by_class_name('btn.btn-primary').click()
''' inputs = driver.find_elements_by_tag_name('input')
inputs[0].send_keys("djy")
inputs[1].send_keys("1234")
inputs[2].click() '''
time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
paging = soup.select_one('.pagination')
lis = paging.find_all('li')
total_pages = len(lis) - 2

bids = []; titles = []; names = []
times = []; view_counts = []; reply_counts = []

for page in range(1, total_pages):
    trs = soup.find_all('tr')
    for tr in trs[1:]:
        tds = tr.find_all('td')
        span = tds[1].find('span')
        reply_count = span.string[1:-1] if span else '0'
        index = tds[1].get_text().find('[')
        title = tds[1].get_text()[:index] if span else tds[1].get_text()
        bids.append(tds[0].string)
        titles.append(title)
        names.append(tds[2].string)
        times.append(tds[3].string)
        view_counts.append(tds[4].string)
        reply_counts.append(reply_count)

    page_element = driver.find_element_by_css_selector('.pagination')
    lis = page_element.find_elements_by_tag_name('li')
    lis[page+1].click()
    time.sleep(1)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

print(titles)

#driver.close()
