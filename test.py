from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import re


def prettifier(str):
    korean_pattern = "[가-힣]+"
    if re.search(korean_pattern, str):
        return re.sub("[a-zA-Z]", '', str).replace('(','').replace(')','').replace('[','').replace(']','').replace(' ', '')
    else:
        return str

# if dont have youtube premium service

SCROLL_PAUSE_SEC = 5
url = input('enter the youtube url: ')

path = "./chromedriver"
driver = webdriver.Chrome(path)
driver.get(url)

time.sleep(5) # need to be modified with explicit wait function

driver.find_element_by_class_name('style-scope ytd-expander').find_element_by_id('more').send_keys(Keys.ENTER)

temp_list = driver.find_element_by_class_name('style-scope ytd-metadata-row-container-renderer').get_attribute('innerHTML')

driver.close()

soup = BeautifulSoup(temp_list, 'html.parser')
temp_list = soup.find_all(["yt-formatted-string"])

song = ''
artist = ''
playlist = []
for idx, elem in enumerate(temp_list):
    if elem.text == "노래":
        song = prettifier(temp_list[idx + 1].text)
    elif elem.text == "아티스트":
        artist = prettifier(temp_list[idx + 1].text)
        playlist.append((song, artist))

print(playlist)

'''
playlist = []

while song_idx < len(temp_list):
    song = prettifier(temp_list[song_idx].text)
    artist = prettifier(temp_list[artist_idx].text)

    playlist.append((song, artist))
    song_idx += interval
    artist_idx += interval

print(playlist)
'''





