
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from soft_assert import SoftAssert
import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TestPythonOrg:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.soft_assert = SoftAssert()
        logging.info("WebDriver initialized")

    def setup(self):
        self.driver.get("https://www.python.org")
        logging.info("Navigated to Python.org")

    def teardown(self):
        self.driver.quit()
        logging.info("WebDriver closed")


    def test_homepage_with_search(self):
        home_page = HomePage(self.driver)
        search_page = SearchResultsPage(self.driver)

        # Find the search box element
        search_box = self.driver.find_element(By.NAME, "q")
        # Type "selenium" into the search box
        search_box.send_keys("selenium")
        # Press Enter
        search_box.send_keys(Keys.RETURN)
        search_page.has_results()
        self.driver.get("https://www.python.org")



    def test_homepage_with_soft_asserts(self):
        home_page = HomePage(self.driver)

        # Title assertion
        self.soft_assert.assert_equal(home_page.get_title(), "Welcome to Python.org", "Homepage title is incorrect")
        
        # Navigation menu assertion
        menu_items = home_page.get_navigation_menu_items()
        expected_menu_items = ["About", "Downloads", "Documentation", "Community", "Success Stories", "News", "Events"]
        self.soft_assert.assert_equal(menu_items, expected_menu_items, "Navigation menu items do not match expected")
        
        # News/Events items assertion
        news_items = home_page.get_latest_news_items()
        self.soft_assert.assert_true(len(news_items) > 0, "No news items found")
        self.soft_assert.assert_true(len(news_items) < 11, "Too many news/events items displayed")
        
        # Download button assertion
        home_page.click_downloads()
        time.sleep(2)

        download_button = home_page.get_download_button()
        self.soft_assert.assert_true(download_button.is_displayed(), "Download button is not visible")
        self.soft_assert.assert_in("Download Python", download_button.text, "Unexpected download button text")
        # Check all soft assertions
        self.soft_assert.assert_all()
        logging.info("All homepage tests passed")



def run_tests():
    test_instance = TestPythonOrg()
    test_methods = [method for method in dir(TestPythonOrg) if method.startswith('test_')]
    results = {'passed': 0, 'failed': 0}

    for method_name in test_methods:
        test_method = getattr(test_instance, method_name)
        test_instance.setup()
        try:
            test_method()
            print(f"✅ {method_name} passed")
            results['passed'] += 1
        except AssertionError as e:
            print(f"❌ {method_name} failed:")
            print(str(e))
            results['failed'] += 1
        except Exception as e:
            print(f"❌ {method_name} failed with an unexpected error: {str(e)}")
            results['failed'] += 1
        finally:
            print("ecco il finally")
            
    test_instance.teardown()

    print(f"\nTest Summary:")
    print(f"Passed: {results['passed']}")
    print(f"Failed: {results['failed']}")
    print(f"Total: {results['passed'] + results['failed']}")

    return results['failed'] == 0

if __name__ == "__main__":
    run_tests()

# The HomePage class remains the same as in the previous example
