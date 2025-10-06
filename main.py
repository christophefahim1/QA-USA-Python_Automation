from encodings.uu_codec import uu_encode
from pages import UrbanRoutesPage
from selenium import webdriver
import data
import helpers


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
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        actual_value = urban_routes_page.get_locations_value()
        expected_value = [data.ADDRESS_FROM, data.ADDRESS_TO]
        assert actual_value == expected_value

    def test_select_plan(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.click_taxi_button()
        urban_routes_page.click_supportive_plan_button()
        actual_value = urban_routes_page.supportive_plan_active_value()
        expected_value = 'Supportive'
        assert expected_value in actual_value

    def test_fill_phone_number(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.click_taxi_button()
        urban_routes_page.click_supportive_plan_button()
        urban_routes_page.click_phone_number_field()
        urban_routes_page.enter_phone_number_field(data.PHONE_NUMBER)
        urban_routes_page.click_submit_phone_number_field()
        sms_code = helpers.retrieve_phone_code(self.driver)
        urban_routes_page.enter_sms_confirmation_field_locator(sms_code)
        urban_routes_page.click_sms_confirm_button_locator()
        actual_value = urban_routes_page.number_displayed()
        expected_value = data.PHONE_NUMBER
        assert expected_value in actual_value

    def test_fill_card(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.click_taxi_button()
        urban_routes_page.click_supportive_plan_button()
        urban_routes_page.clcik_payment_method_field_locator()
        urban_routes_page.clcik_add_card_locator()
        urban_routes_page.enter_card_number_field(data.CARD_NUMBER)
        urban_routes_page.enter_card_code_field(data.CARD_CODE)
        urban_routes_page.click_change_focus_from_code_locator()
        assert urban_routes_page.is_link_button_clickable()
        urban_routes_page.click_card_link_button_locator()
        actual_value = urban_routes_page.text_card_payment_locator()
        expected_value = 'Card'
        assert expected_value in actual_value

    def test_comment_for_driver(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.click_taxi_button()
        urban_routes_page.click_supportive_plan_button()
        urban_routes_page.enter_driver_comment_field(data.MESSAGE_FOR_DRIVER)
        actual_value = urban_routes_page.get_driver_comment()
        expected_value = data.MESSAGE_FOR_DRIVER
        assert expected_value in actual_value

    def test_order_blanket_and_handkerchiefs(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.click_taxi_button()
        urban_routes_page.click_supportive_plan_button()
        urban_routes_page.click_blanket_and_handkerchiefs()  # ADD THIS LINE!
        assert urban_routes_page.is_blanket_selected() == True

    def test_order_2_ice_creams(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.click_taxi_button()
        urban_routes_page.click_supportive_plan_button()
        for i in range(2):
            urban_routes_page.click_order_ice_cream()
        actual_value = urban_routes_page.count_ice_cream()
        expected_value = '2'
        assert expected_value in actual_value

    def test_car_search_model_appears(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.click_taxi_button()
        urban_routes_page.click_supportive_plan_button()
        urban_routes_page.click_phone_number_field()
        urban_routes_page.enter_phone_number_field(data.PHONE_NUMBER)
        urban_routes_page.click_submit_phone_number_field()
        sms_code = helpers.retrieve_phone_code(self.driver)
        urban_routes_page.enter_sms_confirmation_field_locator(sms_code)
        urban_routes_page.click_sms_confirm_button_locator()
        urban_routes_page.enter_driver_comment_field(data.MESSAGE_FOR_DRIVER)
        urban_routes_page.click_order_button()
        assert urban_routes_page.is_car_search_model_displayed() == True

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
