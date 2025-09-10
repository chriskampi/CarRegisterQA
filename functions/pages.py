from locators.page_paths.car_registration_application_form import CarRegistrationApplicationForm


def navigate_to_employees_page(driver):
    """Navigate to employees page and return EmployeePage instance"""
    employee_page = CarRegistrationApplicationForm(driver)
    driver.get(employee_page.url)
    return employee_page