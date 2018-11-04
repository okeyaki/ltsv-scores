import sys

import logbook
import injector


@injector.singleton
class Logger:
    def __init__(self):
        self.logger = logbook.Logger("default")

        logbook.StreamHandler(sys.stdout).push_application()

    def error(self, message):
        self.logger.error(message)

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)
