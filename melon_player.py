import traceback
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from main import playlist

driver = webdriver.Chrome('C:/Users/JuHyeon Park/Desktop/chromedriver.exe')
driver.implicitly_wait(2)
driver.get('https://www.melon.com/index.htm')

driver.find_element_by_xpath('//*[@id="gnbLoginDiv"]/div/button/span').click()
driver.find_element_by_xpath('//*[@id="conts_section"]/div/div/div[3]/button').click()

driver.find_element_by_xpath('//*[@id="id"]').send_keys('bghtht')
driver.find_element_by_xpath('//*[@id="pwd"]').send_keys('jh9229')

driver.find_element_by_xpath('//*[@id="btnLogin"]').click()


# 메인 검색 창과 검색 결과 화면의 검색창 element id 가 달라, 아래 루프에서는 검색 결과 화면이 검색창 element id로 통일시키기 위해 임의 검색을 한번 수행
driver.find_element_by_id('top_search').send_keys('oboki')
driver.find_element_by_xpath('//*[@id="gnb"]/fieldset/button[2]/span').click()

# Loop
for p in playlist:
    try:
        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) == 1)
        driver.switch_to.window(driver.window_handles[0])

        p = p.split('\n')[0]

        driver.find_element_by_id('top_search').clear()
        driver.find_element_by_id('top_search').send_keys(p)
        driver.find_element_by_xpath('//*[@id="header_wrap"]/div[3]/fieldset/button[2]/span').click()

        driver.find_element_by_xpath('//*[@id="divCollection"]/ul/li[3]/a').click()
        driver.find_element_by_xpath('//*[@id="frm_defaultList"]/div/table/tbody/tr[1]/td[3]/div/div/button[2]/span').click()

        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) == 2)
        driver.switch_to.window(driver.window_handles[1])

        tmp = driver.window_handles[1]

        driver.find_element_by_xpath('//*[@id="plylstList"]/div/table/tbody/tr/td[1]/div/div/span').click()
        driver.find_element_by_xpath('//*[@id="plylstList"]/div/table/tbody/tr/td[1]/div/span/button/span/span').click()

        try:
            alert = Alert(driver)
            alert_text = alert.text
            alert.accept()
            driver.close()
            print(alert_text)
        except NoAlertPresentException:
            while True:
                if len(driver.window_handles) > 1:
                    if (tmp != driver.window_handles[1]):
                        break

            WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) == 2)
            driver.switch_to.window(driver.window_handles[1])
            driver.find_element_by_xpath('/html/body/div/div/div[2]/button/span/span').click()

    except NoSuchElementException:
        print("Error: "+p)
        traceback.print_exc()
        continue
    except IndexError:
        print("Error: "+p)
        traceback.print_exc()
        continue

driver.close()
