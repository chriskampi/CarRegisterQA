import pytest
from functions.car_register_application import CarRegistrationApplication
from values_data.car_registration_applications import invalid_car_registration_too_many_letters

@pytest.mark.browser
class TestInvalidCarRegistrationTooManyLetters:
    """Test class for validating car registration form rejection when license plate has too many letters"""
    CAR_REGISTRATION = invalid_car_registration_too_many_letters()

    def test_submit_invalid_car_registration_too_many_letters(self, setup_browser_test):
        """Test rejection of car registration form with too many letters in license plate.
        
        This test verifies:
        - The car registration form loads correctly
        - Invalid car registration data with too many letters (4+ letters + 4 numbers) is entered
        - Year selection from dropdown works
        - Form submission is rejected
        - Error alert is displayed
        - Success message is not displayed
        """
        self.CAR_REGISTRATION.submit_car_registration_form(False)
