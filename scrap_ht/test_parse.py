import requests
from bs4 import BeautifulSoup


user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0"

proxies = [
    '18.189.21.249:3128',
    '190.61.61.210:999',
    '103.165.125.182:80',
    '45.225.89.145:999',
    '181.119.106.85:8080',
    '45.5.2.246:8084',
    '103.169.255.171:8080',
    '45.236.162.115:3128',
    '188.130.240.136:8080',
    '88.79.243.103:3128',
    '94.182.146.250:8080',
    '182.253.93.4:53281',
    '213.217.30.69:3128',
    '173.21.8.226:3128',
    '131.100.51.212:999',
    '45.166.93.29:999',
    '45.4.201.99:999',
    '103.111.137.241:8080',
    '103.88.90.54:8080',
    '94.228.194.18:41890',
    '159.223.212.216:8080',
    '213.19.123.178:229',
    '136.233.80.157:4480',
    '103.137.160.186:8090',
    '49.13.216.96:3128',
    '210.212.39.138:8080',
    '103.180.126.42:8181',
    '103.133.223.20:8080',
    '140.99.122.244:999',
    '202.4.119.97:5020',
]


def fetch_html(url):
    headers = {'user-agent': user_agent}
    print('fetch_html ---------')
    for proxy in proxies:
        try:
            response = requests.get(url, headers=headers, proxies={'http': proxy, 'https': proxy})
            print('fetch_html 2 ---------')
            if response.status_code == 200:
                print(f"Successfully fetched URL:    {proxy}   ")
                return response.content
            else:
                print(f"Failed to fetch URL: {url}. Status code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred while fetching URL: {url}. Error: {e}")
    return None

def parse_html(html):
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        # Parse the HTML here as needed
        return soup
    else:
        return None

def main():
    print('Start main ---------')
    url = 'https://www.okeydostavka.ru/msk'
    html = fetch_html(url)
    print('html ---------')
    if html:
        parsed_data = parse_html(html)
        print(parsed_data)


if __name__ == "__main__":
    print('Start ---------')
    main()


#
# "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"




'''

/kantseliarskie-tovary-knigi/knigi/khudozhestvennaia-literatura
'''


# _______________________________________________________________________________________
# from selenium import webdriver
# import undetected_chromedriver as uc
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
#
# try:
#     proxy_options = {
#             'proxy': {
#                 'http': '200.174.198.86:8888',
#                 'https': '200.174.198.86:8888'
#             }
#         }
#     options = uc.ChromeOptions()
#     # options.add_argument('--headless')  # Включаем headless-режим
#     options.add_argument('--proxy-server={}'.format(proxy_options['proxy']['https']))
#     options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36")
#     options.add_argument("--disable-blink-features=AutomationControlled")
#
#     driver = webdriver.Chrome(options=options)
#
#     # driver.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')
#     driver.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome')
#
#     time.sleep(10)
#
#     page_source = driver.page_source
#
#     with open('page.html', 'w', encoding='utf-8') as file:
#         file.write(page_source)
#
#
# except Exception as ex:
#     print(ex)
# finally:
#     driver.close()
#     driver.quit()


# _______________________________________________________________________________________













# ____________________________________________________________________________




# from selenium import webdriver
#
# import undetected_chromedriver as uc
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
#
# options = webdriver.ChromeOptions()
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36")
# options.add_argument("--disable-blink-features=AutomationControlled")
#
# driver = webdriver.Chrome(options=options)
#
# try:
#
#     driver.get("https://www.vindecoderz.com/EN/check-lookup/ZDMMADBMXHB001652")
#
#     time.sleep(10)
# except Exception as ex:
#     print(ex)
# finally:
#     driver.close()
#     driver.quit()
#




# try:
#     # Настройка прокси-сервера
#     proxy_options = {
#         'proxy': {
#             'http': '103.173.230.88:8080',
#             'https': '103.173.230.88:8080'
#         }
#     }
#
#     # Настройка браузера
#     options = uc.ChromeOptions()
#     # options.add_argument('--headless')  # Включаем headless-режим
#     options.add_argument('--proxy-server={}'.format(proxy_options['proxy']['https']))
#     options.add_argument('--disable-blink-features=AutomationControlled')  # Отключение автоматической идентификации
#     options.add_argument('user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0')
#
#     driver = uc.Chrome(options=options)
#
#     # Загружаем страницу
#     driver.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')
#     time.sleep(5)
#
#
#     # Получаем HTML-код страницы
#     page_source = driver.page_source
#
#     # Сохраняем HTML-код в текстовый файл
#     with open('page.html', 'w', encoding='utf-8') as file:
#         file.write(page_source)
#
# except Exception as ex:
#     print(ex)
# finally:
#     driver.close()
#     driver.quit()



# ____________________________________________________________________________













# import undetected_chromedriver as uc
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# # Список прокси-серверов
# proxies = [
#     '103.173.230.88:8080',
#     '103.148.192.83:8080',
#     '103.178.43.14:8181',
#     '187.73.188.35:8080',
#     '103.203.172.22:84',
#     '144.21.52.220:3128',
#     '182.253.168.223:8080',
#     '148.72.140.24:30127',
#     '200.174.198.86:8888',
#     '45.61.163.2:80',
#     '41.223.74.16:3128',
#     '117.2.230.64:5402',
#     '103.123.64.234:3128',
#     '36.88.253.86:8080',
#     '101.255.52.163:8080',
#     '188.125.167.200:8080',
#     '210.212.39.138:8080',
#     '103.173.230.88:8080',
#     '119.59.96.112:80',
#     '103.162.16.47:8080',
#     '203.202.252.149:1200',
#     '157.25.92.74:3128',
#     '182.253.178.209:80',
# ]
#
#
# def get_driver_with_proxy(proxy):
#     options = uc.ChromeOptions()
#     # options.add_argument('--headless')  # Включаем headless-режим, если нужно
#     options.add_argument('--proxy-server={}'.format(proxy))
#     options.add_argument('--disable-blink-features=AutomationControlled')
#     options.add_argument('user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0')
#     return uc.Chrome(options=options)
#
#
# for proxy in proxies:
#     try:
#         driver = get_driver_with_proxy(proxy)
#
#         # Загружаем страницу
#         driver.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')
#         time.sleep(5)  # Ждем, чтобы страница полностью загрузилась
#
#         # Получаем HTML-код страницы
#         page_source = driver.page_source
#
#         # Сохраняем HTML-код в текстовый файл
#         with open('page.html', 'w', encoding='utf-8') as file:
#             file.write(page_source)
#
#         print(f"Successfully loaded page using proxy: {proxy}")
#         break  # Выход из цикла, если страница успешно загружена
#
#     except Exception as ex:
#         print(f"Failed to load page using proxy: {proxy}, Error: {ex}")
#
#     finally:
#         driver.close()
#         driver.quit()

# import undetected_chromedriver as uc
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# try:
#     # Настройка прокси-сервера
#     proxy_options = {
#         'proxy': {
#             'http': '103.173.230.88:8080',
#             'https': '103.173.230.88:8080'
#         }
#     }
#
#     # Настройка браузера
#     options = uc.ChromeOptions()
#     # options.add_argument('--headless')  # Включаем headless-режим
#     options.add_argument('--proxy-server={}'.format(proxy_options['proxy']['https']))
#     options.add_argument('--disable-blink-features=AutomationControlled')  # Отключение автоматической идентификации
#     options.add_argument('user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0')
#
#     driver = uc.Chrome(options=options)
#
#     # Загружаем страницу
#     driver.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')
#     time.sleep(5)
#
#
#     # Получаем HTML-код страницы
#     page_source = driver.page_source
#
#     # Сохраняем HTML-код в текстовый файл
#     with open('page.html', 'w', encoding='utf-8') as file:
#         file.write(page_source)
#
# except Exception as ex:
#     print(ex)
# finally:
#     driver.close()
#     driver.quit()

















# import undetected_chromedriver as uc
# from bs4 import BeautifulSoup
# import time
#
# try:
#     # driver = undetected_chromedriver.Chrome()
#
#     proxy_options = {
#         'proxy': {
#             'http': 'http://187.73.188.35:8080',
#             'https': 'https://187.73.188.35:8080'
#         }
#     }
#
#     # Настройка браузера
#     options = uc.ChromeOptions()
#     options.add_argument('--headless')  # Включаем headless-режим
#     options.add_argument('--proxy-server={}'.format(proxy_options['proxy']['http']))
#     driver = uc.Chrome(options=options)
#
#     # Загружаем страницу
#     driver.get('https://bristol.ru/category/138')
#     time.sleep(10)  # Ждем, чтобы страница полностью загрузилась
#
#     # Получаем HTML-код страницы
#     page_source = driver.page_source
#
#     # Инициализируем BeautifulSoup для парсинга
#     # Сохраняем HTML-код в текстовый файл
#     with open('page.html', 'w', encoding='utf-8') as file:
#         file.write(page_source)
#
#
# except Exception as ex:
#     print(ex)
# finally:
#     driver.close()
#     driver.quit()
#
#


# _________________________________________________________________________________

# from selenium.webdriver import Chrome
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from time import sleep
# from bs4 import BeautifulSoup
# from selenium.webdriver import FirefoxOptions
# from selenium.webdriver.common.by import By
#
#
#
#
# from selenium import webdriver
# import time
#
#
# options = webdriver.ChromeOptions()
# options.add_argument("user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'")
# options.add_argument("--disable-blink-features=AutomationControlled")
#
# driver = webdriver.Chrome(options=options)
#
#
#
# try:
#     driver.get('https://samokat.ru/')
#     time.sleep(5)
# except Exception as ex:
#     print(ex)
# finally:
#     driver.close()
#     driver.quit()

# _________________________________________________________________________________



# import requests, time
# from selenium import webdriver
#
# from bs4 import BeautifulSoup as bs
#
#
# chrome_driver_path = ''
#
# options = webdriver.ChromeOptions()
#
# link = 'https://samokat.ru/'
#
#

# driver = webdriver.Chrome(options=options)
#
#
#
#






# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#     'Accept-Language': 'en-US,en;q=0.5'
# }
#
#





# response = requests.get(link, headers=headers, verify=False).text
# soup = bs(response, 'lxml')
#
# print(soup.prettify())
# # print(response)
#
#
