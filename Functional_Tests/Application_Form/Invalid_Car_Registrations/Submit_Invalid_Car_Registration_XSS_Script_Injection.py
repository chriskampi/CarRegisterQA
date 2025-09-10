import pytest
from functions.car_register_application import CarRegistrationApplication
from values_data.car_registration_applications import invalid_car_registration_xss_script_injection

@pytest.mark.browser
class TestInvalidCarRegistrationXSSScriptInjection:
    """Test class for validating car registration form rejection when license plate contains XSS script injection"""
    CAR_REGISTRATION = invalid_car_registration_xss_script_injection()

    def test_submit_invalid_car_registration_xss_script_injection(self, setup_browser_test):
        """Test rejection of car registration form with XSS script injection in license plate.
        
        This test verifies:
        - The car registration form loads correctly
        - Invalid car registration data with XSS script injection is entered
        - Year selection from dropdown works
        - Form submission is rejected (XSS prevention)
        - Error alert is displayed
        - Success message is not displayed
        - No JavaScript execution occurs (security validation)
        """
        self.CAR_REGISTRATION.submit_car_registration_form(False)
