import pytest
from functions.car_register_application import CarRegistrationApplication
from values_data.car_registration_applications import invalid_car_registration_special_characters

@pytest.mark.browser
class TestInvalidCarRegistrationSpecialCharacters:
    """Test class for validating car registration form rejection when license plate has special characters"""
    CAR_REGISTRATION = invalid_car_registration_special_characters()

    def test_submit_invalid_car_registration_special_characters(self, setup_browser_test):
        """Test rejection of car registration form with special characters in license plate.
        
        This test verifies:
        - The car registration form loads correctly
        - Invalid car registration data with special characters (3 letters + special chars + numbers) is entered
        - Year selection from dropdown works
        - Form submission is rejected
        - Error alert is displayed
        - Success message is not displayed
        """
        self.CAR_REGISTRATION.submit_car_registration_form(setup_browser_test, False)
