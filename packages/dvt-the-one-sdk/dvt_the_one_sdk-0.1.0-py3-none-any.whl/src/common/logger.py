import logging


class Logger:
    __instance = None

    def __init__(self, name="the-one-api-logger", level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)

        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        console_handler.setFormatter(formatter)

        self.logger.addHandler(console_handler)

    @staticmethod
    def get_instance():
        if Logger.__instance == None:
            Logger.__instance = Logger()
        return Logger.__instance

    def set_level(self, level):
        self.logger.setLevel(level)
        for handler in self.logger.handlers:
            handler.setLevel(level)

