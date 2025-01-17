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
    login_page.validation_logo_web()

def test_invalid_credentials(setup):
    login_page = setup["login_page"]
    login_page.navigate_to("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page.login("Admin", "admin1235")
    login_page.validation_credential_incorrect()
