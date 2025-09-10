import pytest
from functions.car_register_application import CarRegistrationApplication
from values_data.car_registration_applications import invalid_car_registration_with_space

@pytest.mark.browser
class TestInvalidCarRegistrationSpaceBar:
    """Test class for validating car registration form rejection when license plate has space"""
    CAR_REGISTRATION = invalid_car_registration_with_space()

    def test_submit_invalid_car_registration_space_bar(self, setup_browser_test):
        """Test rejection of car registration form with space in license plate.
        
        This test verifies:
        - The car registration form loads correctly
        - Invalid car registration data with space (RTU 2945) is entered
        - Year selection from dropdown works
        - Form submission is rejected
        - Error alert is displayed
        - Success message is not displayed
        """
        self.CAR_REGISTRATION.submit_car_registration_form(False)
