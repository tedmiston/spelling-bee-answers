"""
Generate a list of all words across all days and their frequencies.
"""

import json
from collections import Counter
from pathlib import Path
from pprint import pprint

from tabulate import tabulate

from .settings import settings


def load_all_answers():
    answers = []

    paths = Path(f"{settings.repo_root}/days").glob("*.json")
    paths = sorted(paths)

    for i in paths:
        day_answers = json.load(open(i))["answers"]
        answers.extend(day_answers)

    return answers


def determine_counts(answers):
    counts = Counter(answers)
    # pprint(counts)
    return counts


def generate_table(counts):
    headers = ["Word", "Count"]
    rows = [(word, count) for word, count in counts.items()]
    table = tabulate(rows, headers=headers, tablefmt="github")
    # print(table)
    return table


def update_doc(table):
    tag_start, tag_end = (
        "<!-- generated table start -->",
        "<!-- generated table end -->",
    )

    with open(f"{settings.repo_root}/All Words.md", "r+") as fp:
        doc = fp.read()
        tag_start_idx, tag_end_idx = doc.find(tag_start), doc.find(tag_end)
        after_tag_start_idx = tag_start_idx + len(tag_start)
        doc_parts = [
            doc[:after_tag_start_idx],
            table,
            doc[tag_end_idx:],
        ]

        output = "\n\n".join(doc_parts)
        # print(output)
        fp.seek(0)
        fp.write(output)


def main():
    answers = load_all_answers()
    counts = determine_counts(answers)
    table = generate_table(counts)
    update_doc(table)


if __name__ == "__main__":
    main()
