from selenium.webdriver.common.by import By
from pages_setup.web_base_page import WebBasePage
import  pytest

class Login(WebBasePage):

    # Mapeo de los elementos de la página
    username_field = (By.NAME, "username")
    password_field = (By.NAME, "password")
    login_button = (By.XPATH, "//div[1]/div/div[2]/div[2]/form/div[3]/button")

    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def login(self, username, password):
        self.wait_for_element_visible(By.NAME, "username")
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def validation_logo_web(self):
        self.wait_for_element_visible(By.XPATH, "//div[1]/aside/nav/div[1]/a/div[2]/img")

    def validation_credential_incorrect(self):
        self.wait_for_element_visible(By.XPATH, "//div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p")




