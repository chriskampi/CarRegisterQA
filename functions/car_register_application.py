from functions.pages import navigate_to_employees_page


class CarRegistrationApplication:
    """
    A class to represent a car registration with license plate and year.
    """
    
    def __init__(self, car_registration="", year=None):
        """
        Initialize a CarRegistration object.
        
        Args:
            car_registration (str): The license plate number
            year (int): The year of the car
        """
        self._car_registration = car_registration
        self._year = year
    
    def get_car_registration(self):
        """
        Get the license plate number.
        
        Returns:
            str: The license plate number
        """
        return self._car_registration
    
    def set_car_registration(self, car_registration):
        """
        Set the license plate number.
        
        Args:
            car_registration (str): The license plate number to set
        """
        self._car_registration = car_registration
    
    def get_year(self):
        """
        Get the year of the car.
        
        Returns:
            int: The year of the car
        """
        return self._year
    
    def set_year(self, year):
        """
        Set the year of the car.
        
        Args:
            year (int): The year to set
        """
        self._year = year

    def submit_car_registration_form(self, success=True):
        """
        Submits a car registration form.

        This method processes the car registration request using the global driver context.
        It validates the driver information and ensures that all necessary details are in order
        before submitting the request. This method is part of the system for handling
        registration workflows.

        Parameters:
        success: Indicates whether the registration should be successful (default: True).

        Returns:
        bool: Indicates the success status of the registration submission.

        Raises:
        ValueError: If the driver information is incomplete or invalid.
        KeyError: If required details are missing in the driver's data.
        RuntimeError: If no driver has been set in the global context.
        """

        page = navigate_to_employees_page()
        page.validate_div_alert_message(exists=False)
        page.input_type_car_registration(self._car_registration)
        page.select_car_registration_year(str(self._year))
        page.click_submit_button()
        page.validate_div_success_message(self._car_registration, str(self._year), success)
        page.validate_div_alert_message(not success)

    @staticmethod
    def validate_year_list(year_list):
        """
        Validate a list of years in the car registration year dropdown.

        Args:
            year_list: List of years to validate
            
        Raises:
            RuntimeError: If no driver has been set in the global context.
        """
        page = navigate_to_employees_page()
        page.validate_option_year_list(year_list)


