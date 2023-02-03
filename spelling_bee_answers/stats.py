"""
Generate tables of words across all days.
"""

import json
from collections import Counter
from pathlib import Path
from typing import Any

from rich import print
from tabulate import tabulate

from .models import load_puzzle_from_json
from .settings import settings


def _load_all_puzzles() -> Any:
    paths: Any = Path(f"{settings.repo_root}/days").glob("*.json")
    paths = sorted(paths)

    puzzles: Any = [load_puzzle_from_json(filepath=path) for path in paths]
    return puzzles


def load_all_puzzles_by_key(key: str) -> Any:
    puzzles: Any = _load_all_puzzles()

    values: Any = [getattr(x, key) for x in puzzles]
    values_flattened: Any = []
    for i in values:
        values_flattened.extend(i)

    return values_flattened


def generate_words_table(counts: Any, condition: Any = lambda _: True) -> Any:
    headers: Any = ["Word", "Count", "Definition"]
    rows: Any = [
        (f"**{word}**", count, f"https://www.wordnik.com/words/{word}")
        for word, count in sorted(counts.items())
        if condition(count)
    ]
    table: Any = tabulate(rows, headers=headers, tablefmt="github")
    # print(table)
    return table


def update_doc(filename: str, tag: str, table: str, word_count: int, label: str) -> None:
    tag_start: str = f"<!-- {tag} start -->"
    tag_end: str = f"<!-- {tag} end -->"

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


def main() -> None:  # pragma: no cover
    # all words and multi-count words lists
    answers: Any = load_all_puzzles_by_key(key="answers")
    all_answers_counts: Counter[str] = Counter(answers)
    update_doc(
        filename="Words.md",
        tag="generated multi table",
        table=generate_words_table(all_answers_counts, lambda count: count > 1),
        word_count=len([x for x in all_answers_counts.values() if x > 1]),
        label="words",
    )
    update_doc(
        filename="Words.md",
        tag="generated all table",
        table=generate_words_table(all_answers_counts),
        word_count=len(all_answers_counts.keys()),
        label="words",
    )

    # pangrams list
    pangrams: Any = load_all_puzzles_by_key(key="pangrams")
    pangrams_counts: Counter[str] = Counter(pangrams)
    update_doc(
        filename="Pangrams.md",
        tag="generated table",
        table=generate_words_table(pangrams_counts),
        word_count=len(pangrams_counts.keys()),
        label="pangrams",
    )


if __name__ == "__main__":
    main()
