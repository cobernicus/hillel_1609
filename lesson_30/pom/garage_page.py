from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class GaragePage:
    PROFILE_BUTTON = (By.XPATH, '//button[@id=\'userNavDropdown\']')
    PROFILE_REFERENCE = (By.XPATH, '//a[@href=\'/panel/profile\' and text()=\'Profile\']')
    PROFILE_TEXT_XPATH = (By.XPATH, '//p[contains(@class,\'profile_name\')]')
    PROFILE_TEXT_CSS = (By.CSS_SELECTOR, 'p.profile_name')
    def __init__(self, driver):
        self.driver = driver

    def profile_button_(self):
        """Функція для очікування наявності елемента на сторінці"""
        try:
            element = WebDriverWait(self.driver, timeout=10).until(EC.element_to_be_clickable(self.PROFILE_BUTTON))
            return element

        except TimeoutException:
            raise NoSuchElementException("За даний час елемент не зявився на сторінці")

    def profile_reference(self):
            try:
                element = WebDriverWait(self.driver, timeout=5).until(EC.element_to_be_clickable(self.PROFILE_REFERENCE))
                return element
            except TimeoutException:
                raise NoSuchElementException("За даний час елемент не зявився на сторінці")

    def profile_text(self):
        try:
            element = WebDriverWait(self.driver, timeout=10).until(EC.presence_of_element_located(self.PROFILE_TEXT_CSS))
            return element.get_attribute('innerText')
        except TimeoutException:
            raise NoSuchElementException("За даний час профіль не знайдений на сторінці")