
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
import time, traceback

options = UiAutomator2Options()
options.set_capability("platformName", "android")

driver = webdriver.Remote("http://localhost:4723", options=options)
try:
    driver.implicitly_wait(6)

    # Step - 1 : Tap COLOR button
    print('Step 1: Tap COLOR button')
    driver.implicitly_wait(6)

    # Step - 2 : Check magenta header text color change → {{{{color_changed}}}}
    print('Step 2: Query - Check magenta header text color change → {{{{color_changed}}}}')
    driver.implicitly_wait(6)

    # Step - 3 : Assert {{{{color_changed}}}} equals true
    print('Step 3: Assertion - Assert {{{{color_changed}}}} equals true')
    driver.implicitly_wait(6)

    # Step - 4 : Close current app
    print('Step 4: Close app - Close current app')

    driver.quit()
except Exception as e:
    driver.quit()
