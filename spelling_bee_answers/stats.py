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


def generate_all_words_table(counts):
    headers = ["Word", "Count", "Definition"]
    rows = [(word, count, f"https://www.wordnik.com/words/{word}") for word, count in counts.items()]
    table = tabulate(rows, headers=headers, tablefmt="github")
    # print(table)
    return table


def generate_multi_count_words_table(counts):
    headers = ["Word", "Count", "Definition"]
    rows = [(word, count, f"https://www.wordnik.com/words/{word}") for word, count in counts.items() if count > 1]
    table = tabulate(rows, headers=headers, tablefmt="github")
    # print(table)
    return table


def update_doc(word_count, table, tag):
    tag_start, tag_end = (
        f"<!-- {tag} start -->",
        f"<!-- {tag} end -->",
    )

    with open(f"{settings.repo_root}/Words.md", "r+") as fp:
        doc = fp.read()
        tag_start_idx, tag_end_idx = doc.find(tag_start), doc.find(tag_end)
        after_tag_start_idx = tag_start_idx + len(tag_start)
        doc_parts = [
            doc[:after_tag_start_idx],
            f"{word_count} words",
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

    all_words_table = generate_all_words_table(counts)
    all_words_count = len(counts.keys())
    update_doc(all_words_count, all_words_table, tag="generated all table")

    multi_words_table = generate_multi_count_words_table(counts)
    multi_words_count = len([x for x in counts.values() if x > 1])
    update_doc(multi_words_count, multi_words_table, tag="generated multi table")


if __name__ == "__main__":
    main()
