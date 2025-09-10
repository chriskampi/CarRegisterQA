import pytest
from functions.car_register_application import CarRegistrationApplication
from values_data.car_registration_applications import invalid_car_registration_too_few_numbers

@pytest.mark.browser
class TestInvalidCarRegistrationTooFewNumbers:
    """Test class for validating car registration form rejection when license plate has too few numbers"""
    CAR_REGISTRATION = invalid_car_registration_too_few_numbers()

    def test_submit_invalid_car_registration_too_few_numbers(self, setup_browser_test):
        """Test rejection of car registration form with too few numbers in license plate.
        
        This test verifies:
        - The car registration form loads correctly
        - Invalid car registration data with too few numbers (3 letters + 3 numbers) is entered
        - Year selection from dropdown works
        - Form submission is rejected
        - Error alert is displayed
        - Success message is not displayed
        """
        self.CAR_REGISTRATION.submit_car_registration_form(False)
