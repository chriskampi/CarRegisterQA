import pytest
from functions.car_register_application import CarRegistrationApplication
from values_data.car_registration_applications import invalid_car_registration_mixed_case_letters

@pytest.mark.browser
class TestInvalidCarRegistrationMixedCaseLetters:
    """Test class for validating car registration form rejection when license plate has mixed case letters"""
    CAR_REGISTRATION = invalid_car_registration_mixed_case_letters()

    def test_submit_invalid_car_registration_mixed_case_letters(self, setup_browser_test):
        """Test rejection of car registration form with mixed case letters in license plate.
        
        This test verifies:
        - The car registration form loads correctly
        - Invalid car registration data with mixed case letters (mixed case + 4 numbers) is entered
        - Year selection from dropdown works
        - Form submission is rejected
        - Error alert is displayed
        - Success message is not displayed
        """
        self.CAR_REGISTRATION.submit_car_registration_form(False)
