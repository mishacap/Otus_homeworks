from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

class Alert(BasePage):
    ALERT = By.ID, "confirm"



    def check_alert(self):
        self.get_alert(self.ALERT)
        return self




