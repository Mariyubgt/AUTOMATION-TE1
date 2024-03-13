import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://demo.dealsdray.com/")
driver.find_element(By.XPATH,'//input[@name="username"]').send_keys("prexo.mis@dealsdray.com")
driver.find_element(By.XPATH,'//input[@name="password"]').send_keys("prexo.mis@dealsdray.com")
driver.find_element(By.XPATH,'//button[@type="submit"]').click()
driver.find_element(By.XPATH,"//span[@class='sidenavHoverShow css-1s178v5']").click()
driver.find_element(By.XPATH,"//span[normalize-space()='Orders']").click()
driver.find_element(By.XPATH,'//button[@xpath="1"]').click()
driver.quit()