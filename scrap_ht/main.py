from typing import Generator
from bs4 import BeautifulSoup as bs
import re, os, click, requests


with open('scrap_ht/valid_proxies.txt', 'r') as file:
    proxies = file.read().split('\n')


def select_store(store_address: str, headers: dict) -> str:
    response = requests.get(url=store_address, headers=headers, verify=False)
    if response.status_code == 200:
        print('ok select store')
        soup = bs(response.text, 'html.parser')
        return store_address
    else:
        print('Error in selecting store. Please check the URL and try again.')
        return None


def parse_category(url:str, category, headers) -> list:
    products = []
    full_url = f'{url}/{category}'
    response = requests.get(full_url, headers=headers, verify=False)
    print('response is work -=-=-==-=-=--=-=-=--=')
    if response.status_code == 200:
        # response = requests.get(f"{url}/{category}?page={page}", headers=headers)
        soup = bs(response.content, 'html.parser')
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
def main_func(store_address, category=''):
    output_directory = 'output_files'
    base_name = 'sample'
    extension = '.txt'
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    current_url = select_store(store_address, headers)

    # if pages is not None:
    #     products = parse_category(current_url, category, pages, headers)
    # else:
    products = parse_category(current_url, category, headers)
    # products = parse_category(current_url, categories, pages, headers)
    next_filename = get_next_filename(output_directory, base_name, extension)

    # with open(os.path.join(output_directory, next_filename), 'w', encoding='utf-8') as file:
    #     for product in products:
    #         file.write(product + '\n')


if __name__ == '__main__':
    base_url = 'https://samokat.ru'
    category = 'category/90b0e15a-208c-4264-ac00-07b9cff26bba'      # Ваша категория товаров
    # pages = 3   # Количество страниц для парсинга
    # min_price = 69.99  # Минимальная цена
    # max_price = 4499.0  # Максимальная цена
    # page_size = 72  # Количество продуктов на странице

    main_func(base_url, category)



'''

https://www.okeydostavka.ru/msk/kantseliarskie-tovary-knigi/knigi/khudozhestvennaia-literatura


https://www.okeydostavka.ru/msk/kantseliarskie-tovary-knigi/knigi/khudozhestvennaia-literatura

#facet:&productBeginIndex:72&orderBy:2&pageView:grid&minPrice:69.99&maxPrice:4499.0&pageSize:72&



https://www.okeydostavka.ru/msk/kantseliarskie-tovary-knigi/knigi/khudozhestvennaia-literatura

'''