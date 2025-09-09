import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os


@pytest.fixture(scope="session")
def browser():
    """Setup Chrome browser for testing"""
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    
    # Setup Chrome driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    yield driver
    
    # Cleanup
    driver.quit()


@pytest.fixture
def html_file_path():
    """Path to the HTML file for testing"""
    return r"file:///C:/Users/User/Downloads/QA%20Programming%20Exercise.html"


@pytest.fixture
def setup_browser_test(browser, html_file_path):
    """Setup browser and navigate to HTML file"""
    browser.get(html_file_path)
    browser.maximize_window()
    return browser
