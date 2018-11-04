import collections
import sys

import injector
import pandas

import app.logger


@injector.singleton
class Parser:
    @injector.inject
    def __init__(self, logger: app.logger.Logger):
        self._logger = logger

    def parse(self, stream):
        data = []
        for i, line in enumerate(stream, 1):
            if not line.rstrip():
                continue

            try:
                values = self.parse_line(line)
                if values:
                    data.append(values)
            except ValueError:
                sys.stderr.write(f"failed to parse the line: {i} - {line}\n")

        return pandas.DataFrame(data)

    def parse_line(self, line):
        if not line.rstrip():
            return None

        values = []
        for field in line.rstrip("\r\n").split("\t"):
            values.append(field.split(":", 1))

        return collections.OrderedDict(values)
