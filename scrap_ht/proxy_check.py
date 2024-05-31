import requests


user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0"


with open('scrap_ht/valid_proxies.txt', 'r') as file:
    proxies = file.read().split('\n')


site_to_check = [
    # 'http://books.toscrape.com/',
    # 'https://www.okeydostavka.ru/msk',
    # 'https://sbermarket.ru/',
    # 'https://samokat.ru/',

    'https://samokat.ru/category/90b0e15a-208c-4264-ac00-07b9cff26bba'
    # 'https://www.okeydostavka.ru/msk/kantseliarskie-tovary-knigi'
]

counter = 0

print(proxies[counter], '-=-=--=-=-=-=-=--=-=-=-=')

for site in site_to_check:
    try:
        print(f'Checking {proxies[counter]}')
        res = requests.get(site,
                           proxies={
                                'http': proxies[counter],
                                'https': proxies[counter]
                           },
                           verify=False,
                           )

        print(res.status_code, f'status code -=-=-=-=   {proxies}   site: {site}')
    except requests.exceptions.ProxyError as ex:
        print(f'ProxyError for proxies {proxies}: {ex}')
    except requests.exceptions.ConnectionError as ex:
        print(f'ConnectionError for proxies {proxies}: {ex}')
    except requests.exceptions.Timeout as ex:
        print(f'TimeoutError for proxies {proxies}: {ex}')
    except Exception as ex:
        print(f'An error occurred for proxies {proxies}: {ex}')

    # except Exception as ex:
    #     print(ex)
    # finally:
    #     counter += 1
    #     if counter == len(proxies):
    #         break




'''

complete Java code that supports both HTTP and HTTPS requests using SOCKS proxy.

chrome-extension://bgpmiljelfnilfcfmoppijdkmccbccel/isolated-first.jst
'''