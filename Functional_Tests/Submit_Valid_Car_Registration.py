import pytest
from functions.car_register_application import CarRegistrationApplication
from values_data.car_registration_applications import valid_car_registration

@pytest.mark.browser
class TestValidCarRegistrationSubmission:
    """Test class for validating successful car registration form submission functionality"""
    CAR_REGISTRATION = valid_car_registration()

    def test_submit_valid_car_registration_form(self, setup_browser_test):
        """Test successful submission of a valid car registration form with license plate and year selection.
        
        This test verifies:
        - The car registration form loads correctly
        - Valid car registration data can be entered
        - Year selection from dropdown works
        - Form submission is successful
        - Success message is displayed with correct details
        - No error alerts are shown
        """
        self.CAR_REGISTRATION.submit_car_registration_form(setup_browser_test)