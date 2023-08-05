from unittest.mock import Mock
import pytest
from requests_mock import Mocker
from src.client.client import TheOneAPIClient
from src.api.movies import MoviesAPI
from tests.mock import MockAPI


class TestMoviesAPI:

    def test_search_rejects_non_name(self, requests_mock):
        client = TheOneAPIClient(api_key="test")
        movies_api = MoviesAPI(client)
        requests_mock.get(
            client.base_url + '/v2/movie', json=MockAPI.get_search_movie_response())

        bad_params = {'foo': 'The Return of the King', 'dog': 'cat'}
        response = movies_api.search(bad_params)

        movie_data = response['docs'][0]
        for key in bad_params:
            assert key not in movie_data

    def test_search(self, requests_mock):
        client = TheOneAPIClient(api_key="test")
        movies_api = MoviesAPI(client)
        requests_mock.get(
            client.base_url + '/v2/movie', json=MockAPI.get_search_movie_response())

        response = movies_api.search(name='The Return of the King')
        movie_data = response['docs'][0]

        assert movie_data['name'] == 'The Return of the King'
        assert movie_data['academyAwardWins'] == 11

    def test_get_all(self, requests_mock):
        client = TheOneAPIClient(api_key="test")
        movies_api = MoviesAPI(client)
        requests_mock.get(
            client.base_url + '/v2/movie', json=MockAPI.get_full_movie_response())

        response = movies_api.search()
        assert response

    def test_get_all_with_different_params(self, requests_mock):
        client = TheOneAPIClient(api_key="test")
        movies_api = MoviesAPI(client)
        requests_mock.get(
            client.base_url + '/v2/movie', json=MockAPI.get_full_movie_response())

        expected_calls = [
            ({'limit': 10},),
            ({'sort': 'release_date'},),
            ({'offset': 5},),
            ({'limit': 10, 'sort': 'release_date'},),
            ({'limit': 10, 'offset': 5},),
            ({'sort': 'release_date', 'offset': 5},),
            ({'limit': 10, 'sort': 'release_date', 'offset': 5},),
        ]
        for expected_call in expected_calls:
            response = movies_api.search(*expected_call)
            assert len(response['docs'][0]) == 8

