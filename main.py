from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

path = "./chromedriver_mac_64/chromedriver"
driver = webdriver.Chrome()

# website = "https://www.worldometers.info/world-population/population-by-country/"
# driver.get(website)
# driver.implicitly_wait(5)

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
    df.to_csv("Population.csv", index=True)

# main()

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
    df.to_csv("Coronavirus.csv", index=True)       

# coronavirus_page()
def individual_country_page():
    country_data = []
    country_name = driver.find_element(By.TAG_NAME, 'h1')
    #Gets table header for individual country
    table = driver.find_element(By.CLASS_NAME, 'table')
    table_header = table.find_element(By.XPATH, './/thead')
    table_header_elements = table_header.find_elements(By.XPATH, './/tr/th')
    
    for head in table_header_elements:
        country_data.append(head.text)

    table_body = table.find_elements(By.XPATH, './/tbody/tr/td')
    for body in table_body:
        country_data.append(body.text)
    
    df = pd.DataFrame({"Country": country_data})
    df.to_csv(f"{country_name.text}.csv", index=False)

# individual_country_page()

def country_info():
    driver.get('https://www.worldometers.info/world-population/population-by-country/')
    country_links = driver.find_elements(By.XPATH, '//tbody/tr/td/a')
    country_urls = [link.get_attribute('href') for link in country_links]
    for link in country_urls:
        driver.get(link)
        time.sleep(5)
        individual_country_page()
        driver.back()
        time.sleep(5)

country_info()
driver.quit()
