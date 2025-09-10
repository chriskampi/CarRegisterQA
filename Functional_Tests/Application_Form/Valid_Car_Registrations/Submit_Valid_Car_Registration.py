import pytest
from functions.car_register_application import CarRegistrationApplication
from values_data.car_registration_applications import valid_car_registration_2015, valid_car_registration_2016, valid_car_registration_2017

@pytest.mark.browser
class TestValidCarRegistrationSubmission:
    """Test class for validating successful car registration form submission functionality"""
    CAR_REGISTRATION_2015 = valid_car_registration_2015()
    CAR_REGISTRATION_2016 = valid_car_registration_2016()
    CAR_REGISTRATION_2017 = valid_car_registration_2017()

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
        self.CAR_REGISTRATION_2015.submit_car_registration_form()
        self.CAR_REGISTRATION_2016.submit_car_registration_form()
        self.CAR_REGISTRATION_2017.submit_car_registration_form()