from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import re

SCROLL_PAUSE_SEC = 5
url = "https://www.youtube.com/watch?v=YD-6XxJwh0M&t=5s"

path = "C:/Users/JuHyeon Park/Desktop/chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get(url)

for _ in range(5):
    driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

time.sleep(2)
playlist_html = driver.find_element_by_id("content-text").get_attribute('innerHTML')

soup = BeautifulSoup(playlist_html, 'html.parser')
spans = soup.find_all("span")
playlist = []

for span in spans:
    if "-" in span.text:
        temp = span.text
        re.sub("([\(\[]).*?([\)\]])", "\g<1>\g<2>", temp)
        playlist.append(temp.replace('(','').replace(')','').replace('[','').replace(']',''))
print(playlist)