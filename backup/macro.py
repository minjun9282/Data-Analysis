ex_list = [' 방이동 해동아파트(134-5)', ' 구로동 (744-12)', ' 묵동 헤르만스테이트', ' 호평동 호평두산위브파크']

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver = webdriver.Chrome('C:/Users/오민준/Desktop/chromedriver.exe')
driver.get("https://land.naver.com/")

search_box = driver.find_element_by_id("queryInputHeader")
search_box.send_keys("타워팰리스 1차")
driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/div[1]/div/fieldset/a[1]').click()
driver.find_element_by_xpath('//*[@id="ct"]/div[2]/div[1]/div[2]/div/div/div[1]/div/a/div[1]').click()
driver.find_element_by_xpath('//*[@id="summaryInfo"]/div[2]/div[2]/button[3]').click()

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')
SD_info = soup.select('#detailContents5 > div > div.detail_box--school > div.heading')
print(SD_info)