import pytest
from functions.car_register_application import CarRegistrationApplication
from values_data.car_registration_applications import invalid_car_registration_too_few_letters

@pytest.mark.browser
class TestInvalidCarRegistrationTooFewLetters:
    """Test class for validating car registration form rejection when license plate has too few letters"""
    CAR_REGISTRATION = invalid_car_registration_too_few_letters()

    def test_submit_invalid_car_registration_too_few_letters(self, setup_browser_test):
        """Test rejection of car registration form with too few letters in license plate.
        
        This test verifies:
        - The car registration form loads correctly
        - Invalid car registration data with too few letters (2 letters + 4 numbers) is entered
        - Year selection from dropdown works
        - Form submission is rejected
        - Error alert is displayed
        - Success message is not displayed
        """
        self.CAR_REGISTRATION.submit_car_registration_form(setup_browser_test, False)
