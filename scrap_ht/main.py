from typing import Generator
from bs4 import BeautifulSoup as bs
import re, os, click, requests
import time, requests


with open('scrap_ht/valid_proxies.txt', 'r') as file:
    proxies = file.read().split('\n')


def select_store(store_address: str, headers: dict, proxy: str) -> str:
    proxy_dict = {
        'http': f'http://{proxy}',
        'https': f'https://{proxy}'
    }
    response = requests.get(url=store_address, proxies=proxy_dict, headers=headers)
    soup = bs(response.text, 'lxml')

    url = 'cool yes!!!'
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

    # proxies = {
    #     # 'http': '102.214.166.1:1976',
    #     'https': 'https://102.214.166.1:1976'
    # }



    working_proxy = None
    for proxy in proxies:
        try:
            print(f'Checkign proxy: {proxy}')
            current_url = select_store(store_address, headers, proxy)
            if current_url:
                working_proxy = proxy
                break
        except requests.exceptions.RequestException as ex:
            print(f'Error with proxies {proxy}: {ex}')
            continue
    if working_proxy is None:
        print('No working proxies found.')
        return

    # current_url = select_store(store_address, headers, proxies[counter])


    products = parse_category(current_url, categories, pages, headers)
    next_filename = get_next_filename(output_directory, base_name, extension)

    # res2 = select_store(store_address)
    with open(os.path.join(output_directory, next_filename), 'w', encoding='utf-8') as file:
        for product in products:
            file.write(product + '\n')

if __name__ == '__main__':
    main_func('https://samokat.ru/', '/category/90b0e15a-208c-4264-ac00-07b9cff26bba/', 'pages')
