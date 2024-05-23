from typing import Generator
from bs4 import BeautifulSoup as bs
import re, os, click, requests
from selenium import webdriver
from selenium.webdriver import common
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

MAX_LENGTH = 5000


# @click.command()
# @click.argument('source', type=click.Path(exists=True))
def main_func(store_address, categories, pages):
    output_directory = 'output_files'
    base_name = 'sample'
    extension = '.txt'

    next_filename = get_next_filename(output_directory, base_name, extension)
    base_url = 'https://sbermarket.ru/'


    res2 = select_store(base_url, store_address)
    with open(os.path.join(output_directory, next_filename), 'w', encoding='utf-8') as file:
        for part in res2:
            file.write(part + '\n')


def select_store(url, store_address):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    try:
        wait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="store-selector"]'))
        ).click()

        store_input = driver.find_element_by_xpath('//*[@id="store-selector"]')
        store_input.send_keys(store_address)
        driver.find_element(By.XPATH, '//*[@id="select-store-button"]').click()

        current_url = driver.current_url

    finally:
        driver.quit()

    return current_url

def parse_category(url, category, pages):
    products = []

    for page in range(1, pages + 1):
        response = requests.get(f"{url}/{category}?page={page}")
        soup = bs(response.content, 'html.parser')

        for item in soup.select('.product-card'):
            name = item.select('.product-name').text.strip()
            price = item.select('.product-price').text.strip()
            products.append(
                {
                    'name': name,
                    'price': price
                }
            )
    return products



def get_next_filename(directory: str, base_name: str, extension: str) -> str:
    """Returns the next available filename in the specified directory."""
    index = 1
    while True:
        filename = '{}_{}{}'.format(base_name, index, extension)
        if not os.path.exists(os.path.join(directory, filename)):
            return filename
        index += 1


if __name__ == '__main__':
    main_func('https://sbermarket.ru/technopark', 'katalog-elektronika', 'pages')


'''

https://sbermarket.ru/technopark/c/katalog-elektronika/tekhnika-apple-ce25290?sid=25686

'''