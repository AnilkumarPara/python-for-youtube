from selenium import webdriver
from selenium.webdriver.common.by import By

cdriver = webdriver.Chrome()
cdriver.maximize_window()
cdriver.get("https://www.youtube.com/")
cdriver.implicitly_wait(6)
sub_xpath = cdriver.find_element(By.XPATH, "//div[@id='items']//ytd-guide-entry-renderer//a[@href='/feed/subscriptions']")
if sub_xpath is not None:
    print("Subscription element is found")

