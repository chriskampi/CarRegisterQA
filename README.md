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

## Test Coverage

The comprehensive test suite includes the following test categories:

### Functional Testing
- **Valid Scenarios**: 3 test cases covering valid car registrations with all years
- **Invalid Scenarios**: 14 test cases covering various invalid input patterns
- **Security Testing**: XSS prevention and input sanitization

### UI/UX Testing
- **Form Elements**: Visibility and proper display of all form elements
- **Alert Messages**: Success and error message display
- **Form Behavior**: Input validation and form reset functionality

### Test Categories by File

| Test File | Description | Test Cases |
|-----------|-------------|------------|
| `Submit_Valid_Car_Registration.py` | Valid registration scenarios | 3 |
| `Submit_Invalid_Car_Registration_*.py` | Invalid registration patterns | 14 |
| `Validate_Year_List.py` | Year dropdown validation | 1 |

### Test Data Coverage
- **Valid Patterns**: RTU9999, MNO2945, NIK0000
- **Invalid Patterns**: Empty, wrong length, case sensitivity, special characters, XSS
- **Years**: 2015, 2016, 2017, and default selection
- **Security**: script tags

## Configuration

### Browser Settings
- Tests run in head Chrome by default
- Window size: 1920x1080
- Chrome options optimized for testing

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

### Head Mode

To run tests in headless mode (not see the browser):
1. Edit `conftest.py`
2. Comment in the `--headless` option in `chrome_options`

## Dependencies

- **selenium**: WebDriver automation
- **pytest**: Testing framework
- **webdriver-manager**: Automatic ChromeDriver management

## Contributing

When adding new tests:
1. Follow the existing naming conventions
2. Use appropriate pytest markers
3. Add docstrings to test methods
4. Ensure tests are independent and can run in any order
