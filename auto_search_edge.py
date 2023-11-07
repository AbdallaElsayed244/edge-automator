from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pickle

# Start the browser and visit the website
browser = webdriver.Edge()
browser.get('https://www.bing.com')

# Assuming 'element' is the locator of the element to be located
element = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, "element"))
)

# Load cookies
cookies = pickle.load(open("cookie.pkl", "rb"))
for cookie in cookies:
    browser.add_cookie(cookie)

# Perform searches
tab = range(31, 91)
for x in tab:
    term = f"quote of the day {x}"
    print(term)
    browser.execute_script(f"window.open('https://www.bing.com/search?q={term}');")

# Keep the browser open to observe the searches
input("Press Enter to close the browser...")
browser.quit()  # Close the browser when the user presses Enter