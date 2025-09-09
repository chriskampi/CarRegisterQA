# Car Register QA - Selenium Pytest Project

This project contains automated browser tests using Selenium WebDriver and pytest for testing a local HTML file.

## Project Structure

```
CarRegisterQA/
├── conftest.py              # Pytest configuration and browser setup
├── pytest.ini              # Pytest settings and markers
├── requirements.txt         # Python dependencies
├── Functional_Tests/
│   └── test_browser.py     # Browser test cases
└── README.md               # This file
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

### Run all tests
```bash
pytest
```

### Run tests with verbose output
```bash
pytest -v
```

### Run only browser tests
```bash
pytest -m browser
```

### Run tests and generate HTML report
```bash
pytest --html=reports/report.html --self-contained-html
```

### Run specific test
```bash
pytest Functional_Tests/test_browser.py::TestBrowserFunctionality::test_page_loads_successfully
```

## Test Coverage

The test suite includes the following browser tests:

- **Page Loading**: Verifies the HTML page loads successfully
- **Content Validation**: Checks for basic page content and structure
- **Responsiveness**: Tests page behavior at different window sizes
- **Error Checking**: Validates no critical console errors
- **Performance**: Ensures page loads within acceptable time
- **Form Testing**: Validates form elements if present
- **Link Testing**: Checks link functionality if present
- **Accessibility**: Basic accessibility checks
- **Meta Tags**: Validates important meta tags

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
