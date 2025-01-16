from pages_object_model.login_page import Login
from selenium.webdriver.common.by import By

class AdminPage(Login):

    main_orange = (By.XPATH, "//div[1]/div[1]/aside/nav/div[2]/ul")

    def click_element_main(self, textMain):
        self.click_element_by_text(self.main_orange, textMain)