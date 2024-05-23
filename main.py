from typing import Generator
from bs4 import BeautifulSoup as bs
import re, os, click
from selenium import webdriver

MAX_LENGTH = 5000


# @click.command()
# @click.argument('source', type=click.Path(exists=True))
def main_func(source, store_address, categories, pages):
    output_directory = 'output_files'
    base_name = 'sample'
    extension = '.html'

    next_filename = get_next_filename(output_directory, base_name, extension)
    base_url = 'https://sbermarket.ru/'


    res2 = select_store(base_url, store_address)
    with open(os.path.join(output_directory, next_filename), 'w', encoding='utf-8') as file:
        for part in res2:
            file.write(part + '\n')


def select_store(url, store_address):
    options = webdriver.ChromeOptions()
    pass #TODO


def get_next_filename(directory: str, base_name: str, extension: str) -> str:
    """Returns the next available filename in the specified directory."""
    index = 1
    while True:
        filename = '{}_{}{}'.format(base_name, index, extension)
        if not os.path.exists(os.path.join(directory, filename)):
            return filename
        index += 1


if __name__ == '__main__':
    main_func('input_files', 'output_files', 'categories', 'pages')


