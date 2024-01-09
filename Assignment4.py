# Queens College
# Internet and Web Technology (CSCI 355)
# Winter 2024
# Assignment 4 - Data Scraping, Storage, and Visualization
# Essmer Sanchez
# Worked With Class

# [1] Install and import these third-party libraries which are needed in the tasks below
import requests
import html5lib
from bs4 import BeautifulSoup


#[2] Define a function to print the HTML content of a webpage at a given URL (uniform resource locator, web address)
def print_page_content(url):
    r = requests.get(url)
    print(r.content)


#[3] Define a function to parse the HTML content for a given URL.
def parse_page_content(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    print(soup.prettify())


# [4] Define a function to get the next text item from an iterator
def next_text(itr):
    return next(itr).text

# [5] Define a function to get the next int item from an iterator
def next_int(itr):
    return int(next_text(itr).replace(',', ''))


# [6]Define a function to scrape the site.
def scrape_covid_data(dict_countries_population):
    url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'
    # get URL html
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    data = []
    itr = iter(soup.find_all('td'))
    while True:
        try:
            country = next_text(itr)
            cases = next_int(itr)
            deaths = next_int(itr)
            continent = next_text(itr)
            if country.startswith('Japan'):
                country = 'Japan'
            if country in ['Channel Islands', 'MS Zaandam']:
                continue
            population = dict_countries_population[country]
            data.append([country, population, cases, deaths, continent])
        except StopIteration:
            break

    # Sort the data by the number of deaths
    # data.sort(key=lambda row: row[3], reverse=True)
    return data


# [7] Define a function get_country_population(url) that will scrape this website to get country populations:
# https://www.worldometers.info/world-population/population-by-country/.
# Build a dictionary in which the keys are country names and the values are country populations.
def scrape_population_data():
    url = 'https://www.worldometers.info/world-population/population-by-country/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    itr = iter(soup.find_all('td'))
    dict_countries = {}
    while True:
        try:
            no = next_text(itr)
            country = next_text(itr)
            population = next_int(itr)
            yearly_change = next_text(itr)
            net_change = next_text(itr)
            density = next_text(itr)
            land_area = next_text(itr)
            migrants = next_text(itr)
            fertility = next_text(itr)
            median_age = next_text(itr)
            urban_pop = next_text(itr)
            world_share = next_text(itr)
            dict_countries[country] = population
        except StopIteration:
            break
    return dict_countries

def main():
    # url = 'https://www.google.com'
    # print_page_content(url)
    # parse_page_content(url)
    dict_countries_population = scrape_population_data()
    scrape_covid_data(dict_countries_population)


if __name__ == '__main__':
    main()
