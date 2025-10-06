from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UrbanRoutesPage:
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CALL_TAXI_BUTTON_LOCATOR = (By.XPATH, '//button[@class="button round"]')
    SUPPORTIVE_PLAN_LOCATOR = (By.XPATH, "//div[text()='Supportive']")
    SUPPORTIVE_PLAN_ACTIVE_LOCATOR = (By.CSS_SELECTOR, ".tcard.active")
    PHONE_NUMBER_LOCATOR = (By.CLASS_NAME, "np-text")
    PHONE_NUMBER_FIELD_LOCATOR = (By.ID, 'phone')
    SUBMIT_PHONE_NUMBER_LOCATOR = (By.XPATH, "//button[text()='Next']")
    SMS_CONFIRMATION_FIELD_LOCATOR = (By.XPATH, '//input[@placeholder="xxxx"]')
    SMS_CONFIRM_BUTTON_LOCATOR = (By.XPATH, "//button[text()='Confirm']")
    PAYMENT_METHOD_LOCATOR = (By.XPATH, '//div[@class="pp-text"]')
    ADD_CARD_LOCATOR = (By.CLASS_NAME, 'pp-plus')
    CARD_NUMBER_FIELD_LOCATOR = (By.ID, 'number')
    CARD_CODE_FIELD_LOCATOR = (By.XPATH, '//input[@placeholder="12"]')
    CHANGE_FOCUS_FROM_CODE_LOCATOR = (By.CLASS_NAME, "plc")
    CARD_LINK_BUTTON_LOCATOR = (By.XPATH, "//button[text()='Link']")
    CARD_PAYMENT_LOCATOR = (By.XPATH, '//div[@class="pp-value-text"]')
    DRIVER_COMMENT_FIELD_LOCATOR = (By.ID, "comment")
    BLANKET_SWITCH_LOCATOR = (By.CLASS_NAME, 'switch')
    VERIFY_THE_BLANKET_SELECTION_LOCATOR = (By.CLASS_NAME, 'switch-input')
    ORDER_ICE_CREAM_LOCATOR = (By.XPATH, '//div[text()="Ice cream"]/following-sibling::div//div[@class="counter-plus"]')
    ICE_CREAM_VALUE_LOCATOR = (By.XPATH, "//div[text()='Ice cream']//following-sibling::*//div[@class='counter-value']")
    ORDER_BUTTON_FOR_RIDE_LOCATOR = (By.CLASS_NAME, "smart-button-main")
    CAR_SEARCH_MODEL_LOCATOR = (By.CLASS_NAME, "order-buttons")

    def __init__(self, driver):
        self.driver = driver

    def enter_from_location(self, from_text):
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)

    def enter_to_location(self, to_text):
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)

    def get_locations_value(self):
        from_value = self.driver.find_element(*self.FROM_LOCATOR).get_attribute('value')
        to_value = self.driver.find_element(*self.TO_LOCATOR).get_attribute('value')
        return [from_value, to_value]

    def click_taxi_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CALL_TAXI_BUTTON_LOCATOR)
        ).click()

    def click_supportive_plan_button(self):
        self.driver.find_element(*self.SUPPORTIVE_PLAN_LOCATOR).click()

    def supportive_plan_active_value(self):
        return self.driver.find_element(*self.SUPPORTIVE_PLAN_ACTIVE_LOCATOR).text

    def click_phone_number_field(self):
        self.driver.find_element(*self.PHONE_NUMBER_LOCATOR).click()

    def enter_phone_number_field(self, phone_number):
        self.driver.find_element(*self.PHONE_NUMBER_FIELD_LOCATOR).send_keys(phone_number)

    def click_submit_phone_number_field(self):
        self.driver.find_element(*self.SUBMIT_PHONE_NUMBER_LOCATOR).click()

    def enter_sms_confirmation_field_locator(self, sms_confirmation):
        self.driver.find_element(*self.SMS_CONFIRMATION_FIELD_LOCATOR).send_keys(sms_confirmation)

    def click_sms_confirm_button_locator(self):
        self.driver.find_element(*self.SMS_CONFIRM_BUTTON_LOCATOR).click()

    def number_displayed(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.PHONE_NUMBER_LOCATOR)
        )
        return element.get_property("textContent")

    def clcik_payment_method_field_locator(self):
        self.driver.find_element(*self.PAYMENT_METHOD_LOCATOR).click()

    def clcik_add_card_locator(self):
        self.driver.find_element(*self.ADD_CARD_LOCATOR).click()

    def enter_card_number_field(self, card_number):
        self.driver.find_element(*self.CARD_NUMBER_FIELD_LOCATOR).send_keys(card_number)

    def enter_card_code_field(self, card_code):
        self.driver.find_element(*self.CARD_CODE_FIELD_LOCATOR).send_keys(card_code)

    def click_change_focus_from_code_locator(self):
        self.driver.find_element(*self.CHANGE_FOCUS_FROM_CODE_LOCATOR).click()

    def is_link_button_clickable(self):
        return self.driver.find_element(*self.CARD_LINK_BUTTON_LOCATOR).is_enabled()

    def click_card_link_button_locator(self):
        self.driver.find_element(*self.CARD_LINK_BUTTON_LOCATOR).click()

    def text_card_payment_locator(self):
        return self.driver.find_element(*self.CARD_PAYMENT_LOCATOR).text

    def enter_driver_comment_field(self, driver_comment):
        self.driver.find_element(*self.DRIVER_COMMENT_FIELD_LOCATOR).send_keys(driver_comment)

    def get_driver_comment(self):
        return self.driver.find_element(*self.DRIVER_COMMENT_FIELD_LOCATOR).get_attribute('value')

    def click_blanket_and_handkerchiefs(self):
        self.driver.find_element(*self.BLANKET_SWITCH_LOCATOR).click()

    def is_blanket_selected(self):
        return self.driver.find_element(*self.VERIFY_THE_BLANKET_SELECTION_LOCATOR).get_property('checked')

    def click_order_ice_cream(self):
        self.driver.find_element(*self.ORDER_ICE_CREAM_LOCATOR).click()

    def count_ice_cream(self):
        return self.driver.find_element(*self.ICE_CREAM_VALUE_LOCATOR).text

    def click_order_button(self):
        self.driver.find_element(*self.ORDER_BUTTON_FOR_RIDE_LOCATOR).click()

    def enter_locations(self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)

    def is_car_search_model_displayed(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CAR_SEARCH_MODEL_LOCATOR)
        ).is_displayed()
