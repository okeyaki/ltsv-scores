import re

import injector


@injector.singleton
class Analyzer:
    def analyze(self, action, df):
        scores = []
        for _, values in df.iterrows():
            score = 0
            for rule in action.rules:
                match = re.search(rule.compiled_pattern, values[rule.field])
                if match:
                    score += rule.weight

            scores.append(score)

        df['score'] = scores

        return df.groupby([action.evaluated_field])['score'] \
            .sum() \
            .reset_index() \
            .sort_values('score', ascending=True)
