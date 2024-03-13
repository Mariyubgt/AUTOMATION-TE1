from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Safari()
driver.implicitly_wait(10)
driver.get("https://www.getcalley.com/page-sitemap.xml")
driver.get("https://www.getcalley.com/")
driver.get_screenshot_as_file("selenium1.png")
driver.get("https://www.getcalley.com/calley-call-from-browser/")
driver.get_screenshot_as_file("selenium2.png")
driver.get("https://www.getcalley.com/calley-pro-features/")
driver.get_screenshot_as_file("selenium3.png")
driver.get("https://www.getcalley.com/how-calley-auto-dialer-app-works/")
driver.get_screenshot_as_file("selenium4.png")
driver.get("https://www.getcalley.com/calley-zoho-crm-integration/")
driver.get_screenshot_as_file("selenium5.png")
driver.quit()
print(driver.title)
driver.quit()