import pytest
import time
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path='./chromedriver')
    driver.implicitly_wait(5)
    yield driver
    time.sleep(1)
    driver.quit()
