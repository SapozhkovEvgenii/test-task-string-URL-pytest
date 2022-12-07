import json
import os
from concurrent.futures import ThreadPoolExecutor

import requests
import validators


strings = [
    'https://google.by', 'https://yandex.ru',
    'https://youtube.com', 'fjkdfhdk', 'https://stackoverflow.com',
    'htt://docs-python.ru/', 'https://facebook.com', 'https://habr.com',
    'https://django.fun', 'https://pythontic.com', 'https://github.com',
    'https://python-dependency-injector.ets-labs.org/introduction/index.html'
]


def check_url(*urls):
    """ check if all strings to be passed are urls """
    if not urls:
        print("No data to check")
        return None
    checked_strings = set()
    for url in urls:
        if not validators.url(url):  # type: ignore
            print(f'String "{url}" is not url')
        else:
            checked_strings.add(url)
    return checked_strings


def get_method_codes(url):
    with requests.Session() as session:
        result = {url: {}}
        response_get = session.get(url)
        if response_get.status_code != 405:
            result[url]['GET'] = response_get.status_code
        response_post = session.post(url)
        if response_post.status_code != 405:
            result[url]['POST'] = response_post.status_code
        response_put = session.put(url)
        if response_put.status_code != 405:
            result[url]['PUT'] = response_put.status_code
        response_delete = session.delete(url)
        if response_delete.status_code != 405:
            result[url]['DELETE'] = response_delete.status_code
        response_options = session.options(url)
        if response_options.status_code != 405:
            result[url]['OPTIONS'] = response_options.status_code
        response_head = session.head(url)
        if response_head.status_code != 405:
            result[url]['HEAD'] = response_head.status_code
        response_patch = session.patch(url)
        if response_patch.status_code != 405:
            result[url]['PATCH'] = response_patch.status_code
        return result


def work():
    urls = check_url(*strings)
    if urls:
        count_core_of_processor = os.cpu_count()
        lenght_urls = len(urls)
        count_workers = (len(urls) if lenght_urls <= count_core_of_processor  #type: ignore
                        else count_core_of_processor * 2)  #type: ignore
        with ThreadPoolExecutor(max_workers=count_workers) as executor:
            res = executor.map(get_method_codes, urls)
            result_dict = {key: val for elem in res for key, val in elem.items()}
            print(json.dumps(result_dict, indent=4))
