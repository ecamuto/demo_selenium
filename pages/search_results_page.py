from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchResultsPage(BasePage):
    SEARCH_RESULTS = (By.CLASS_NAME, "list-recent-events")

    def has_results(self):
        results = self.find_elements(self.SEARCH_RESULTS)
        return len(results) > 0

