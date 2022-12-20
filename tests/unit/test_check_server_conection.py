from task_string_url_pytest.functions_for_check import (
    check_server_connection_get,
    check_server_connection_delete,
    check_server_connection_head,
    check_server_connection_options,
    check_server_connection_patch,
    check_server_connection_post,
    check_server_connection_put
    )

import requests
import pytest


@pytest.fixture(scope='module')
def session():
    session = requests.Session()
    yield session
    session.close()


def test_check_server_connection_get(session):
    res = check_server_connection_get('https://google.by', session)
    assert (isinstance(res, requests.Response) or (res is None))


def test_check_server_connection_delete(session):
    res = check_server_connection_delete('https://google.by', session)
    assert (isinstance(res, requests.Response) or (res is None))


def test_check_server_connection_head(session):
    res = check_server_connection_head('https://google.by', session)
    assert (isinstance(res, requests.Response) or (res is None))


def test_check_server_connection_options(session):
    res = check_server_connection_options('https://google.by', session)
    assert (isinstance(res, requests.Response) or (res is None))


def test_check_server_connection_patch(session):
    res = check_server_connection_patch('https://google.by', session)
    assert (isinstance(res, requests.Response) or (res is None))


def test_check_server_connection_post(session):
    res = check_server_connection_post('https://google.by', session)
    assert (isinstance(res, requests.Response) or (res is None))


def test_check_server_connection_put(session):
    res = check_server_connection_put('https://google.by', session)
    assert (isinstance(res, requests.Response) or (res is None))
