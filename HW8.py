"""
Создать тест в котором происходит инициализация драйвера.
Перейдите на любой выбранный вами ресурс. Нажмите на копку либо введите текст в поле ввода.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try :
    driver.get("https://incompetech.com/wordpress/")
    sleep(1)
    search_field = '//*[@id="s"]'
    element = driver.find_element(By.XPATH, search_field)
    element.clear() # just in case
    element.send_keys("baba yaga")
    element.send_keys(Keys.ENTER) # using ENTER
    sleep(3)
finally:
    driver.close()
    driver.quit()
