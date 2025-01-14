from asyncio import timeout

from pages.driver_factory import DriverFactory
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebBasePage(DriverFactory):
    def __init__(self, driver=None):

        super().__init__()  # Llama al constructor de DriverFactory
        self.driver = driver or self.get_driver("chrome")  # Usa el driver proporcionado o el predeterminado

    def navigate_to(self, url):
        self.driver.get(url)

    def wait_for_element(self, by, value, timeout=10):

        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def wait_for_element_visible(self, by, value, timeout= 10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, value))
        )

    def quit(self):
        self.driver.quit()
