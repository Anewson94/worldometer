from selenium import webdriver

path = "./chromedriver_mac_64/chromedriver"
driver = webdriver.Chrome()

website = "https://www.worldometers.info/world-population/population-by-country/"
driver.get(website)
