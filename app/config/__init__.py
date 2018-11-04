import re

import injector
import yaml


class Config:
    def __init__(self, action):
        self.action = action


class Action:
    def __init__(self, evaluated_field):
        self.evaluated_field = evaluated_field

        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)


class ActionRule:
    def __init__(self, field, pattern, weight):
        self.field = field
        self.pattern = pattern
        self.weight = weight

        self.compiled_pattern = re.compile(re.escape(self.pattern))


@injector.singleton
class ConfigLoader:
    def __init__(self):
        pass

    def load(self, file):
        with open(file) as stream:
            data = yaml.load(stream)

            action = Action(evaluated_field=data["action"]["evaluated_field"])

            for rule_data in data["action"]["rules"]:
                action.add_rule(
                    ActionRule(
                        field=rule_data["field"],
                        pattern=rule_data["pattern"],
                        weight=rule_data["weight"]
                    )
                )

            return Config(action=action)
