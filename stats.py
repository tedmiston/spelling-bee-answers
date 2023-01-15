"""
Stats.
"""

import json
from collections import Counter
from pathlib import Path
from pprint import pprint

answers = []

paths = Path("days").glob("*.json")
paths = sorted(paths)

for i in paths:
    day_answers = json.load(open(i))["answers"]
    answers.extend(day_answers)

counts = Counter(answers)
pprint(counts)
