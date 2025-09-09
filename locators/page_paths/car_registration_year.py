from locators.base_page import BasePage

class CarRegistrationYearLocators(BasePage):
    """
    Page Object Model class for car registration year selection functionality.
    
    This class provides methods to interact with the car registration year form,
    including inputting car registration details, selecting years, clicking submit,
    and validating success/error messages.
    """

    def __init__(self, driver):
        """
        Initialize the CarRegistrationYearLocators with WebDriver instance.
        
        Args:
            driver: Selenium WebDriver instance for browser automation
        """
        super().__init__(driver)
        self.url = f"file:///C:/Users/{self.elements.username}/Downloads/QA%20Programming%20Exercise.html"

    def input_type_car_registration(self, car_registration):
        """
        Input car registration text into the registration input field.
        
        Args:
            car_registration (str): The car registration text to input
        """
        path = f"{self.elements.input_via_placeholder}"

        self.actions.find_and_type(path, car_registration)

    def click_submit_button(self):
        """
        Click the submit button to submit the car registration form.
        """
        path = self.elements.button_submit()
        self.actions.find_and_click(path)

    def select_car_registration_year(self, year):
        """
        Select a year from the car registration year dropdown.
        
        Args:
            year (str): The year to select from the dropdown
        """
        self.actions.find_and_click(self.elements.select_via_id("select-year"))
        self.actions.find_and_click(self.elements.option_via_text(year))

    def validate_div_success_message(self, car_registration, year, exists: bool = True):
        """
        Validate the presence of success message after form submission.
        
        Args:
            car_registration (str): The car registration text that was submitted
            year (str): The year that was selected
            exists (bool, optional): Whether to check if element exists or not. Defaults to True.
            
        Returns:
            bool: True if the success message is found (or not found if exists=False), False otherwise
        """
        path = (f"{self.elements.div_alert_success()}[contains(.,'Success! Selected {car_registration}"
                f" with year {year}')]")
        return self.actions.find(path, exists)

    def validate_div_alert_message(self, exists: bool = True):
        """
        Validate the presence of error alert message after form submission.
        
        Args:
            exists (bool, optional): Whether to check if element exists or not. Defaults to True.
            
        Returns:
            bool: True if the error message is found (or not found if exists=False), False otherwise
        """
        path = f"{self.elements.div_alert_success()}[contains(.,'There was an error!')]"
        return self.actions.find(path, exists)



