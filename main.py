import time

from pages import UrbanRoutesPage
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import data
import helpers


# from helpers import is_url_reachable


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_set_route(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page.enter_locations('East 2nd street, 601', '1300 1st street')
        time.sleep(2)
        actual_value = urban_routes_page.get_locations_value()
        expected_value = ['East 2nd street, 601', '1300 1st street']
        assert actual_value == expected_value

    def test_select_plan(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page.enter_locations('East 2nd street, 601', '1300 1st street')
        time.sleep(2)
        urban_routes_page.click_taxi_button()
        time.sleep(2)
        urban_routes_page.click_supportive_plan_button()
        time.sleep(2)
        actual_value = urban_routes_page.supportive_plan_active_value()
        expected_value = 'Supportive'
        assert expected_value in actual_value

    def test_fill_phone_number(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page.enter_locations('East 2nd street, 601', '1300 1st street')
        time.sleep(2)
        urban_routes_page.click_taxi_button()
        time.sleep(2)
        urban_routes_page.click_supportive_plan_button()
        time.sleep(2)
        urban_routes_page.click_phone_number_field()
        time.sleep(2)
        urban_routes_page.enter_phone_number_field('+1 123 123 12 12')
        time.sleep(2)
        urban_routes_page.click_submit_phone_number_field()
        time.sleep(2)
        sms_code = helpers.retrieve_phone_code(self.driver)
        urban_routes_page.enter_sms_confirmation_field_locator(sms_code)
        time.sleep(2)
        urban_routes_page.click_sms_confirm_button_locator()
        time.sleep(2)
        actual_value = urban_routes_page.number_displayed()
        expected_value = '+1 123 123 12 12'
        assert expected_value in actual_value

    def test_fill_card(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page.enter_locations('East 2nd street, 601', '1300 1st street')
        time.sleep(2)
        urban_routes_page.click_taxi_button()
        time.sleep(2)
        urban_routes_page.click_supportive_plan_button()
        time.sleep(2)
        urban_routes_page.clcik_payment_method_field_locator()
        time.sleep(2)
        urban_routes_page.clcik_add_card_locator()
        time.sleep(2)
        urban_routes_page.enter_card_number_field('123400004321')
        time.sleep(2)
        urban_routes_page.enter_card_code_field(1234)
        time.sleep(2)
        urban_routes_page.click_change_focus_from_code_locator()
        time.sleep(2)
        assert urban_routes_page.is_link_button_clickable()
        urban_routes_page.click_card_link_button_locator()
        actual_value = urban_routes_page.text_card_payment_locator()
        expected_value = 'Card'
        assert expected_value in actual_value

    def test_comment_for_driver(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page.enter_locations('East 2nd street, 601', '1300 1st street')
        time.sleep(1)
        urban_routes_page.click_taxi_button()
        time.sleep(1)
        urban_routes_page.click_supportive_plan_button()
        time.sleep(1)
        urban_routes_page.enter_driver_comment_field(data.MESSAGE_FOR_DRIVER)
        time.sleep(1)
        actual_value = urban_routes_page.get_driver_comment()
        expected_value = 'Stop at the juice bar, please'
        assert expected_value in actual_value

    def test_order_blanket_and_handkerchiefs(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page.enter_locations('East 2nd street, 601', '1300 1st street')
        time.sleep(1)
        urban_routes_page.click_taxi_button()
        time.sleep(1)
        urban_routes_page.click_supportive_plan_button()  # Only call this ONCE
        time.sleep(1)
        urban_routes_page.click_blanket_and_handkerchiefs()  # ADD THIS LINE!
        time.sleep(1)
        assert urban_routes_page.is_blanket_selected() == True

    def test_order_2_ice_creams(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page.enter_locations('East 2nd street, 601', '1300 1st street')
        time.sleep(1)
        urban_routes_page.click_taxi_button()
        time.sleep(1)
        urban_routes_page.click_supportive_plan_button()  # Only call this ONCE
        time.sleep(1)
        for i in range(2):
            urban_routes_page.click_order_ice_cream()
        time.sleep(1)
        actual_value = urban_routes_page.count_ice_cream()
        expected_value = '2'
        assert expected_value in actual_value

    def test_car_search_model_appears(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page.enter_locations('East 2nd street, 601', '1300 1st street')
        time.sleep(1)
        urban_routes_page.click_taxi_button()
        time.sleep(1)
        urban_routes_page.click_supportive_plan_button()
        time.sleep(1)
        urban_routes_page.click_phone_number_field()
        time.sleep(1)
        urban_routes_page.enter_phone_number_field('+1 123 123 12 12')
        time.sleep(1)
        urban_routes_page.click_submit_phone_number_field()
        time.sleep(1)
        sms_code = helpers.retrieve_phone_code(self.driver)
        urban_routes_page.enter_sms_confirmation_field_locator(sms_code)
        time.sleep(3)
        urban_routes_page.click_sms_confirm_button_locator()
        time.sleep(1)
        urban_routes_page.enter_driver_comment_field(data.MESSAGE_FOR_DRIVER)
        time.sleep(1)
        urban_routes_page.click_order_button()
        time.sleep(1)
        assert urban_routes_page.is_car_search_model_displayed() == True

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
