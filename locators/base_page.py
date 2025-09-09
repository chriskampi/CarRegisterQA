from locators.elements import Elements
from utils.selenium_action_utils import SeleniumActions


class BasePage:
    """
    Base page class that provides common initialization for all page objects.
    
    This class handles the common setup that all page objects need:
    - WebDriver instance
    - Elements utility for XPath generation
    - SeleniumActions utility for browser interactions
    """
    
    def __init__(self, driver):
        """
        Initialize the BasePage with WebDriver instance.
        
        Args:
            driver: Selenium WebDriver instance for browser automation
        """
        self.driver = driver
        self.elements = Elements()
        self.actions = SeleniumActions(self.driver)
