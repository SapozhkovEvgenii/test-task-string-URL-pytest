import validators
import requests


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


def check_server_connection_get(url: str, session):
    """ server connection check using GET method """
    try:
        response = session.get(url)
        if response and response.status_code != 405:
            return response
    except requests.ConnectionError:
        return None


def check_server_connection_post(url: str, session: requests.Session):
    """ server connection check using POST method """
    try:
        response = session.post(url)
        if response and response.status_code != 405:
            return response
    except requests.ConnectionError:
        return None


def check_server_connection_put(url: str, session: requests.Session):
    """ server connection check using PUT method """
    try:
        response = session.put(url)
        if response and response.status_code != 405:
            return response
    except requests.ConnectionError:
        return None


def check_server_connection_delete(url: str, session: requests.Session):
    """ server connection check using DELETE method """
    try:
        response = session.delete(url)
        if response and response.status_code != 405:
            return response
    except requests.ConnectionError:
        return None


def check_server_connection_options(url: str, session: requests.Session):
    """ server connection check using OPTIONS method """
    try:
        response = session.options(url)
        if response and response.status_code != 405:
            return response
    except requests.ConnectionError:
        return None


def check_server_connection_head(url: str, session: requests.Session):
    """ server connection check using HEAD method """
    try:
        response = session.head(url)
        if response and response.status_code != 405:
            return response
    except requests.ConnectionError:
        return None


def check_server_connection_patch(url: str, session: requests.Session):
    """ server connection check using PATCH method """
    try:
        response = session.patch(url)
        if response and response.status_code != 405:
            return response
    except requests.ConnectionError:
        return None
