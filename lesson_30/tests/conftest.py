import pytest
import time
import allure

from selenium import webdriver
from lesson_30.pom.garage_page import GaragePage
from lesson_30.pom.home_page import HomePage
from lesson_30.pom.sign_up_page import Sigh_Up_Page


UserName = 'guest'
Password = 'welcome2qauto'


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def open_home_page(driver):
    def _open_home_page():
        page = driver.get(f"https://{UserName}:{Password}@qauto2.forstudy.space")
        driver.maximize_window()
        time.sleep(2)
        return page
    return _open_home_page


@pytest.fixture
def open_sign_up_form(driver):
    def _user_sign_up_form():
        home_page = HomePage(driver)
        element = home_page.sign_up_button().click()
        time.sleep(2)
        return element
    return _user_sign_up_form

@pytest.fixture
def input_name(driver):
    def _input_name(name):
        sign_up_page = Sigh_Up_Page(driver)
        sign_up_page.name_field().click()
        time.sleep(2)
        sign_up_page.name_field().send_keys(name)
        time.sleep(2)
        return sign_up_page
    return _input_name

@pytest.fixture
def check_name_in_field(driver):
    def _check_name_in_field(name):
        sign_up_page = Sigh_Up_Page(driver)
        name_in_field = sign_up_page.name_text()
        check = (name == name_in_field)
        return check
    return _check_name_in_field


@pytest.fixture
def input_last_name(driver):
    def _input_last_name(last_name):
        sign_up_page = Sigh_Up_Page(driver)
        sign_up_page.last_name_field().click()
        time.sleep(2)
        sign_up_page.last_name_field().send_keys(last_name)
        time.sleep(2)
    return _input_last_name

@pytest.fixture
def input_email(driver):
    def _input_email(email):
        sign_up_page = Sigh_Up_Page(driver)
        sign_up_page.email_field().click()
        sign_up_page.email_field().send_keys(email)
    return _input_email

@pytest.fixture
def input_password(driver):
    def _input_password(password):
        sign_up_page = Sigh_Up_Page(driver)
        sign_up_page.password_field().click()
        sign_up_page.password_field().send_keys(password)
    return _input_password

@pytest.fixture
def repeat_input_password(driver):
    def _repeat_input_password(password ):
        sign_up_page = Sigh_Up_Page(driver)
        sign_up_page.reenter_password_field().click()
        sign_up_page.reenter_password_field().send_keys(password)
    return _repeat_input_password

@pytest.fixture
def press_register_button(driver):
    def _press_register_button():
        sign_up_page = Sigh_Up_Page(driver)
        sign_up_page.register_button().click()
    return _press_register_button

@pytest.fixture
def open_user_profile(driver):
    def _open_user_profile():
        garage_page = GaragePage(driver)
        garage_page.profile_button_().click()
        garage_page.profile_reference().click()
    return _open_user_profile

@pytest.fixture
def check_if_name_present_in_profile(driver):
    def _check_if_name_present_in_profile(name):
        garage_page = GaragePage(driver)
        name_in_profile = garage_page.profile_text()
        check = (name in name_in_profile)
        return check
    return _check_if_name_present_in_profile

def open_home_page_(driver):
    driver.get(f"https://{UserName}:{Password}@qauto2.forstudy.space")
    driver.maximize_window()
    time.sleep(4)

    return driver
def open_sign_up_form_(driver):
    element = driver.find_element(*HomePage.SIGN_UP)
    element.click()
    return driver

