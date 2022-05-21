import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)






url = "https://www.aqa.science/"

try:
    requests.get(url,timeout=3).raise_for_status()
except requests.exceptions.HTTPError as errh:
    print ("Http Error:",errh)
except requests.exceptions.ConnectionError as errc:
    print ("Error Connecting:",errc)
except requests.exceptions.Timeout as errt:
    print ("Timeout Error:",errt)
except requests.exceptions.RequestException as err:
    print ("OOps: Something Else",err)
else:
    driver.get(url)
    sleep(1)
    login_button = '/html/body/div/div[1]/div/ul/li/a'
    element = driver.find_element(By.XPATH, login_button)
    element.click()
    sleep(1)
    login_username = '//*[@id="id_username"]'
    login_password = '//*[@id="id_password"]'
    login_sumit_button = '//*[@id="submit-id-submit"]'
    # 3 lines below need to be replaced by "enter-text-function-byXPATH"
    element = driver.find_element(By.XPATH, login_username)
    element.clear() # just in case
    element.send_keys("admin") # need to be more secure

    element = driver.find_element(By.XPATH, login_password)
    element.clear() # just in case
    element.send_keys("admin123") # need to be more secure

    element = driver.find_element(By.XPATH, login_sumit_button)
    element.click()
    sleep(3)
finally:
    driver.close()
    driver.quit()