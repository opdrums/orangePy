import pytest
from pages_object_model.module_admin_page import AdminPage

@pytest.fixture(scope="session")
def setup():
    admin_page = AdminPage()
    yield {
        "admin_page": admin_page,
    }

    admin_page.quit()

def test_register_user_admin(setup):
    admin_page = setup["admin_page"]
    admin_page.navigate_to("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    admin_page.login("Admin", "admin123")
    admin_page.click_element_main("Admin")