import threading
import queue

import requests

queue = queue.Queue()
valid_proxies = []


with open('scrap_ht/proxy_list.txt', 'r') as file:
    proxies = file.read().split('\n')
    for proxy in proxies:
        queue.put(proxy)

def check_proxies():
    """

    """
    global queue
    while not queue.empty():
        proxy = queue.get()
        try:
            res = requests.get('http://ipinfo.io/json',
                               proxies=
                                   {
                                       'http': proxy,
                                       'https': proxy
                                   },
                               timeout=5
                               )
        except:
            continue
        if res.status_code == 200:
            print(proxy)

for _ in range(10):
    threading.Thread(target=check_proxies).start()
