from selenium.webdriver.common.by import By

from huace.book_project.page.base_page import BasePage
from huace.book_project.page.bookshelf_page import BookShelf


class MainPage(BasePage):
    _base_url = "http://novel.hctestedu.com/"

    def goto_detail(self):
        novel = self.find(By.LINK_TEXT, "爱是大雾散尽时")
        novel.click()
        return BookShelf(self._driver)