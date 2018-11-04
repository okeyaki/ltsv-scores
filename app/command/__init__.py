import argparse
import sys

import injector

import app.analyzer
import app.config
import app.parser


@injector.singleton
class Command:
    @injector.inject
    def __init__(
        self,
        config_loader: app.config.ConfigLoader,
        parser: app.parser.Parser,
        analyzer: app.analyzer.Analyzer,
    ):
        self._config_loader = config_loader
        self._parser = parser
        self._analyzer = analyzer

    def run(self):
        args = self._parse_args()

        config = self._config_loader.load(args.config)

        if args.target:
            with open(args.target) as stream:
                df = self._parser.parse(stream)
        else:
            df = self._parser.parse(sys.stdin)

        print(self._analyzer.analyze(config.action, df).to_string(index=False))

    def _parse_args(self):
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument("--target")
        arg_parser.add_argument("--config")

        return arg_parser.parse_args()
