from functions.pages import navigate_to_employees_page


class CarRegistration:
    """
    A class to represent a car registration with license plate and year.
    """
    
    def __init__(self, license_plate="", year=None):
        """
        Initialize a CarRegistration object.
        
        Args:
            license_plate (str): The license plate number
            year (int): The year of the car
        """
        self._license_plate = license_plate
        self._year = year
    
    def get_license_plate(self):
        """
        Get the license plate number.
        
        Returns:
            str: The license plate number
        """
        return self._license_plate
    
    def set_license_plate(self, license_plate):
        """
        Set the license plate number.
        
        Args:
            license_plate (str): The license plate number to set
        """
        self._license_plate = license_plate
    
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


def validate_year_list(driver, year_list):
    """
    Validate a list of years in the car registration year dropdown.
    
    Args:
        driver: Selenium WebDriver instance
        year_list: List of years to validate
    """
    page = navigate_to_employees_page(driver)
    page.validate_option_year_list(year_list)


