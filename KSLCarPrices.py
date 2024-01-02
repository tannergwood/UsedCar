from selenium import webdriver
from selenium.webdriver.common.by import By
import fnmatch


carlistings = []

for i in range(1,11):
    driver = webdriver.Chrome()
    url = f"https://cars.ksl.com/sitemap/srp-used?page={i}"
    driver.get(url)
    links = driver.find_elements(By.CLASS_NAME, "opened")
    for link in links:
        carlistings.append(link.text[5:-37])
    driver.quit()

listings = fnmatch.filter(carlistings, "https://cars.ksl.com/listing/???????")

# I Want to loop through this list of car listings, click on see more for the vehicle specs
# grab the info, and load it into a dataframe
