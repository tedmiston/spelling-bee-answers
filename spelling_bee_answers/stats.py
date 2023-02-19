"""
Generate tables of words across all days.
"""

from collections import Counter
from pathlib import Path

# from rich import print
from tabulate import tabulate

from .dictionary import load_definitions, lookup_word
from .models import load_puzzle_from_json
from .settings import settings


def _load_all_puzzles():
    paths = Path(f"{settings.repo_root}/days").glob("*.json")
    paths = sorted(paths)

    puzzles = [load_puzzle_from_json(filepath=path) for path in paths]
    return puzzles


def load_all_puzzles_by_key(key):
    puzzles = _load_all_puzzles()

    values = [getattr(x, key) for x in puzzles]
    values_flattened = []
    for i in values:
        values_flattened.extend(i)

    return values_flattened


def generate_words_table(counts, condition=lambda _: True):
    words_dict = load_definitions()

    headers = ["Word", "Count", "Definition Text", "Definition URL"]
    rows = []
    for word, count in sorted(counts.items()):
        if condition(count):
            word_obj = lookup_word(words_dict, word)
            if word_obj is not None:
                word_col = f"**{word}** <small>*({word_obj.part_of_speech})*</small>"
                if len(word_obj.definitions) > 1:
                    definition_text = "- " + "<br>- ".join(word_obj.definitions)
                else:
                    definition_text = word_obj.definitions[0]
            else:
                word_col = f"**{word}**"
                definition_text = None

            definition_url = f"https://www.wordnik.com/words/{word}"

            row = (word_col, count, definition_text, definition_url)
            rows.append(row)

    table = tabulate(rows, headers=headers, tablefmt="github")
    # print(table)
    return table


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


def main():  # pragma: no cover
    # all words lists
    answers = load_all_puzzles_by_key(key="answers")
    all_answers_counts = Counter(answers)
    update_doc(
        filename=f"{settings.output_dir}/{settings.output_file_words}",
        tag="generated multi table",
        table=generate_words_table(all_answers_counts, lambda count: count > 1),
        word_count=len([x for x in all_answers_counts.values() if x > 1]),
        label="words",
    )
    update_doc(
        filename=f"{settings.output_dir}/{settings.output_file_words}",
        tag="generated all table",
        table=generate_words_table(all_answers_counts),
        word_count=len(all_answers_counts.keys()),
        label="words",
    )

    # pangrams lists
    pangrams = load_all_puzzles_by_key(key="pangrams")
    pangrams_counts = Counter(pangrams)
    update_doc(
        filename=f"{settings.output_dir}/{settings.output_file_pangrams}",
        tag="generated multi table",
        table=generate_words_table(pangrams_counts, lambda count: count > 1),
        word_count=len([x for x in pangrams_counts.values() if x > 1]),
        label="pangrams",
    )
    update_doc(
        filename=f"{settings.output_dir}/{settings.output_file_pangrams}",
        tag="generated all table",
        table=generate_words_table(pangrams_counts),
        word_count=len(pangrams_counts.keys()),
        label="pangrams",
    )


if __name__ == "__main__":
    main()
