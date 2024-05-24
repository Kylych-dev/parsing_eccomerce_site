from typing import Generator
from bs4 import BeautifulSoup as bs
import re, os, click, requests
import time, requests

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0'
}

proxies = {
    'http': '102.214.166.1:1976',
    'https': '102.214.166.1:1976'
}

BASE_URL = 'https://www.okeydostavka.ru/msk'

url = BASE_URL + '/kantseliarskie-tovary-knigi'



def proxy_request(url):
    payload = {
        'source': 'universal',
        'url': url,
        'geo_location': 'Germany'
    }

    response = requests.request(
        # 'POST'm
    )



def get_location(url):
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    ip = soup.find('div', class_='ip').text.strip()

    print(ip)



def main():
    get_location(url='https://2ip.ru/')


BASE_URL = 'https://www.okeydostavka.ru/msk'

url = BASE_URL + '/kantseliarskie-tovary-knigi'

response

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
    soup = bs(requests.get(url, headers=headers).content, 'lxml')


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
