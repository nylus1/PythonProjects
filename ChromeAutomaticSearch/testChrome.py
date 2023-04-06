from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time, pyautogui

driver = webdriver.Chrome()
driver.get("https://www.afrengine.es")
time.sleep(1)

try:
    desplegable=driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/button")
    time.sleep(1)
    desplegable.click()
except:
    print("Unable to find the button to test")


desplegableVehiculo = driver.find_elements(By.XPATH, "/html/body/div[2]/div/form/div[1]/select[1]/option")

print(desplegableVehiculo)

time.sleep(5)

#  Acura MDX 3.5 V6 290hp (2022 -> ...)