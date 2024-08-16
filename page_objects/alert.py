from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

class Alert(BasePage):
    ALERT = By.ID, "confirm"



    def confirm_alert(self):
        self.get_element(self.ALERT)
        self.click(self.ALERT)




