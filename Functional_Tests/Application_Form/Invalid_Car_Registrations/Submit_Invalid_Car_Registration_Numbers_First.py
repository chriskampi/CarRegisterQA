import pytest
from functions.car_register_application import CarRegistrationApplication
from values_data.car_registration_applications import invalid_car_registration_numbers_first

@pytest.mark.browser
class TestInvalidCarRegistrationNumbersFirst:
    """Test class for validating car registration form rejection when license plate has numbers before letters"""
    CAR_REGISTRATION = invalid_car_registration_numbers_first()

    def test_submit_invalid_car_registration_numbers_first(self, setup_browser_test):
        """Test rejection of car registration form with numbers before letters in license plate.
        
        This test verifies:
        - The car registration form loads correctly
        - Invalid car registration data with numbers before letters (4 numbers + 3 letters) is entered
        - Year selection from dropdown works
        - Form submission is rejected
        - Error alert is displayed
        - Success message is not displayed
        """
        self.CAR_REGISTRATION.submit_car_registration_form(False)
