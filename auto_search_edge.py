from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import time  # Import the time module

# Start the browser and visit the website
browser = webdriver.Edge()
browser.get('https://www.bing.com')

# Wait for the specific element to be present on the page


# Load cookies
cookies = pickle.load(open("cookie.pkl", "rb"))
for cookie in cookies:
    browser.add_cookie(cookie)

# Add a delay to allow the browser to load the cookies
time.sleep(5)  # Adjust the delay as needed

# Perform searches
tab = range(31, 91)
for x in tab:
    term = f"quote of the day {x}"
    print(term)
    browser.execute_script(f"window.open('https://www.bing.com/search?q={term}');")

# Keep the browser open to observe the searches
input("Press Enter to close the browser...")
browser.quit()  # Close the browser when the user presses Enter