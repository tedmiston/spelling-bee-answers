"""
Generate tables of words across all days.
"""

import json
from collections import Counter
from pathlib import Path

from rich import print
from tabulate import tabulate

from .models import load_puzzle_from_json
from .settings import settings


def _load_all_puzzles():
    paths = Path(f"{settings.repo_root}/days").glob("*.json")
    paths = sorted(paths)

    puzzles = [load_puzzle_from_json(filepath=path) for path in paths]
    return puzzles


def _load_all_puzzles_by_key(key):
    puzzles = _load_all_puzzles()

    values = [getattr(x, key) for x in puzzles]
    values_flattened = []
    for i in values:
        values_flattened.extend(i)

    return values_flattened


def load_all_answers():
    return _load_all_puzzles_by_key(key="answers")


def load_all_pangrams():
    return _load_all_puzzles_by_key(key="pangrams")


def determine_counts(words):
    counts = Counter(words)
    # print("counts:", counts)
    return counts


def _generate_words_table(counts, condition=lambda _: True):
    headers = ["Word", "Count", "Definition"]
    rows = [
        (f"**{word}**", count, f"https://www.wordnik.com/words/{word}")
        for word, count in sorted(counts.items())
        if condition(count)
    ]
    table = tabulate(rows, headers=headers, tablefmt="github")
    # print(table)
    return table


def generate_all_words_table(counts):
    return _generate_words_table(counts)


def generate_multi_count_words_table(counts):
    return _generate_words_table(counts, lambda count: count > 1)


def generate_pangrams_table(counts):
    return _generate_words_table(counts)


def update_doc(filename, tag, table, word_count, label):
    tag_start, tag_end = (
        f"<!-- {tag} start -->",
        f"<!-- {tag} end -->",
    )

    with open(f"{settings.repo_root}/{filename}", "r+") as fp:
        doc = fp.read()
        tag_start_idx, tag_end_idx = doc.find(tag_start), doc.find(tag_end)
        after_tag_start_idx = tag_start_idx + len(tag_start)
        doc_parts = [
            doc[:after_tag_start_idx],
            f"{word_count} {label}",
            table,
            doc[tag_end_idx:],
        ]

        output = "\n\n".join(doc_parts)
        # print(output)
        fp.seek(0)
        fp.write(output)


def main():
    # all words and multi-count words lists
    answers = load_all_answers()
    all_answers_counts = determine_counts(answers)
    update_doc(
        filename="Words.md",
        tag="generated multi table",
        table=generate_multi_count_words_table(all_answers_counts),
        word_count=len([x for x in all_answers_counts.values() if x > 1]),
        label="words",
    )
    update_doc(
        filename="Words.md",
        tag="generated all table",
        table=generate_all_words_table(all_answers_counts),
        word_count=len(all_answers_counts.keys()),
        label="words",
    )

    # pangrams list
    pangrams = load_all_pangrams()
    pangrams_counts = determine_counts(pangrams)
    update_doc(
        filename="Pangrams.md",
        tag="generated table",
        table=generate_pangrams_table(pangrams_counts),
        word_count=len(pangrams_counts.keys()),
        label="pangrams",
    )


if __name__ == "__main__":
    main()
