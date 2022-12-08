import json
import os

from concurrent.futures import ThreadPoolExecutor

import requests

from task_string_url_pytest.functions_for_check import (  # noqa: F401
    check_url,
    check_server_connection_put,
    check_server_connection_delete,
    check_server_connection_get,
    check_server_connection_head,
    check_server_connection_options,
    check_server_connection_patch,
    check_server_connection_post
)

strings = [
    'https://google.by', 'https://yandex.ru',
    'https://youtube.com', 'set/os.symbols', 'https://stackoverflow.com',
    'htt://docs-python.ru/', 'https://facebook.com', 'https://habr.com',
    'https://django.fun', 'https://pythontic.com', 'https://github.com',
    'https://python-dependency-injector.ets-labs.org/introduction/index.html'
]


def get_method_codes(url):
    with requests.Session() as session:
        result = {url: {}}
        response_get = check_server_connection_get(url, session)
        if response_get:
            result[url]['GET'] = response_get.status_code
        response_post = check_server_connection_post(url, session)
        if response_post:
            result[url]['POST'] = response_post.status_code
        response_put = check_server_connection_put(url, session)
        if response_put:
            result[url]['PUT'] = response_put.status_code
        response_delete = check_server_connection_delete(url, session)
        if response_delete:
            result[url]['DELETE'] = response_delete.status_code
        response_options = check_server_connection_options(url, session)
        if response_options:
            result[url]['OPTIONS'] = response_options.status_code
        response_head = check_server_connection_head(url, session)
        if response_head:
            result[url]['HEAD'] = response_head.status_code
        response_patch = check_server_connection_patch(url, session)
        if response_patch:
            result[url]['PATCH'] = response_patch.status_code
        return {k: v for k, v in result.items() if v}


def work():
    urls = check_url(*strings)
    if urls:
        count_core_of_processor = os.cpu_count()
        lenght_urls = len(urls)
        count_workers = (len(urls) if lenght_urls <= count_core_of_processor  # type: ignore
                        else count_core_of_processor * 2)  # type: ignore
        with ThreadPoolExecutor(max_workers=count_workers) as executor:
            res = executor.map(get_method_codes, urls)
            result_dict = {key: val for elem in res for key, val in elem.items()}
            print(json.dumps(result_dict, indent=4))
