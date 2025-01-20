import string
from random import choice
import allure
import lesson_30.pom.sign_up_page as sign_up_page
import lesson_30.tests.conftest as conftest
from selenium import webdriver

name = f'NewTestUser{choice(string.ascii_uppercase)}{choice(string.ascii_lowercase)}'
last_name = f'{name}last'
email = f'{name}@test.com'
password = 'Abracadabra1'

UserName = 'guest'
Password = 'welcome2qauto'


def driver():
    driver = webdriver.Chrome()
    return driver


@allure.feature("Check sign up frame appearance")
def test_open_sign_up_page_(driver):
    with allure.step("Step 1"):
        conftest.open_home_page_(driver)
    with allure.step("Step 2"):
        conftest.open_sign_up_form_(driver)
    assert driver.find_element(*sign_up_page.Sigh_Up_Page.INPUT_NAME).is_displayed()


@allure.feature("Check whole sign up sequence")
def test_sign_up_on_qauto2_page(driver, open_home_page, open_sign_up_form, input_name,
                                input_last_name, input_email, input_password, repeat_input_password,
                                press_register_button, open_user_profile, check_if_name_present_in_profile):
    open_home_page()
    open_sign_up_form()
    input_name(name)
    input_last_name(last_name)
    input_email(email)
    input_password(password)
    repeat_input_password(password)
    press_register_button()
    open_user_profile()
    assert check_if_name_present_in_profile(name)

def driver_close(driver):
    driver.quit()
