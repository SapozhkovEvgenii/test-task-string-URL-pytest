import pytest
from task_string_url_pytest.functions_for_check import check_url


@pytest.mark.url_valid
@pytest.mark.parametrize("urls, expected_result", [
        (
            ['https://google.by', 'https://yandex.ru', 'fhhjdk'],
            {'https://google.by', 'https://yandex.ru'}
        ),
        (
            ['https://google.by', 'https://yandex.ru', "sdjkhfj", 'https://yandex.ru'],
            {'https://google.by', 'https://yandex.ru'}
        ),
        (
            ['https://youtube.com', 'https://stackoverflow.com', 'https:/stackoverflow.com'],
            {'https://youtube.com', 'https://stackoverflow.com'}
        ),

    ]
)
def test_check_url(urls, expected_result):
    assert check_url(*urls) == expected_result


@pytest.mark.url_valid
@pytest.mark.parametrize("urls, expected_exception", [
        (
            ['https://google.by', 'https://yandex.ru', 123, 'fhhjdk'],
            TypeError
        ),
        (
            ['https://google.by', 'https://yandex.ru', "sdjkhfj", 23.5, 'https://yandex.ru'],
            TypeError
        ),
        (
            ['https://youtube.com', 'https://stackoverflow.com', True, 'https:/stackoverflow.com'],
            TypeError
        ),

    ]
)
def test_check_url_error(urls, expected_exception):
    with pytest.raises(expected_exception):
        check_url(*urls)


@pytest.mark.url_valid
def test_no_data():
    assert check_url() is None


@pytest.mark.url_fail
@pytest.mark.xfail()
@pytest.mark.parametrize("urls, expected_result", [
        (
            ['https://google.by', 'https://yandex.ru', 'fhhjdk'],
            {'https://google.by'}
        ),
        (
            ['https://google.by', 'https://yandex.ru', "sdjkhfj", 'https://yandex.ru'],
            {'https://google.by', 'http://yandex.ru'}
        ),
        (
            ['https://youtube.com', 'https://stackoverflow.com', 'https:/stackoverflow.com'],
            {}
        ),

    ]
)
def test_check_url_fail(urls, expected_result):
    assert check_url(*urls) == expected_result
