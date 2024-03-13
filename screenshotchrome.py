import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import os

chrome_options = Options()
chrome_options.add_experimental_option('detach',True)
options = webdriver.ChromeOptions()
options.add_argument('__headless')
browser = webdriver.Chrome(options=chrome_options)

now = datetime.now()
current_time = now.strftime("%H_%M_%S")

browser.get("https://www.getcalley.com/page-sitemap.xml")
browser.get("https://www.getcalley.com/")

browser.set_window_size(1920, 1080)
browser.save_screenshot(os.getcwd()+'/screen1/Screenshot_'+current_time+'.png')

browser.get("https://www.getcalley.com/calley-call-from-browser/")
browser.set_window_size(1366, 768)
browser.get_screenshot_as_file("selenium2.png")

browser.get("https://www.getcalley.com/calley-pro-features/")
browser.set_window_size(1536, 864)
browser.get_screenshot_as_file("selenium3.png")

browser.get("https://www.getcalley.com/how-calley-auto-dialer-app-works/")
browser.get_screenshot_as_file("selenium4.png")

browser.get("https://www.getcalley.com/calley-zoho-crm-integration/")
browser.get_screenshot_as_file("selenium5.png")
browser.quit()