from typing import Generator
from bs4 import BeautifulSoup as bs
import re, os, click, requests
import time, requests


def select_store(url: str, headers: dict, proxies: dict) -> str:
    response = requests.get(url=url, proxies=proxies, headers=headers)
    soup = bs(response.text, 'lxml')
    return url

def parse_category(url:str, category:str, pages:int, headers:dict) -> list:
    products = []
    for page in range(1, pages + 1):

        response = requests.get(f"{url}/{category}?page={page}", headers=headers)
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
        filename = f'{base_name}_{index}{extension}'
        if not os.path.exists(os.path.join(directory, filename)):
            return filename
        index += 1

# @click.command()
# @click.argument('source', type=click.Path(exists=True))
def main_func(store_address, categories, pages):
    output_directory = 'output_files'
    base_name = 'sample'
    extension = '.txt'

    """Selects a store and returns the current URL."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0'
    }
    proxies = {
        'http': '102.214.166.1:1976',
        'https': '102.214.166.1:1976'
    }


    next_filename = get_next_filename(output_directory, base_name, extension)

    res2 = select_store(store_address)
    with open(os.path.join(output_directory, next_filename), 'w', encoding='utf-8') as file:
        for part in res2:
            file.write(part + '\n')

if __name__ == '__main__':
    main_func('https://www.okeydostavka.ru/msk', '/kantseliarskie-tovary-knigi', 'pages')
