import os

class Elements:
    """
    A utility class for generating XPath locators for web elements.
    
    This class provides static methods to create XPath expressions for various
    HTML elements like inputs, buttons, selects, options, and divs. It uses
    flexible matching strategies (contains) to make locators more robust.
    
    Index:
        Search for 'INPUT-' - for input functions
        Search for 'BUTTON-' - for button functions  
        Search for 'SELECT-' - for select functions
        Search for 'OPTION-' - for option functions
        Search for 'DIV-' - for div functions
    """

    username = os.getenv('USERNAME')

    # INPUT-------------------------------------------------------------------------------------------------------------

    @staticmethod
    def input_via_id(path_id):
        """
        Generate XPath locator for input element by ID.
        
        Args:
            path_id (str): The ID or partial ID of the input element
            
        Returns:
            str: XPath expression to locate the input element
        """
        path = f"//input[contains(@id,'{path_id}')]"

        return path

    @staticmethod
    def input_via_placeholder(path_id):
        """
        Generate XPath locator for input element by placeholder text.
        
        Args:
            path_id (str): The placeholder text or partial placeholder text
            
        Returns:
            str: XPath expression to locate the input element
        """
        path = f"//input[contains(@placeholder,'{path_id}')]"

        return path

    # BUTTON------------------------------------------------------------------------------------------------------------

    @staticmethod
    def button_via_id(path_id):
        """
        Generate XPath locator for button element by ID.
        
        Args:
            path_id (str): The ID or partial ID of the button element
            
        Returns:
            str: XPath expression to locate the button element
        """
        path = f"//button[contains(@id,'{path_id}')]"
        return path

    def button_submit(self):
        """
        Generate XPath locator for submit button.
        
        Returns:
            str: XPath expression to locate the submit button with ID 'btn-submit'
        """
        path = self.button_via_id("btn-submit")
        return path

    # SELECT------------------------------------------------------------------------------------------------------------

    @staticmethod
    def select_via_id(path_id):
        """
        Generate XPath locator for select element by ID.
        
        Args:
            path_id (str): The ID or partial ID of the select element
            
        Returns:
            str: XPath expression to locate the select element
        """
        path = f"//select[contains(@id,'{path_id}')]"
        return path

    # OPTION------------------------------------------------------------------------------------------------------------

    @staticmethod
    def option_via_text(path_text=None):
        """
        Generate XPath locator for option element by text content.
        
        Args:
            path_text (str): The text content or partial text of the option element
            
        Returns:
            str: XPath expression to locate the option element
        """
        path = f"//option"
        if path_text:
            path += f"[contains(.,'{path_text}')]"

        return path

    # DIV---------------------------------------------------------------------------------------------------------------

    @staticmethod
    def div_via_class(path_class):
        """
        Generate XPath locator for div element by class name.
        
        Args:
            path_class (str): The class name or partial class name of the div element
            
        Returns:
            str: XPath expression to locate the div element
        """
        path = f"//div[contains(@class,'{path_class}')]"
        return path

    def div_alert_success(self):
        """
        Generate XPath locator for success alert div.
        
        Returns:
            str: XPath expression to locate the div with 'alert alert-success' class
        """
        path = self.div_via_class("alert alert-success")
        return path

    def div_alert_danger(self):
        """
        Generate XPath locator for danger alert div.
        
        Returns:
            str: XPath expression to locate the div with 'alert alert-danger' class
        """
        path = self.div_via_class("alert alert-danger")
        return path
