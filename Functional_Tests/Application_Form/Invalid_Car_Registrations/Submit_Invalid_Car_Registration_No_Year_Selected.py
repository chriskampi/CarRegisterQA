import pytest
from values_data.car_registration_applications import invalid_car_registration_no_year_selected

@pytest.mark.browser
class TestInvalidCarRegistrationNoYearSelected:
    """Test class for validating car registration form rejection when no year is selected"""
    CAR_REGISTRATION = invalid_car_registration_no_year_selected()

    def test_submit_invalid_car_registration_no_year_selected(self, setup_browser_test):
        """Test rejection of car registration form when no year is selected.
        
        This test verifies:
        - The car registration form loads correctly
        - Valid car registration data (RTU2945) is entered
        - No year is selected from dropdown (default "Select a year")
        - Form submission is rejected
        - Error alert is displayed
        - Success message is not displayed
        """
        self.CAR_REGISTRATION.submit_car_registration_form(False)
