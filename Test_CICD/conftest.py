import pytest
from selenium import webdriver
from selenium.webdriver.chrome import service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(autouse=True)
def setup(request):
    print('test start')
    yield
    print('test end')
