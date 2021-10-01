from selenium import webdriver
import pytest


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(60)
    yield driver
    driver.quit()
