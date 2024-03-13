from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


options = webdriver.FirefoxOptions()
options.add_argument('__headless')
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://www.getcalley.com/page-sitemap.xml")
driver.get("https://www.getcalley.com/")
driver.set_window_size(1920, 1080)
driver.get_screenshot_as_file("selenium1.png")

driver.get("https://www.getcalley.com/calley-call-from-browser/")
driver.set_window_size(1366, 768)
driver.get_screenshot_as_file("selenium2.png")

driver.get("https://www.getcalley.com/calley-pro-features/")
driver.set_window_size(1536, 864)
driver.get_screenshot_as_file("selenium3.png")

driver.get("https://www.getcalley.com/how-calley-auto-dialer-app-works/")
driver.get_screenshot_as_file("selenium4.png")

driver.get("https://www.getcalley.com/calley-zoho-crm-integration/")
driver.get_screenshot_as_file("selenium5.png")
driver.quit()