# Car Registration QA - Comprehensive Test Automation Project

This project contains a comprehensive automated test suite using Selenium WebDriver and pytest for testing a car registration web application. The project demonstrates best practices in test automation, including Page Object Model, comprehensive test coverage, and robust error handling.

## Project Overview

The application under test is a simple car registration form that validates:
- **Car Registration Format**: Must match `^([A-Z]{3})([0-9]{4})$` (3 uppercase letters + 4 digits)
- **Year Selection**: Must select a year from dropdown (2015, 2016, 2017)
- **Form Validation**: Client-side JavaScript validation with success/error messaging

## Project Structure

```
CarRegisterQA/
├── conftest.py                           # Pytest configuration and browser setup
├── pytest.ini                           # Pytest settings and markers
├── requirements.txt                      # Python dependencies
├── run_tests.py                         # Test execution script
├── TEST_PLAN.md                         # Comprehensive test plan
├── Functional_Tests/                     # Test cases directory
│   ├── Submit_Valid_Car_Registration.py
│   ├── Submit_Invalid_Car_Registration_*.py
│   ├── Test_UI_Elements.py              # UI/UX test cases
│   ├── Test_Edge_Cases.py               # Edge case and boundary testing
│   ├── Test_Comprehensive_Validation.py # Comprehensive validation tests
│   └── Validate_Year_List.py
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
    └── years.py                        # Year data
```

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- Chrome browser installed on your system

### Installation

1. **Clone or download this project**
   ```bash
   cd CarRegisterQA
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure the HTML file exists**
   - Make sure the file `C:/Users/User/Downloads/QA Programming Exercise.html` exists
   - If the path is different, update the `html_file_path` fixture in `conftest.py`

## Running Tests

### Quick Start
```bash
# Run all tests
python run_tests.py

# Run with HTML report
python run_tests.py --html-report

# Check requirements
python run_tests.py --check-requirements
```

### Test Execution Options

#### Using the Test Runner Script
```bash
# Run all tests
python run_tests.py

# Run specific test category
python run_tests.py --category browser
python run_tests.py --category smoke
python run_tests.py --category regression

# Run specific test file
python run_tests.py --file Functional_Tests/Test_UI_Elements.py

# Generate HTML report
python run_tests.py --html-report

# Run with coverage report
python run_tests.py --coverage
```

#### Using pytest directly
```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run only browser tests
pytest -m browser

# Run tests and generate HTML report
pytest --html=reports/report.html --self-contained-html

# Run specific test file
pytest Functional_Tests/Test_UI_Elements.py

# Run specific test method
pytest Functional_Tests/Test_UI_Elements.py::TestUIElements::test_form_elements_visibility
```

## Test Coverage

The comprehensive test suite includes the following test categories:

### Functional Testing
- **Valid Scenarios**: 3 test cases covering valid car registrations with all years
- **Invalid Scenarios**: 14 test cases covering various invalid input patterns
- **Edge Cases**: Boundary testing and extreme scenarios
- **Security Testing**: XSS prevention and input sanitization

### UI/UX Testing
- **Form Elements**: Visibility and proper display of all form elements
- **User Interface**: Bootstrap styling and responsive design
- **Alert Messages**: Success and error message display
- **Form Behavior**: Input validation and form reset functionality

### Test Categories by File

| Test File | Description | Test Cases |
|-----------|-------------|------------|
| `Submit_Valid_Car_Registration.py` | Valid registration scenarios | 3 |
| `Submit_Invalid_Car_Registration_*.py` | Invalid registration patterns | 14 |
| `Test_UI_Elements.py` | UI/UX validation | 5 |
| `Test_Edge_Cases.py` | Boundary and edge case testing | 9 |
| `Test_Comprehensive_Validation.py` | Comprehensive validation suite | 4 |
| `Validate_Year_List.py` | Year dropdown validation | 1 |

**Total Test Cases**: 36+ individual test methods

### Test Data Coverage
- **Valid Patterns**: ABC1234, XYZ5678, DEF9012, RTU9999, MNO2945, NIK0000
- **Invalid Patterns**: Empty, wrong length, case sensitivity, special characters, XSS, unicode
- **Years**: 2015, 2016, 2017, and default selection
- **Security**: XSS injection, HTML injection, script tags

## Configuration

### Browser Settings
- Tests run in headless Chrome by default
- Window size: 1920x1080
- Chrome options optimized for testing

### Pytest Configuration
- Test discovery: `tests/` directory
- HTML reports: `reports/` directory
- Markers available: `browser`, `smoke`, `regression`

## Troubleshooting

### Common Issues

1. **ChromeDriver not found**
   - The project uses `webdriver-manager` to automatically download ChromeDriver
   - Ensure Chrome browser is installed

2. **HTML file not found**
   - Verify the file path in `conftest.py`
   - Ensure the file exists and is accessible

3. **Permission errors**
   - Run tests with appropriate permissions
   - Check file access rights

### Debug Mode

To run tests in non-headless mode (see the browser):
1. Edit `conftest.py`
2. Comment out the `--headless` option in `chrome_options`

## Dependencies

- **selenium**: WebDriver automation
- **pytest**: Testing framework
- **pytest-html**: HTML report generation
- **webdriver-manager**: Automatic ChromeDriver management

## Contributing

When adding new tests:
1. Follow the existing naming conventions
2. Use appropriate pytest markers
3. Add docstrings to test methods
4. Ensure tests are independent and can run in any order
