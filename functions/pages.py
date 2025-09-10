from locators.page_paths.car_registration_application_form import CarRegistrationApplicationForm
from utils.driver_context import driver_context


def navigate_to_employees_page(driver=None):
    """
    Navigate to employees page and return EmployeePage instance.
    
    Args:
        driver: Optional WebDriver instance. If not provided, uses the global driver context.
        
    Returns:
        CarRegistrationApplicationForm: The page object instance
        
    Raises:
        RuntimeError: If no driver is provided and none is set in the global context.
    """
    if driver is None:
        driver = driver_context.get_driver()
    
    employee_page = CarRegistrationApplicationForm(driver)
    driver.get(employee_page.url)
    return employee_page