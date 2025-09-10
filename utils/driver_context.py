"""
Driver context manager for managing WebDriver instances globally.

This module provides a way to store and access the current WebDriver instance
without needing to pass it as a parameter to every function.
"""

from selenium.webdriver.remote.webdriver import WebDriver
from typing import Optional


class DriverContext:
    """
    Global context manager for WebDriver instances.
    
    This class provides a singleton pattern to store and access the current
    WebDriver instance throughout the application without needing to pass
    it as a parameter to every function.
    """
    
    _instance: Optional['DriverContext'] = None
    _driver: Optional[WebDriver] = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def set_driver(self, driver: WebDriver) -> None:
        """
        Set the current WebDriver instance.
        
        Args:
            driver: The WebDriver instance to store
        """
        self._driver = driver
    
    def get_driver(self) -> WebDriver:
        """
        Get the current WebDriver instance.
        
        Returns:
            The current WebDriver instance
            
        Raises:
            RuntimeError: If no driver has been set
        """
        if self._driver is None:
            raise RuntimeError("No driver has been set. Call set_driver() first.")
        return self._driver
    
    def clear_driver(self) -> None:
        """Clear the current WebDriver instance."""
        self._driver = None
    
    def has_driver(self) -> bool:
        """
        Check if a driver is currently set.
        
        Returns:
            True if a driver is set, False otherwise
        """
        return self._driver is not None


# Global instance for easy access
driver_context = DriverContext()
