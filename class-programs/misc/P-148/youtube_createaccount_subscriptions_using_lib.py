# Install the Selenium
from selenium import webdriver
import time
from lib.element_interactions import ElementInteractions
import pytest


class TestYouTube:
    def test_youtube_sign_in_path(self):
        cdriver = webdriver.Chrome()
        cdriver.get("https://www.youtube.com/")
        cdriver.maximize_window()
        cdriver.implicitly_wait(5)
        ei = ElementInteractions(driver=cdriver)
        sub_xpath = ei.get_element('xpath', "//div[@id='items']//ytd-guide-entry-renderer//a["
                                            "@href='/feed/subscriptions']")
        assert sub_xpath
        sub_xpath.click()
        time.sleep(2)
        sign_xpath = ei.get_element('xpath', "//div[@id='contents']//a[@aria-label='Sign in']")
        assert sign_xpath
        sign_xpath.click()
        time.sleep(2)
        c_a_xpath = ei.get_element('xpath', "//div[@class='XOrBD']//button[contains(@class,'VfPpkd-LgbsSe')]")
        assert c_a_xpath
        c_a_xpath.click()
        time.sleep(2)
        cdriver.quit()
