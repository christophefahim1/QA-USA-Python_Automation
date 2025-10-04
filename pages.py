from selenium.webdriver.common.by import By


class UrbanRoutesPage:
    from_locator = (By.ID, 'from')
    to_locator = (By.ID, 'to')
    call_taxi_button_locator = (By.XPATH, '//button[@class="button round"]')
    supportive_plan_locator = (By.XPATH, "//div[text()='Supportive']")
    supportive_plan_active_locator = (By.CSS_SELECTOR, ".tcard.active")
    phone_number_locator = (By.XPATH, '//div[@class="np-text"]')
    phone_number_field_locator = (By.ID, 'phone')
    submit_phone_number_locator = (By.XPATH, "//button[text()='Next']")
    sms_confirmation_field_locator = (By.XPATH, '//input[@placeholder="xxxx"]')
    sms_confirm_button_locator = (By.XPATH, "//button[text()='Confirm']")
    payment_method_locator = (By.XPATH, '//div[@class="pp-text"]')
    add_card_locator = (By.CLASS_NAME, 'pp-plus')
    card_number_field_locator = (By.ID, 'number')
    card_code_field_locator = (By.XPATH, '//input[@placeholder="12"]')
    change_focus_from_code_locator = (By.CLASS_NAME, "plc")
    card_link_button_locator = (By.XPATH, "//button[text()='Link']")
    card_payment_locator = (By.XPATH, '//div[@class="pp-value-text"]')
    driver_comment_field_locator = (By.ID, "comment")
    blanket_switch = (By.CLASS_NAME, 'switch')
    verify_the_blanket_selection = (By.CLASS_NAME, 'switch-input')
    order_ice_cream = (By.XPATH, '//div[text()="Ice cream"]/following-sibling::div//div[@class="counter-plus"]')
    ice_cream_value_locator = (By.XPATH, "//div[text()='Ice cream']//following-sibling::*//div[@class='counter-value']")
    order_button_for_ride_locator = (By.CLASS_NAME, "smart-button-main")
    car_search_model_locator = (By.CLASS_NAME, "order-buttons")

    def __init__(self, driver):
        self.driver = driver

    def enter_from_location(self, from_text):
        self.driver.find_element(*self.from_locator).send_keys(from_text)

    def enter_to_location(self, to_text):
        self.driver.find_element(*self.to_locator).send_keys(to_text)

    def get_locations_value(self):
        from_value = self.driver.find_element(*self.from_locator).get_attribute('value')
        to_value = self.driver.find_element(*self.to_locator).get_attribute('value')
        return [from_value, to_value]

    def click_taxi_button(self):
        self.driver.find_element(*self.call_taxi_button_locator).click()

    def click_supportive_plan_button(self):
        self.driver.find_element(*self.supportive_plan_locator).click()

    def supportive_plan_active_value(self):
        return self.driver.find_element(*self.supportive_plan_active_locator).text

    def click_phone_number_field(self):
        self.driver.find_element(*self.phone_number_locator).click()

    def enter_phone_number_field(self, phone_number):
        self.driver.find_element(*self.phone_number_field_locator).send_keys(phone_number)

    def click_submit_phone_number_field(self):
        self.driver.find_element(*self.submit_phone_number_locator).click()

    def enter_sms_confirmation_field_locator(self, sms_confirmation):
        self.driver.find_element(*self.sms_confirmation_field_locator).send_keys(sms_confirmation)

    def click_sms_confirm_button_locator(self):
        self.driver.find_element(*self.sms_confirm_button_locator).click()

    def number_displayed(self):
        return self.driver.find_element(*self.phone_number_locator).text

    def clcik_payment_method_field_locator(self):
        self.driver.find_element(*self.payment_method_locator).click()

    def clcik_add_card_locator(self):
        self.driver.find_element(*self.add_card_locator).click()

    def enter_card_number_field(self, card_number):
        self.driver.find_element(*self.card_number_field_locator).send_keys(card_number)

    def enter_card_code_field(self, card_code):
        self.driver.find_element(*self.card_code_field_locator).send_keys(card_code)

    def click_change_focus_from_code_locator(self):
        self.driver.find_element(*self.change_focus_from_code_locator).click()

    def is_link_button_clickable(self):
        return self.driver.find_element(*self.card_link_button_locator).is_enabled()

    def click_card_link_button_locator(self):
        self.driver.find_element(*self.card_link_button_locator).click()

    def text_card_payment_locator(self):
        return self.driver.find_element(*self.card_payment_locator).text

    def enter_driver_comment_field(self, driver_comment):
        self.driver.find_element(*self.driver_comment_field_locator).send_keys(driver_comment)

    def get_driver_comment(self):
        return self.driver.find_element(*self.driver_comment_field_locator).get_attribute('value')

    def click_blanket_and_handkerchiefs(self):
        self.driver.find_element(*self.blanket_switch).click()

    def is_blanket_selected(self):
        return self.driver.find_element(*self.verify_the_blanket_selection).get_property('checked')

    def click_order_ice_cream(self):
        self.driver.find_element(*self.order_ice_cream).click()

    def count_ice_cream(self):
        return self.driver.find_element(*self.ice_cream_value_locator).text

    def click_order_button(self):
        self.driver.find_element(*self.order_button_for_ride_locator).click()

    def enter_locations(self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)

    def is_car_search_model_displayed(self):
        return self.driver.find_element(*self.car_search_model_locator).is_displayed()
