from src.client.client import TheOneAPIClient
from .api import characters
from .api.movies import MoviesAPI


class TheOneSDK:
    def __init__(self, api_key):
        self.client = TheOneAPIClient(api_key)

        self.movies = MoviesAPI(self.client)
        # self.characters = CharactersAPI(self.client)

