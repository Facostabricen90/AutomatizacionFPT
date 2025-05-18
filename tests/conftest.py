import pytest
import ssl
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pages.home_page import HomePage

@pytest.fixture(scope="session")
def browser():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

@pytest.fixture
def home_page(browser):
    return HomePage(browser)
