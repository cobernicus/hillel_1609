import time

from selenium import webdriver

from lesson_27.pom.home_page import HomePage


class TestTrackingPage:
    track_number = '20400435461505'
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://tracking.novaposhta.ua/#/uk")

    def teardown_method(self, method):
        self.driver.quit()

    def test_tracking_data(self):
        page = HomePage(self.driver)
        page.input_track_number(HomePage.INPUT_CSS, self.track_number)
        time.sleep(2)
        page.click_button(HomePage.BUTTON_ID)
        time.sleep(2)
        page.close_popup(HomePage.POPUP_CSS)
        time.sleep(2)
        status = page.check_inner_text(HomePage.MESSAGE)
        assert status == 'Відправлення отримано. Грошовий переказ видано одержувачу.'
