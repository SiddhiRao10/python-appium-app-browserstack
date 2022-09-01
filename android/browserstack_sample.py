from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

desired_cap = {
    # Set your access credentials
    "browserstack.user" : os.environ['BROWSERSTACK_USERNAME'],
    "browserstack.key" : os.environ['BROWSERSTACK_ACCESS_KEY'],

    # Set URL of the application under test
    "app" : os.environ['BROWSERSTACK_APP_URL'],

    # Specify device and os_version for testing
    "device" : "Google Pixel 3",
    "os_version" : "9.0",
    
    # Set other BrowserStack capabilities
    "project" : "First Python project", 
    "build" : "browserstack-build-1",
    "name" : "first_test"
}

# Initialize the remote Webdriver using BrowserStack remote URL
# and desired capabilities defined above
driver = webdriver.Remote(
    command_executor="http://hub-cloud.browserstack.com/wd/hub", 
    desired_capabilities=desired_cap
)
time.sleep(5)
# Test case for the BrowserStack sample Android app. 
# If you have uploaded your app, update the test case here. 
text = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((MobileBy.ID, "com.bitrise_io.sample_apps_android_simple_google_play_deploy:id/textView"))
)

# Invoke driver.quit() after the test is done to indicate that the test is completed.
driver.quit()
