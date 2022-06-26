import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, InvalidArgumentException
from time import sleep

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


def add_text2field(Xpath: str, text: str, *args, **kwargs):
    element = driver.find_element(By.XPATH, Xpath)
    element.clear()
    element.send_keys(text)
    return


def wait4it_presence(Xpath: str, wait_time=10, *args, **kwargs):
    WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH, Xpath)))
    return


def login(username: str, password: str, *args, **kwargs):
    login_username = '//*[@id="id_username"]'
    login_password = '//*[@id="id_password"]'
    login_sumit_button = '//*[@id="login-form"]/div[3]/input'
    wait4it_presence(login_username)  # login form is here,so:
    add_text2field(Xpath=login_username, text=username)
    add_text2field(Xpath=login_password, text=password)
    element = driver.find_element(By.XPATH, login_sumit_button)
    element.click()
    logged_in_name = '//*[@id="user-tools"]/strong'
    wait4it_presence(logged_in_name)  # it is here so we are in
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
        wait4it_presence(on_users_search_xpath)
        add_text2field(Xpath=on_users_search_xpath, text=text_to_search)
        driver.find_element(By.XPATH, on_users_search_xpath).send_keys(Keys.ENTER)  # need to submit the search
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


def create_user(user_dict: dict, *args, **kwargs):
    """
    The fuction creates user from USER_LIST_URL = "https://www.aqa.science/admin/auth/user/"
    :param user_dict: the dictionary of the user's parameters to create
    if ['Username'] and ['Password'] is NULL - function will return NULL (the user will not be created)
    if neither ['First name'] nor ['Last name'] nor ['Email address'] is present the user will be created as is
    if any of these parameters is there - it will be added to the user
    :return:
    False if the fuction was used not from the USER_LIST_URL
    False if there are no ['Username'] or/and ['Password']
    user_change_link - the user link - if the creation was succesfull
    """
    if driver.current_url != USER_LIST_URL:
        print(f"It is the wrong URL for this function: {driver.current_url} is not {USER_LIST_URL} !")
        return False
    elif user_dict['Username'] and user_dict['Password']:
        on_Users_add_user_xpath = '//*[@id="content-main"]/ul/li/a'
        wait4it_presence(on_Users_add_user_xpath)
        driver.find_element(By.XPATH, on_Users_add_user_xpath).click()
        # available on the first page
        user_username_xpath = '//*[@id="id_username"]'
        user_password_xpath = '//*[@id="id_password1"]'
        user_confirm_password_xpath = '//*[@id="id_password2"]'
        user_save_xpath = '//*[@id="user_form"]/div/div/input[1]'
        user_save_and_cont_edit_xpath = '//*[@id="user_form"]/div/div/input[3]'  # unfortunately useless now
        # available on the second page
        edit_user_firstname_xpath = '//*[@id="id_first_name"]'
        edit_user_lastname_xpath = '//*[@id="id_last_name"]'
        edit_user_email_xpath = '//*[@id="id_email"]'
        # the error note
        error_note_xpath = '//*[@id="user_form"]/div/p'
        wait4it_presence(user_username_xpath)
        add_text2field(Xpath=user_username_xpath, text=user_dict['Username'])
        wait4it_presence(user_password_xpath)
        add_text2field(Xpath=user_password_xpath, text=user_dict['Password'])
        wait4it_presence(user_confirm_password_xpath)
        add_text2field(Xpath=user_confirm_password_xpath, text=user_dict['Password'])
        # let's go to another page; click the SAVE button
        driver.find_element(By.XPATH, user_save_xpath).click()

        # it is important o get this link; it is the user link (also the user change link)
        user_change_link = driver.current_url
        # if there is any additional info - fill it
        if user_dict['First name'] or user_dict['Last name'] or user_dict['Email address']:
            wait4it_presence(edit_user_firstname_xpath)
            add_text2field(Xpath=edit_user_firstname_xpath, text=user_dict['First name'])
            wait4it_presence(edit_user_lastname_xpath)
            add_text2field(Xpath=edit_user_lastname_xpath, text=user_dict['Last name'])
            wait4it_presence(edit_user_email_xpath)
            add_text2field(Xpath=edit_user_email_xpath, text=user_dict['Email address'])
        # let's finish the user creation; click the SAVE button
        driver.find_element(By.XPATH, user_save_xpath).click()
        return user_change_link
    else:
        print("you don't have username or password filled; the action cannot be processed")
        return False


def change_user(user_link: str, user_parameters: dict, *args, **kwargs):
    """
    the function to change given user parameters; please be informed:
    at the moment only  username, first name, last name and email are implemented
    :param user_link: the user link allowing to change the user
    :param user_parameters: all the user parameters to be changed
    :return: True if the change was successful and False if it was not
    """
    try:
        start_point = driver.current_url  # we need to know the initial point; we will go there after all
        driver.get(user_link)
        if driver.current_url != user_link:
            raise InvalidArgumentException
    except InvalidArgumentException:
        print(f"Something went wrong: the link {user_link} is invalid")
        result = False
    else:
        user_username_xpath = '//*[@id="id_username"]'
        user_firstname_xpath = '//*[@id="id_first_name"]'
        user_lastname_xpath = '//*[@id="id_last_name"]'
        user_email_xpath = '//*[@id="id_email"]'
        user_save_xpath = '//*[@id="user_form"]/div/div/input[1]'
        error_note_xpath = '//*[@id="user_form"]/div/p'

        if user_parameters['Username']:
            wait4it_presence(user_username_xpath)
            add_text2field(Xpath=user_username_xpath, text=user_parameters['Username'])
        if user_parameters['First name']:
            wait4it_presence(user_firstname_xpath)
            add_text2field(Xpath=user_firstname_xpath, text=user_parameters['First name'])
        if user_parameters['Last name']:
            wait4it_presence(user_lastname_xpath)
            add_text2field(Xpath=user_lastname_xpath, text=user_parameters['Last name'])
        if user_parameters['Email address']:
            wait4it_presence(user_email_xpath)
            add_text2field(Xpath=user_email_xpath, text=user_parameters['Email address'])
        # we need to save the changes
        wait4it_presence(user_save_xpath)
        driver.find_element(By.XPATH, user_save_xpath).click()
        # but something might go wrong
        try:
            driver.find_element(By.XPATH, error_note_xpath)
        except NoSuchElementException:
            result = True
        else:
            print("Something went wrong: you have entered an invalid parameter; user changes cannot be saved")
            result = False
    finally:
        driver.get(start_point)
        return result


def read_user(user_link: str, *args, **kwargs):
    """
    the function to get user parameter via the user link
    :param user_link: the user link allowing to change the user
    :return: dict with following user parameters Username, First name, Last name and Email address
    """
    try:
        start_point = driver.current_url  # we need to know the initial point; we will go there after all
        driver.get(user_link)
        if driver.current_url != user_link:
            raise InvalidArgumentException
    except InvalidArgumentException:
        print(f"Something went wrong: the link {user_link} is invalid")
        return False
    else:
        result = dict.fromkeys(['Username', 'First name','Last name','Email address'])
        user_username_xpath = '//*[@id="id_username"]'
        user_firstname_xpath = '//*[@id="id_first_name"]'
        user_lastname_xpath = '//*[@id="id_last_name"]'
        user_email_xpath = '//*[@id="id_email"]'

        wait4it_presence(user_username_xpath)
        result['Username'] = driver.find_element(By.XPATH, user_username_xpath).get_attribute("value")
        # print(driver.find_element(By.XPATH, user_username_xpath).text())
        wait4it_presence(user_firstname_xpath)
        result['First name'] = driver.find_element(By.XPATH, user_firstname_xpath).get_attribute("value")
        wait4it_presence(user_lastname_xpath)
        result['Last name'] = driver.find_element(By.XPATH, user_lastname_xpath).get_attribute("value")
        # print(driver.find_element(By.XPATH, user_lastname_xpath).text())
        wait4it_presence(user_email_xpath)
        result['Email address'] = driver.find_element(By.XPATH, user_email_xpath).get_attribute("value")
        # print(driver.find_element(By.XPATH, user_email_xpath).text())

        return result

    finally:
        driver.get(start_point)


def delete_user(user_link: str, *args, **kwargs):
    try:
        start_point = driver.current_url  # we need to know the initial point; we will go there after all
        driver.get(user_link)
        if driver.current_url != user_link:
            raise InvalidArgumentException
    except InvalidArgumentException:
        print(f"Something went wrong: the link {user_link} is invalid")
        result = False
    else:
        user_delete_xpath = '//*[@id="user_form"]/div/div/p/a'
        user_delete_yes_xpath = '//*[@id="content"]/form/div/input[2]'
        user_delete_no_xpath = '//*[@id="content"]/form/div/a'
        wait4it_presence(user_delete_xpath)
        driver.find_element(By.XPATH, user_delete_xpath).click()
        wait4it_presence(user_delete_yes_xpath)
        driver.find_element(By.XPATH, user_delete_yes_xpath).click()
        result = True
    finally:
        driver.get(start_point)
        return result


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
    wait4it_presence(on_Users_add_user_xpath)

    user_to_be_created = {
        'Username': 'IgorV_testuser_no29',
        'Password': 'Test123!',
        'First name': '',
        'Last name': '',
        'Email address': ''
    }

    user_to_be_changed = {
        'Username': 'IgorV_testuser_no29',
        'First name': 'first265',
        'Last name': 'last265',
        'Email address': 'email265@mail.com'
    }



    # checking that there are no such user before the creation
    assert search_by_searchbar(text_to_search=user_to_be_created['Username']) == False, "Rough search has found the " \
                                                                                        "user, need to abort user " \
    # creating the user and the variable with the user link in the same time
    user_link = create_user(user_to_be_created)
    # checking that the user was created
    assert search_by_searchbar(text_to_search=user_to_be_changed['Username']), "No user found, so user creation was unsuccessful"
    # changing the user
    change_user(user_link=user_link, user_parameters=user_to_be_changed)
    # checking that the user was changed according to the input dictionary
    assert read_user(user_link) == user_to_be_changed, "changing input and obtained does not match"
    # deleting the user
    delete_user(user_link=user_link)
    # checking that the user was deleted
    assert search_by_searchbar(text_to_search=user_to_be_created['Username']) == False, "Rough search has found the " \
                                                                                        "user,  so user deleting was " \
                                                                                        "unsuccessful "


finally:
    driver.close()
    driver.quit()
