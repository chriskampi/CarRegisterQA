import pytest
from functions.car_registration import validate_year_list

@pytest.mark.browser
class TestBrowserFunctionality:
    """Test class for browser-based testing of the HTML file"""

    def test_page_loads_successfully(self, setup_browser_test):
        """Test that the HTML page loads without errors"""
        validate_year_list(setup_browser_test, ['2018'])