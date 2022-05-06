"""
Создать тест в котором происходит инициализация драйвера.
Перейдите на любой выбранный вами ресурс. Нажмите на копку либо введите текст в поле ввода.
----
Chrome is up to date
Version 101.0.4951.54 (Official Build) (64-bit)
-----
chromedriver_win32_(101_0_4951_141) https://chromedriver.storage.googleapis.com/index.html?path=101.0.4951.41/
"""

from selenium import webdriver


#  options

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep as sleep


# options = Options()
options = webdriver.ChromeOptions()

# options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try :
    driver.get("https://incompetech.com/wordpress/")
    sleep(3)
finally:
    driver.close()
    driver.quit()