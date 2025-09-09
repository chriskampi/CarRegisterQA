import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
import shutil


@pytest.fixture(scope="session")
def browser():
    """Setup Chrome browser for testing"""
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Commented out to run in visible mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--allow-running-insecure-content")
    chrome_options.add_argument("--disable-extensions")
    
    # Clear any existing webdriver cache to avoid corrupted downloads
    wdm_cache = os.path.expanduser("~/.wdm")
    if os.path.exists(wdm_cache):
        try:
            shutil.rmtree(wdm_cache)
        except Exception:
            pass  # Ignore cleanup errors
    
    # Setup Chrome driver with better error handling
    try:
        # Force download of fresh ChromeDriver
        driver_path = ChromeDriverManager(cache_valid_range=1).install()
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
    except Exception as e:
        # Fallback: try without webdriver-manager
        print(f"WebDriver Manager failed: {e}")
        print("Trying to use system ChromeDriver...")
        try:
            driver = webdriver.Chrome(options=chrome_options)
        except Exception as e2:
            print(f"System ChromeDriver also failed: {e2}")
            raise Exception(f"Could not start Chrome browser. WebDriver Manager error: {e}. System ChromeDriver error: {e2}")
    
    yield driver
    
    # Cleanup
    try:
        driver.quit()
    except Exception:
        pass  # Ignore cleanup errors


@pytest.fixture
def html_file_path():
    """Path to the HTML file for testing"""
    username = os.getenv('USERNAME') or os.getenv('USER')
    return rf"file:///C:/Users/{username}/Downloads/QA%20Programming%20Exercise.html"


@pytest.fixture
def setup_browser_test(browser, html_file_path):
    """Setup browser and navigate to HTML file"""
    browser.get(html_file_path)
    browser.maximize_window()
    return browser
