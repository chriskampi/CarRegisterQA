from locators.elements import Elements
from utils.selenium_action_utils import SeleniumActions

class CarRegistrationYearLocators:

        def __init__(self, driver):
            self.driver = driver
            self.elements = Elements()
            self.actions = SeleniumActions(self.driver)
            self.url = f"file:///C:/Users/{self.elements.username}/Downloads/QA%20Programming%20Exercise.html"

        def input_type_car_registration(self, car_registration):

            path = f"{self.elements.input_via_placeholder}"

            self.actions.find_and_type(path, car_registration)

        def click_submit_button(self):
            path = self.elements.button_submit()
            self.actions.find_and_click(path)

        def select_car_registration_year(self, year):

            self.actions.find_and_click(self.elements.select_via_id("select-year"))
            self.actions.find_and_click(self.elements.option_via_text(year))

        def validate_div_success_message(self, car_registration, year, exists: bool = True):
            path = (f"{self.elements.div_alert_success()}[contains(.,'Success! Selected {car_registration}"
                    f" with year {year}')]")
            return self.actions.find(path, exists)

        def validate_div_alert_message(self, exists: bool = True):
            path = f"{self.elements.div_alert_success()}[contains(.,'There was an error!')]"
            return self.actions.find(path, exists)



