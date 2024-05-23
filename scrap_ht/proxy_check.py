import requests

with open('scrap_ht/valid_proxies.txt', 'r') as file:
    proxies = file.read().split('\n')


site_to_check = [
    'http://books.toscrape.com/',
    'https://www.okeydostavka.ru/msk',
    'https://www.okeydostavka.ru/msk/kantseliarskie-tovary-knigi'
]

counter = 0

for site in site_to_check:
    try:
        print(f'Checking {proxies[counter]}')
        res = requests.get(site, proxies={
                                'http': proxies[counter],
                                'https': proxies[counter]
                            })
                                    # timeout=5)
        print(res.status_code, 'status code -=-=-=-=')
    except Exception as e:
        print(e)
    finally:
        counter += 1
        if counter == len(proxies):
            break
