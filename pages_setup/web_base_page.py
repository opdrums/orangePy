from pages_setup.driver_factory import DriverFactory
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class WebBasePage(DriverFactory):
    def __init__(self, driver =None):
        super().__init__()
        self.driver = driver

    def navigate_to(self, url):
        self.get_driver("chrome")
        self.driver.get(url)

    def wait_for_element(self, by, value, timeout=10):

        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def wait_for_element_visible(self, by, value, timeout= 10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, value))
        )
        assert element.is_displayed()

    def click_element_by_text(self,  elements_locator, text_to_find):

        elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(elements_locator)
        )

        for element in elements:
            element_text_parts = element.text.split('\n')
            for indice in element_text_parts:
                if indice in text_to_find:
                    span_element = self.driver.find_element(By.XPATH, f"//span[text()='{indice}']")
                    span_element.click()
                    return
            raise ValueError(f"El texto '{text_to_find}' no se encontró en los elementos")

    def quit(self):
        self.driver.quit()
