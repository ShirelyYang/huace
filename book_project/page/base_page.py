from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    _current_element: WebElement = None
    _base_url = ""

    def __init__(self, driver:WebDriver = None):
        self._driver = ""
        if self._driver is None:
            self._driver = webdriver.Chrome()
        else:
            self._driver = driver
        if self._base_url == "":
            self._driver.get(self._base_url)
        self._driver.maximize_window()
        self.implicitly_wait(3)

    def find(self, by, locator):
        self._current_element = self._driver.find_element(by, locator)
        return self._current_element

    def click(self):
        self._current_element.click()
        return self

    def base_quit(self):
        self._driver.quit()