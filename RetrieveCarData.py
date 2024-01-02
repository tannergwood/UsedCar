from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'https://cars.ksl.com/listing/8753814'
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(2)
driver.execute_script("window.scrollTo(0, window.innerHeight / 2);")
driver.implicitly_wait(2)
SeeMore = driver.find_element(By.XPATH, ".//button[text()='See More']")
#SeeMore = driver.find_element(By.CLASS_NAME, "")
SeeMore.click()
driver.implicitly_wait(2)
mileage = driver.find_element(By.CLASS_NAME, "MuiGrid-root.jss143.label.MuiGrid-item.MuiGrid-grid-m-6").text
print(mileage)
driver.quit()

# try:
#     seeMore = driver.find_element(By.CLASS_NAME, "Button__StyledButton-hsu6mt-0.Button__StyledGhostButton-hsu6mt-2.irwPbm.dnigEV.seeMore")
#     seeMore.click()
#     extColor = driver.find_element(By.CLASS_NAME, "Typography__variantProp-sc-5cwz35-0.kMOSqH").text
#     print(extColor)
# finally:
#     driver.quit()
#     print("Whoa")


