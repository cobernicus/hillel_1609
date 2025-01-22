from selenium.webdriver.common.by import By
from lesson_27.pom.base_page import BasePage


class HomePage(BasePage):

    INPUT = (By.XPATH, '//input[@class=\'track__form-group-input\']')
    INPUT_ID = (By.ID, "en")
    INPUT_CSS = (By.CSS_SELECTOR, "#en")

    BUTTON_XPATH = (By.XPATH, '//input[@class=\'track__form-group-btn\']')
    BUTTON_ID = (By.ID, "np-number-input-desktop-btn-search-en")

    POPUP_CSS = (By.CSS_SELECTOR, ".button")
    MESSAGE = (By.CSS_SELECTOR, 'div.header__status-text')



    def __init__(self, driver):
        BasePage.__init__(self, driver)
        super().__init__(driver=driver)

    def input_track_number(self, locator, track_num: str):
        self.driver.find_element(locator[0], locator[1]).click()
        self.driver.find_element(locator[0], locator[1]).send_keys(track_num)

    def click_button(self, locator):
        self.driver.find_element(locator[0], locator[1]).click()

    def close_popup (self, locator):
        element = self.driver.find_element(locator[0], locator[1])
        if element.is_displayed():
            element.click()

    def check_inner_text(self, locator):
        try:
            text = self.driver.find_element(locator[0], locator[1]).get_attribute('innerText').strip()
            print('\nstatus: ', text)
            return text
        except:
            print('No status found')
