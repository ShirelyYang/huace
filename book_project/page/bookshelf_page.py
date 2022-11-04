from selenium.webdriver.common.by import By

from huace.book_project.page.base_page import BasePage


class BookShelf(BasePage):
    # def add_shelf(self):
    #     self.find(By.LINK_TEXT, "加入书架").click()

    def get_shelf_list(self):
        self.find(By.CSS_SELECTOR, "a.sj_link").click()
        lis = self.find(By.CSS_SELECTOR, "*.book_list")
        print(lis)

    # def login(self):
    #     self.find(By.XPATH, "\\input[@name='txtUName']").send_keys("13588888888")
    #     self.find(By.XPATH, "\\input[@name='txtPassword']").send_keys("12345")
    #     self.find(By.XPATH, "\\input[@name='btnLogin']").click()