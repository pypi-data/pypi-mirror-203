import configparser
import requests

from ..common.exceptions import InvalidApiKeyException, InvalidVersionException, InvalidEndpointException
from ..common import constants as c
from ..common.logger import Logger
from ..common.utils import get_value_from_config


class TheOneAPIClient():
    def __init__(self, api_key, version="v2"):
        self.logger = Logger.get_instance()
        self.api_key = api_key
        self.version = version
        self.config = self._load_config()

        self.headers = {"Authorization": f"Bearer {self.api_key}"}

        self._check_api_key()
        self._check_version()

    def _check_api_key(self):
        if self.api_key is None:
            raise InvalidApiKeyException()

    def _check_version(self):
        if self.version not in ["v1", "v2"]:
            raise InvalidVersionException(self.version)

    def _load_config(self):
        config = configparser.ConfigParser()

        config_path = os.path.join(os.path.abspath(os.path.join(
            os.path.dirname(__file__), "..", "..")), "config.ini")

        if not os.path.isfile(config_path):
           raise FileNotFoundError(f"Config file not found at {config_path}")

        config.read(config_path)

        if c.API not in config:
            raise ValueError(f"Config file is missing [{c.API}] section")
        if c.ENDPOINTS not in config:
            raise ValueError(f"Config file is missing [{c.ENDPOINTS}] section")

        self.base_url = get_value_from_config(config, c.API, c.BASE_URL)
        self.timeout = get_value_from_config(config, c.API, c.TIMEOUT)

        # set the endpoint URLs using the config
        self.endpoints = {
            endpoint_name: config.get(c.ENDPOINTS, endpoint_name)
            for endpoint_name in c.SUPPORTED_ENDPOINTS
        }
        return config

    def get(
        self,
        endpoint: str,
        params: dict = None,
    ) -> dict:
        if endpoint not in self.endpoints:
            raise InvalidEndpointException(endpoint)

        url = f"{self.base_url}/{self.version}/{endpoint}"

        self.logger.info(f"GET {url} called with params {params}")
        response = requests.get(url, headers=self.headers, params=params)
        self.logger.info(f"Response status code: {response.status_code}")
        self.logger.info(f"Response content: {response.content}")
        response.raise_for_status()
        return response.json()

    def post(self, endpoint: str, data: dict) -> dict:
        pass
