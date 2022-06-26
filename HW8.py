"""
Создать тест в котором происходит инициализация драйвера.
Перейдите на любой выбранный вами ресурс. Нажмите на копку либо введите текст в поле ввода.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from time import sleep

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
MAIN_URL = "https://incompetech.com/wordpress/"

try:
    requests.get(MAIN_URL, timeout=3).raise_for_status()
except requests.exceptions.HTTPError as errh:
    print("Http Error:", errh)
except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)
except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    print("OOps: Something Else", err)
else:
    driver.get(MAIN_URL)
    sleep(2)
    search_field = '//*[@id="s"]'
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, search_field)))
    element = driver.find_element(By.XPATH, search_field)
    element.clear() # just in case
    element.send_keys("baba yaga")
    element.send_keys(Keys.ENTER) # using ENTER
    sleep(2)
    try:
        baba_yaga_link = '//*[@id="post-1569"]/h2/a'
        driver.find_element(By.XPATH, baba_yaga_link)
    except NoSuchElementException:
        print("The link is absent!")
    else:
        print("The link is here. It is fine")
finally:
    driver.close()
    driver.quit()

