import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def add_text2field(Xpath: str, text: str, *args, **kwargs):
    element = driver.find_element(By.XPATH, Xpath)
    element.clear()
    element.send_keys(text)
    return

def login(username: str, password: str, *args, **kwargs):
    login_button = '/html/body/div/div[1]/div/ul/li/a'
    element = driver.find_element(By.XPATH, login_button)
    element.click()
    login_username = '//*[@id="id_username"]'
    login_password = '//*[@id="id_password"]'
    login_sumit_button = '//*[@id="submit-id-submit"]'
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, login_username))) # login form is here,so:
    add_text2field(Xpath = login_username, text = username)
    add_text2field(Xpath = login_password, text = password)
    element = driver.find_element(By.XPATH, login_sumit_button)
    element.click()
    logged_in_name = '/html/body/div/div[1]/div/ul/li/a'
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, logged_in_name))) # it is here so we are in
    return

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

    login(username='admin' , password='admin123')

finally:
    driver.close()
    driver.quit()