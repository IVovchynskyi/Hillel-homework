import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


def add_text2field(Xpath: str, text: str, *args, **kwargs):
    element = driver.find_element(By.XPATH, Xpath)
    element.clear()
    element.send_keys(text)
    return


def login(username: str, password: str, *args, **kwargs):
    login_username = '//*[@id="id_username"]'
    login_password = '//*[@id="id_password"]'
    login_sumit_button = '//*[@id="login-form"]/div[3]/input'
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, login_username)))  # login form is here,so:
    add_text2field(Xpath=login_username, text=username)
    add_text2field(Xpath=login_password, text=password)
    element = driver.find_element(By.XPATH, login_sumit_button)
    element.click()
    logged_in_name = '//*[@id="user-tools"]/strong'
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, logged_in_name)))  # it is here so we are in
    return


def search_by_searchbar(text_to_search: str, *args, **kwargs):
    """
    the function if only to be used at https://www.aqa.science/admin/auth/user/
    :param text_to_search: text to search via searchbar on the userlist page
    :return: set of usernames found by the search text or False if search results is empty
    """
    if driver.current_url != USER_LIST_URL:
        print(f"It is the wrong URL for this function: {driver.current_url} is not {USER_LIST_URL} !")
        return
    else:
        on_users_search_xpath = '//*[@id="searchbar"]'
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, on_users_search_xpath)))
        add_text2field(Xpath=on_users_search_xpath, text=text_to_search)
        driver.find_element(By.XPATH, on_users_search_xpath).send_keys(Keys.ENTER) # need to submit the search
        try:
            on_users_search_table_body_xpath = '//*[@id="result_list"]/tbody'
            driver.find_element(By.XPATH, on_users_search_table_body_xpath)
        except NoSuchElementException:
            found_usernames = False
        else:
            found_results_raw_text = driver.find_element(By.XPATH, on_users_search_table_body_xpath).text
            found_usernames = set(y.split(' ')[0] for y in found_results_raw_text.split('\n'))
        finally:
            # come back to user list page anyway
            driver.get(USER_LIST_URL)
            return found_usernames


MAIN_URL = "https://www.aqa.science/admin/login/?next=/admin/"
USER_LIST_URL = "https://www.aqa.science/admin/auth/user/"
# Yes, it is bad, I promise not to do such things further
USERNAME = 'admin'
PASSWORD = 'admin123'

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

    login(username=USERNAME, password=PASSWORD)

    # Go to users from login page
    to_Users_xpath = '//*[@id="content-main"]/div/table/tbody/tr[2]/th/a'
    to_Users_element = driver.find_element(By.XPATH, to_Users_xpath)
    to_Users_element.click()
    # wait till the Users page is ready
    on_Users_add_user_xpath = '//*[@id="content-main"]/ul/li/a'
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, on_Users_add_user_xpath)))

    user_to_be_created = {
        'Username': 'IgorV_testuser_no16',
        'Password': 'Test123!',
        'First name': 'no16',
        'Last name': '',
        'Email address': ''
    }


    if driver.current_url != USER_LIST_URL:
        print(f"It is the wrong URL for this function: {driver.current_url} is not {USER_LIST_URL} !")
        # return
    elif user_to_be_created['Username'] and user_to_be_created['Password']:
        on_Users_add_user_xpath = '//*[@id="content-main"]/ul/li/a'
        # Wait till the button is here
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, on_Users_add_user_xpath)))
        # the button is here so we can click on it
        driver.find_element(By.XPATH, on_Users_add_user_xpath).click()
        # available on the first page
        user_username_xpath = '//*[@id="id_username"]'
        user_password_xpath = '//*[@id="id_password1"]'
        user_confirm_password_xpath = '//*[@id="id_password2"]'
        user_save_xpath = '//*[@id="user_form"]/div/div/input[1]'
        user_save_and_cont_edit_xpath = '//*[@id="user_form"]/div/div/input[3]'
        # available on the second page
        edit_user_firstname_xpath = '//*[@id="id_first_name"]'
        edit_user_lastname_xpath = '//*[@id="id_last_name"]'
        edit_user_email_xpath = '//*[@id="id_email"]'
        edit_user_delete_xpath = '//*[@id="user_form"]/div/div/p/a'
        # available only after the delete button is pressed
        edit_user_delete_yes_xpath = '//*[@id="content"]/form/div/input[2]'
        edit_user_delete_no_xpath = '//*[@id="content"]/form/div/a'
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, user_username_xpath)))
        add_text2field(Xpath=user_username_xpath, text=user_to_be_created['Username'])
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, user_password_xpath)))
        add_text2field(Xpath=user_password_xpath, text=user_to_be_created['Password'])
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, user_confirm_password_xpath)))
        add_text2field(Xpath=user_confirm_password_xpath, text=user_to_be_created['Password'])
        # let's go to another page; click the SAVE button
        driver.find_element(By.XPATH, user_save_xpath).click()
        # if there is any additional info - fill it
        if user_to_be_created['First name'] or user_to_be_created['Last name'] or user_to_be_created['Email address']:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, edit_user_firstname_xpath)))
            add_text2field(Xpath=edit_user_firstname_xpath, text=user_to_be_created['First name'])
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, edit_user_lastname_xpath)))
            add_text2field(Xpath=edit_user_lastname_xpath, text=user_to_be_created['Last name'])
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, edit_user_email_xpath)))
            add_text2field(Xpath=edit_user_email_xpath, text=user_to_be_created['Email address'])
        # let's finish the user creation; click the SAVE button
        driver.find_element(By.XPATH, user_save_xpath).click()
    else:
        print("you don't have username or password filled; the action cannot be processed")

    sleep(3)

finally:
    driver.close()
    driver.quit()
