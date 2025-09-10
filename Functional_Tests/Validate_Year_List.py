import pytest
from functions.car_register_application import CarRegistrationApplication
from values_data.years import car_registration_option_years

@pytest.mark.browser
class TestYearDropdownValidation:
    """Test class for validating year dropdown options in the car registration form"""
    YEAR_OPTIONS = car_registration_option_years
    CAR_REGISTRATION = CarRegistrationApplication()

    def test_validate_year_dropdown_options(self, setup_browser_test):
        """Test validation of available year options in the car registration dropdown.
        
        This test verifies:
        - All expected year options are present in the dropdown
        - The dropdown contains the correct number of options
        - Year options match the predefined test data
        """
        self.CAR_REGISTRATION.validate_year_list(setup_browser_test, self.YEAR_OPTIONS)