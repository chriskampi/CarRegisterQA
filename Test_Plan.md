# Car Registration QA - Comprehensive Test Automation Project

This project contains a comprehensive automated test suite using Selenium WebDriver
and pytest for testing a car registration web application. The project demonstrates best practices in test automation,
including Page Object Model, comprehensive test coverage, and robust error handling.

## 1. HTML File Analysis

### Application Structure
The car registration form is a simple web application with:
- **Input Field**: Car registration text input
- **Year Dropdown**: Selection of 2015, 2016, or 2017
- **Submit Button**: Form submission
- **Alert Messages**: Success and error feedback

### Validation Logic
- **RegEx Pattern**: `^([A-Z]{3})([0-9]{4})$`
- **Requirements**: Exactly 3 uppercase letters + 4 digits
- **Year Selection**: Must select a year (not default)

## 2. Test Plan

### 2.1 Testing Strategy
- **Equivalence Partitioning**: Grouping test cases by validity
- **Boundary Value Analysis**: Testing edge cases and limits
- **Error Guessing**: Testing common error scenarios

### 2.2 Test Categories
1. **Functional Testing**: Core functionality validation
3. **Security Testing**: Input validation and XSS prevention

## 3. Automated Test Implementation

### 3.1 Technology Stack
- **Selenium WebDriver**: Browser automation
- **pytest**: Test framework
- **webdriver-manager**: Driver management

### 3.2 Framework Architecture
- **Page Object Model**: Clean separation of concerns
- **Singleton Pattern**: Driver context management
- **Factory Pattern**: Test data object creation
- **Strategy Pattern**: Locator generation

### 3.3 Test Organization
```
Functional_Tests/
├── Submit_Valid_Car_Registration.py      # Valid scenarios
├── Submit_Invalid_Car_Registration_*.py  # Invalid scenarios
└── Validate_Year_List.py                 # Year dropdown validation
```

## 4. Test Cases Implemented

### 4.1 Valid Test Cases
- ✅ Valid car registration with year 2015
- ✅ Valid car registration with year 2016
- ✅ Valid car registration with year 2017

### 4.2 Invalid Test Cases
- ✅ Empty car registration
- ✅ Too few letters (2 letters + 4 numbers)
- ✅ Too many letters (4+ letters + 4 numbers)
- ✅ Too few numbers (3 letters + 3 numbers)
- ✅ Too many numbers (3 letters + 5+ numbers)
- ✅ Lowercase letters
- ✅ Mixed case letters
- ✅ Special characters
- ✅ Numbers before letters
- ✅ No year selected
- ✅ Greek letters
- ✅ Romanian pattern
- ✅ Space characters
- ✅ XSS script injection

## Project Overview

The application under test is a simple car registration form that validates:
- **Car Registration Format**: Must match `^([A-Z]{3})([0-9]{4})$` (3 uppercase letters + 4 digits)
- **Year Selection**: Must select a year from dropdown (2015, 2016, 2017)

## Project Structure

```
CarRegisterQA/
├── conftest.py                           # Pytest configuration and browser setup
├── pytest.ini                            # Pytest settings and markers
├── requirements.txt                      # Python dependencies
├── Functional_Tests/                     # Test cases directory
    └── Application_Form/
        └── Valid_Car_Registrations/
    │       ├── Submit_Valid_Car_Registration.py
        └── Invalid_Car_Registrations/
│           ├── Submit_Invalid_Car_Registration_*.py
        └── Year_Options/
            └── Validate_Year_List.py
├── functions/                           # Business logic and page objects
│   ├── car_register_application.py     # Main application logic
│   └── pages.py                        # Page navigation
├── locators/                           # Locator strategy and elements
│   ├── base_page.py                    # Base page class
│   ├── elements.py                     # XPath locator generation
│   └── page_paths/
│       └── car_registration_application_form.py
├── utils/                              # Utility classes
│   ├── driver_context.py               # WebDriver context management
│   └── selenium_action_utils.py        # Selenium action wrappers
└── values_data/                        # Test data management
    ├── car_registration_applications.py # Test data objects
    └── years.py                         # Year data