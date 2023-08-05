import logging

logger = logging.getLogger(__name__)

class BaseException(Exception):
    def __init__(self, message):
        super().__init__(message)
        logger.error(message)

class InvalidApiKeyException(BaseException):
    def __init__(self):
        message = "Invalid API key."
        super().__init__(message)

class InvalidEndpointException(BaseException):
    def __init__(self, endpoint):
        message = f"Invalid endpoint: {endpoint}"
        super().__init__(message)

class InvalidVersionException(BaseException):
    def __init__(self, version):
        message = f"Invalid version: {version}"
        super().__init__(message)

class InvalidSearchKeyError(BaseException):
    def __init__(self, message):
        super().__init__(message)
