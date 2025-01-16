import pytest
from pages_object_model.login_page import Login

@pytest.fixture(scope="function")
def setup():
    login_page = Login()
    yield {
        "login_page": login_page,
    }

    login_page.quit()

def test_valid_login(setup):
    login_page = setup["login_page"]
    login_page.navigate_to("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page.login("Admin", "admin123")
    login_page.validate_element_visible("//div[1]/aside[1]/nav[1]/div[1]/a[1]/div[2]/img[1]")

def test_invalid_credentials(setup):
    login_page = setup["login_page"]
    login_page.navigate_to("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page.login("Admin", "admin1235")