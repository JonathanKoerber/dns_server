import pytest
from unittest import mock
from dns import buildresponse, load_zones, bind_socket


@pytest.mark.parametrize('search_size', [10, 100, 200, 300, 400, 500, 6001000, 10000, 10000])
def test_search(search_size, search_target, dig_request):
    '''not sure how to get the server running. needs root privalage to bind socket to port.
    Maybe I can mock the port. But will still need to get the '''
    data = search_target(search_size, 'something.org')
    with mock.patch.object(bind_socket, autospec=True, return_value = dig_request):
        with mock.patch.object(load_zones, autospec=True, return_value = search_target(search_size, 'something.org')):
            resp = buildresponse(dig_request)
        assert True