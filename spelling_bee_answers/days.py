"""
Generate the table of days in the readme file.
"""

import json
import logging
from typing import List, Union

import pendulum
from pendulum.date import Date
from pendulum.period import Period
from tabulate import tabulate

from .models import Puzzle, load_puzzle_from_json
from .settings import settings

logging.basicConfig(
    level=getattr(logging, settings.log_level),
)


def generate_table() -> str:
    logging.info("Generating table")

    # if the time is after 12 am eastern but before 3 am eastern, then the current day
    # is *NOT* be included yet as the new day's puzzle gets published at 3 am eastern
    start_date: Date = pendulum.date(2023, 1, 1)
    day_offset: int = 1 if pendulum.now(tz="US/Eastern").hour >= 3 else 2
    end_date: Date = pendulum.today().date() - pendulum.duration(days=day_offset)
    puzzle_dates: Period = end_date - start_date

    headers: List[str] = ["Date", "File", "Forum", "Words", "Pangrams", "Notes"]
    table: List[List[Union[int, str]]] = []
    for date in puzzle_dates:
        filepath: str = f"days/{date}.json"
        path_link: str = f"[{date}.json]({filepath})"
        date_str: str = date.strftime("%Y/%m/%d")
        forum_link: str = f"[Forum](https://www.nytimes.com/{date_str}/crosswords/spelling-bee-forum.html)"
        puzzle: Puzzle = load_puzzle_from_json(filepath=f"{settings.repo_root}/{filepath}")
        word_count: int = len(puzzle.answers)
        pangram_count: int = len(puzzle.pangrams)
        notes: str = ""
        row: List[Union[int, str]] = [f"**{date}**", path_link, forum_link, word_count, pangram_count, notes]
        table.append(row)

    markdown: str = tabulate(table, headers=headers, tablefmt="github")
    if settings.display_generated_readme_table:
        print(markdown)

    return markdown


def update_readme(markdown: str, filename: str = "README.md") -> None:
    logging.info("Updating readme")

    tag_start: str = "<!-- generated table start -->"
    tag_end: str = "<!-- generated table end -->"

    with open(f"{settings.repo_root}/{filename}", "r+") as fp:
        doc: str = fp.read()
        tag_start_idx: int = doc.find(tag_start)
        tag_end_idx: int = doc.find(tag_end)
        after_tag_start_idx: int = tag_start_idx + len(tag_start)
        doc_parts: List[str] = [
            doc[:after_tag_start_idx],
            markdown,
            doc[tag_end_idx:],
        ]

        output: str = "\n\n".join(doc_parts)
        if settings.display_generated_readme_output:
            print(output)
        fp.seek(0)
        fp.write(output)

    logging.info("Done")


def main() -> None:  # pragma: no cover
    markdown: str = generate_table()
    update_readme(markdown)


if __name__ == "__main__":
    main()
