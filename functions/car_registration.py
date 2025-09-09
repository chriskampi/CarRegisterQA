from functions.pages import navigate_to_employees_page

def validate_year_list(driver, year_list):
    """
    Validate a list of years in the car registration year dropdown.
    
    Args:
        driver: Selenium WebDriver instance
        year_list: List of years to validate
    """
    page = navigate_to_employees_page(driver)
    page.validate_option_year_list(year_list)






