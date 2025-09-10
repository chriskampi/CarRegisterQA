import pytest
from functions.car_register_application import CarRegistrationApplication
from values_data.car_registration_applications import invalid_car_registration_empty

@pytest.mark.browser
class TestInvalidCarRegistrationEmpty:
    """Test class for validating car registration form rejection when license plate is empty"""
    CAR_REGISTRATION = invalid_car_registration_empty()

    def test_submit_invalid_car_registration_empty(self, setup_browser_test):
        """Test rejection of car registration form with empty license plate.
        
        This test verifies:
        - The car registration form loads correctly
        - Invalid car registration data with empty license plate is entered
        - Year selection from dropdown works
        - Form submission is rejected
        - Error alert is displayed
        - Success message is not displayed
        """
        self.CAR_REGISTRATION.submit_car_registration_form(setup_browser_test, False)
