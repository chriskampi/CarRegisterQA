from time import sleep
from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SeleniumActions:
    def __init__(self, driver: WebDriver, wait_seconds: int = 10):
        self.driver = driver
        self.wait_seconds = wait_seconds

    def open_url(self, url: str) -> None:
        """Open a URL in the browser"""
        self.driver.get(url)

    def find(self, xpath: str, exists: bool = True) -> WebElement | bool:
        """
        Validate the existence of an xpath and optionally return the element

        Args:
            xpath: The XPath to find
            exists: If True, return the element. If False, just validate existence and return True/False

        Returns:
            WebElement if exists=True, bool if exists=False
        """
        if exists:
            # Original behavior - wait for element and return it
            wait = WebDriverWait(self.driver, self.wait_seconds)
            element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
            return element
        else:
            # Just check if element exists without waiting
            try:
                wait = WebDriverWait(self.driver, 0)  # No wait
                element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
                return True
            except:
                return False

    def find_and_click(self, xpath: str) -> None:
        """After validating the existence of the xpath, click it"""
        element = self.find(xpath)
        element.click()

    def find_and_type(self, xpath: str, text: str) -> None:
        """After validating the existence of the xpath, send keys"""
        element = self.find(xpath)
        element.clear()
        sleep(0.3)
        element.send_keys(text)

    def find_and_assert_count(self, xpath_pattern, expected_values) -> None:
        """
        Find elements using xpath pattern and assert that the count matches the expected list length.
        Validates each expected value exists using the xpath pattern,
        and counts all elements that match the xpath pattern.
        
        Args:
            xpath_pattern: The XPath pattern to find elements (e.g., "//option[text()='{}']")
            expected_values: List of expected values to validate and count against
            
        Raises:
            AssertionError: If the number of found elements doesn't match the expected list length
        """
        # Validate each expected value exists using the xpath pattern
        for value in expected_values:
            path = xpath_pattern + f"[contains(.,'{value}')]"
            self.find(path, exists=True)
        
        # Count all elements that match the xpath pattern
        elements = self.driver.find_elements(By.XPATH, xpath_pattern)
        found_count = len(elements)
        
        expected_count = len(expected_values)
        
        assert found_count == expected_count, \
            f"Expected {expected_count} elements but found {found_count} elements"