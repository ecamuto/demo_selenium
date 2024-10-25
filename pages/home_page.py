from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from pages.search_results_page import SearchResultsPage
import logging

class HomePage(BasePage):
    URL = "https://www.python.org"
    SEARCH_INPUT = (By.ID, "id-search-field")
    NAVIGATION_MENU = (By.CSS_SELECTOR, "ul.navigation[role='menubar'] li[aria-haspopup='true']")
    NEWS_EVENTS_ITEMS = (By.CSS_SELECTOR, ".list-widgets.row  li")
    DOWNLOAD_BUTTON = (By.XPATH, "//div[@class='download-for-current-os']/div[not(contains(@style, 'display: none'))]//a")
    DOWNLOADS_ITEM = (By.ID, "downloads")

    def search_for(self, term):
        search_input = self.find_element(self.SEARCH_INPUT)
        search_input.send_keys(term + Keys.RETURN)
        return SearchResultsPage(self.driver)

    def get_navigation_menu_items(self):
        menu_items = self.find_elements(self.NAVIGATION_MENU)
        return [item.text for item in menu_items]

    def get_latest_news_items(self):
        return self.find_elements(self.NEWS_EVENTS_ITEMS)

    def click_downloads(self):
        try:
            download_item = self.find_element(self.DOWNLOADS_ITEM)
            download_item.click()
        except Exception as e:
            logging.error(f"Failed to click downloads menu item: {str(e)}")
 
    def get_download_button(self):
        try:
            return self.find_element_visible(self.DOWNLOAD_BUTTON)
        except Exception as e:
            logging.error(f"Failed to find download button: {str(e)}")
            logging.info("Current URL: %s", self.driver.current_url)
            logging.info("Page source: %s", self.driver.page_source)
            raise