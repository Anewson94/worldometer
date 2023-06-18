from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

path = "./chromedriver_mac_64/chromedriver"
driver = webdriver.Chrome()

website = "https://www.worldometers.info/world-population/population-by-country/"
driver.get(website)
driver.implicitly_wait(5)

# countries = []

def main():
    population = []
    rows = driver.find_elements(By.XPATH, "//tbody/tr")
    for row in rows:
        population.append(row.text)
        # country = row.find_element(By.XPATH, "./td").text
        # countries.append(country)
    
    population = [item.split(",") for item in population]
    df = pd.DataFrame({"Population": population})
    df.to_csv("Population.csv")

main()

def coronavirus_page():
    coronavirus_data = []
    coro_page = driver.find_element(By.XPATH, '//*[@id="navbar-main"]/ul/li[1]/a')
    coro_page.click()
    driver.implicitly_wait(5)
    rows = driver.find_elements(By.XPATH, '//tbody/tr')
    for row in rows:
        coronavirus_data.append(row.text) 
    coronavirus_data = [item.split(",") for item in coronavirus_data]
    df = pd.DataFrame({"Coronavirus": coronavirus_data})
    df.to_csv("Coronavirus.csv")       

coronavirus_page()

driver.quit()
