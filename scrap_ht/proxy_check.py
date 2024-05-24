import requests


user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0"


with open('scrap_ht/valid_proxies.txt', 'r') as file:
    proxies = file.read().split('\n')


site_to_check = [
    # 'http://books.toscrape.com/',
    # 'https://www.okeydostavka.ru/msk',
    'https://sbermarket.ru/'
    # 'https://www.okeydostavka.ru/msk/kantseliarskie-tovary-knigi'
]

counter = 0

for site in site_to_check:
    try:
        print(f'Checking {proxies[counter]}')
        res = requests.get(site, proxies={
                                'http': proxies[counter],
                                'https': proxies[counter]
                                # 'https': '203.189.88.156:80'

        },
                           )
                                # timeout=5)
        print(res.status_code, f'status code -=-=-=-=   {proxies}   site: {site}')
    except requests.exceptions.ProxyError as e:
        print(f'ProxyError for proxies {proxies}: {e}')
    except requests.exceptions.ConnectionError as e:
        print(f'ConnectionError for proxies {proxies}: {e}')
    except requests.exceptions.Timeout as e:
        print(f'TimeoutError for proxies {proxies}: {e}')
    except Exception as e:
        print(f'An error occurred for proxies {proxies}: {e}')

    # except Exception as e:
    #     print(e)
    # finally:
    #     counter += 1
    #     if counter == len(proxies):
    #         break




'''

complete Java code that supports both HTTP and HTTPS requests using SOCKS proxy.
'''