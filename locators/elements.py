import os

class Elements:

    username = os.getenv('USERNAME')

    # INPUT-------------------------------------------------------------------------------------------------------------

    @staticmethod
    def input_via_id(path_id):
        path = f"//input[contains(@id,'{path_id}')]"

        return path

    @staticmethod
    def input_via_placeholder(path_id):
        path = f"//input[contains(@placeholder,'{path_id}')]"

        return path

    # BUTTON------------------------------------------------------------------------------------------------------------

    @staticmethod
    def button_via_id(path_id):
        path = f"//button[contains(@id,'{path_id}')]"
        return path

    def button_submit(self):
        path = self.button_via_id("btn-submit")
        return path

    # SELECT------------------------------------------------------------------------------------------------------------

    @staticmethod
    def select_via_id(path_id):
        path = f"//select[contains(@id,'{path_id}')]"
        return path

    # OPTION------------------------------------------------------------------------------------------------------------

    @staticmethod
    def option_via_text(path_text):
        path = f"//option[contains(.,'{path_text}')]"
        return path

    # DIV---------------------------------------------------------------------------------------------------------------

    @staticmethod
    def div_via_class(path_class):
        path = f"//div[contains(@class,'{path_class}')]"
        return path

    def div_alert_success(self):
        path = self.div_via_class("alert alert-success")
        return path

    def div_alert_danger(self):
        path = self.div_via_class("alert alert-danger")
        return path
