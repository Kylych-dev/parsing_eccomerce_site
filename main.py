from typing import Generator
from bs4 import BeautifulSoup as bs
import re, os, click


MAX_LENGTH = 5000


@click.command()
@click.option('--max-length', type=int, default=MAX_LENGTH, help='The maximum length of the message fragment.')
@click.argument('source', type=click.Path(exists=True))
def main_func(source, max_length):
    output_directory = 'output_files'
    base_name = 'sample'
    extension = '.html'

    next_filename = get_next_filename(output_directory, base_name, extension)

    res2 = split_message('input_files/sample.html')
    with open(os.path.join(output_directory, next_filename), 'w', encoding='utf-8') as file:
        for part in res2:
            file.write(part + '\n')


def split_message(source: str, max_length=MAX_LENGTH) -> Generator[str, None, None]:
    """Splits the original message (`source`) into fragments of the specified length
        (`max_len`)."""
    with open(source, 'r', encoding='utf-8') as file:
        html_content = file.read()
        soup = bs(html_content)


def get_next_filename(directory: str, base_name: str, extension: str) -> str:
    """Returns the next available filename in the specified directory."""
    index = 1
    while True:
        filename = '{}_{}{}'.format(base_name, index, extension)
        if not os.path.exists(os.path.join(directory, filename)):
            return filename
        index += 1


if __name__ == '__main__':
    main_func()


