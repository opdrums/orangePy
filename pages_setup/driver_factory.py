from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import logging
import os

class DriverFactory:
    def __init__(self):
        self.driver = None

    def get_driver(self, browser: str, headless: bool = False):
        if self.driver is None:
            if browser.lower() == "chrome":
                self.driver = self._create_chrome_driver(headless)
            elif browser.lower() == "firefox":
                self.driver = self._create_firefox_driver(headless)
            else:
                raise ValueError(f"Navegador no soportado: {browser}")
        return self.driver

    def _create_chrome_driver(self, headless: bool):
        chrome_options = ChromeOptions()

        # Modo Headless (en CI/CD generalmente es necesario)
        if headless or self._is_ci_environment():
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--no-sandbox")

        # Opciones adicionales de Chrome
        chrome_options.add_argument("--disable-notifications")  # Desactiva notificaciones
        #chrome_options.add_argument("--window-size=1920x1080")
        chrome_options.add_argument("--start-maximized")

        # Iniciar el driver de Chrome con las opciones configuradas
        logging.info("Iniciando el driver de Chrome...")
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=chrome_options
        )
        return driver

    def _create_firefox_driver(self, headless: bool):
        firefox_options = FirefoxOptions()

        # Modo Headless (en CI/CD generalmente es necesario)
        if headless or self._is_ci_environment():
            firefox_options.add_argument("--headless")

        # Opciones adicionales de Firefox
        firefox_options.add_argument("--disable-notifications")  # Desactiva notificaciones

        # Iniciar el driver de Firefox con las opciones configuradas
        logging.info("Iniciando el driver de Firefox...")
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=firefox_options
        )
        return driver

    def quit_driver(self):
        """Cierra el navegador y termina la sesión de WebDriver."""
        if self.driver:
            logging.info("Cerrando el driver...")
            self.driver.quit()
            self.driver = None
        else:
            logging.warning("No se encontró un driver para cerrar.")

    def _is_ci_environment(self):
        """Verifica si el entorno es CI/CD (como GitHub Actions)."""
        return os.environ.get("CI", "false") == "true"
