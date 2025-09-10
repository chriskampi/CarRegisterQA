import pytest
from functions.car_register_application import CarRegistrationApplication
from values_data.car_registration_applications import valid_car_registration

@pytest.mark.browser
class TestBrowserFunctionality:
    """Test class for browser-based testing of the HTML file"""
    CAR_REGISTRATION = valid_car_registration()

    def test_page_loads_successfully(self, setup_browser_test):
        """Test that the HTML page loads without errors"""
        self.CAR_REGISTRATION.submit_car_registration_form(setup_browser_test)