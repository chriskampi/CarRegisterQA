import pytest
from values_data.car_registration_applications import invalid_car_registration_no_year_selected

@pytest.mark.browser
class TestInvalidCarRegistrationTooManyNumbers:
    """Test class for validating car registration form rejection when license plate has too many numbers"""
    CAR_REGISTRATION = invalid_car_registration_no_year_selected()

    def test_submit_invalid_car_registration_too_many_numbers(self, setup_browser_test):
        """Test rejection of car registration form with too many numbers in license plate.
        
        This test verifies:
        - The car registration form loads correctly
        - Invalid car registration data with too many numbers (3 letters + 5+ numbers) is entered
        - Year selection from dropdown works
        - Form submission is rejected
        - Error alert is displayed
        - Success message is not displayed
        """
        self.CAR_REGISTRATION.submit_car_registration_form(False)
