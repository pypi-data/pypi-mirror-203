class BaseException(Exception):
    pass

class InvalidApiKeyException(BaseException):
    def __init__(self):
        message = "THE_ONE_API_KEY environment variable is not set or is invalid."
        super().__init__(message)

class InvalidVersionException(BaseException):
    def __init__(self, version):
        message = f"The API version '{version}' is not valid or is not supported by this SDK."
        super().__init__(message)


class InvalidSearchKeyError(BaseException):
    """
    Exception raised when an invalid search key is provided to the search() method.
    """
    def __init__(self, message):
        super().__init__(message)
