import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options,
                               executable_path="../../chromedriver/chromedriver")
    browser.implicitly_wait(1)  # ждем 1 сек
    yield browser
    print("\nquit browser..")
    time.sleep(30)
    browser.quit()

