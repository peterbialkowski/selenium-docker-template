from selenium import webdriver
import os

REMOTE_DRIVER = os.getenv("REMOTE_DRIVER", "http://127.0.0.1:4444")
print(f"{REMOTE_DRIVER = }")

# >> docker run -d -p 4444:4444 selenium/standalone-chrome

# driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME)
options = webdriver.ChromeOptions()
options.add_argument('--headless')  
with webdriver.Remote(REMOTE_DRIVER, options=options) as driver:
    driver.get("https://merchant.tillpayments.com/login")
    title = driver.title
    print(title)
