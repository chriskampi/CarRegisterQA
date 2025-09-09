from locators.page_paths.car_registration_year import CarRegistrationYearLocators


def navigate_to_employees_page(driver):
    """Navigate to employees page and return EmployeePage instance"""
    employee_page = CarRegistrationYearLocators(driver)
    driver.get(employee_page.url)
    return employee_page