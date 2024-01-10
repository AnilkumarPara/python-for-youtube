from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


def get_by_type(locator_type):
    if locator_type.lower() == 'id':
        return By.ID
    elif locator_type.lower() == 'xpath':
        return By.XPATH
    elif locator_type.lower() == 'name':
        return By.NAME
    elif locator_type.lower() == 'css_selector':
        return By.CSS_SELECTOR
    print("Invalid locator")
    return False


class ElementInteractions:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator=None, value=None):
        element = None

        ele_type = get_by_type(locator)
        element = self.driver.find_element(ele_type, value)
        if element is not None:
            print("Element is found")
            return element
        else:
            print("Element is not found")

    def is_element_present(self, locator, value):
        try:
            element = self.driver.find_element(locator, value)
            if element is not None:
                print("Element is found")
                return True
            else:
                print("Element is not found")
                return False
        except NoSuchElementException:
            print("Element is not found")
            return False
