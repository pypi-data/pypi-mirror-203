import pytest
from src.client.client import TheOneAPIClient
from src.common.exceptions import InvalidApiKeyException, InvalidVersionException, InvalidEndpointException
from tests.mock import MockAPI


class TestTheOneAPIClient:
    def test_valid_endpoints(self, requests_mock):
        client = TheOneAPIClient(api_key="test")
        requests_mock.get(client.base_url + '/v2/movie', json=MockAPI.get_search_movie_response())

        endpoints = [
            "movie",
        ]

        for endpoint in endpoints:
            # make sure approved endpoints work
            response = client.get(endpoint)
            assert 'The Return of the King' == response['docs'][0]['name']

    def test_invalid_endpoints(self):
        client = TheOneAPIClient(api_key="test")
        endpoints = [
            "foo",
        ]
        with pytest.raises(InvalidEndpointException):
            for endpoint in endpoints:
                response = client.get(endpoint)

    def test_invalid_api_key(self, caplog):
        with pytest.raises(InvalidApiKeyException):
            TheOneAPIClient(api_key=None)

        # Verify that the log messages were fired
        assert "Invalid API key" in caplog.text

    def test_invalid_version(self, caplog):
        with pytest.raises(InvalidVersionException):
            TheOneAPIClient(api_key="test", version="invalid_version")

        # Verify that the log messages were fired
        assert "Invalid version" in caplog.text


