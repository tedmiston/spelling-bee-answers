"""
Generate the table of days in the readme file.
"""

import json
import logging

import pendulum
from tabulate import tabulate

from .models import load_puzzle_from_json
from .settings import settings

logging.basicConfig(
    level=getattr(logging, settings.log_level),
)


def _get_puzzle_dates():
    # if the time is after 12 am eastern but before 3 am eastern, then the current day
    # is *NOT* be included yet as the new day's puzzle gets published at 3 am eastern
    start_date = pendulum.date(2023, 1, 1)
    day_offset = 1 if pendulum.now(tz="US/Eastern").hour >= 3 else 2
    end_date = pendulum.today().date() - pendulum.duration(days=day_offset)
    puzzle_dates = end_date - start_date
    return puzzle_dates


def generate_table():
    logging.info("Generating table")

    puzzle_dates = _get_puzzle_dates()

    headers = ["Date", "File", "Forum", "Words", "Pangrams"]
    table = []
    for date in puzzle_dates:
        filepath = f"days/{date}.json"
        path_link = f"[{date}.json](../{filepath})"
        date_str = date.strftime("%Y/%m/%d")
        forum_link = f"[Forum](https://www.nytimes.com/{date_str}/crosswords/spelling-bee-forum.html)"
        puzzle = load_puzzle_from_json(filepath=f"{settings.repo_root}/{filepath}")
        word_count = len(puzzle.answers)
        pangram_count = len(puzzle.pangrams)
        row = [f"**{date}**", path_link, forum_link, word_count, pangram_count]
        table.append(row)

    markdown = tabulate(table, headers=headers, tablefmt="github")
    if settings.display_generated_readme_table:
        print(markdown)

    return markdown


def update_doc(markdown, filename=f"{settings.outputs_dir}/Days.md"):
    logging.info("Updating readme")

    tag_start, tag_end = (
        "<!-- generated table start -->",
        "<!-- generated table end -->",
    )

    with open(f"{settings.repo_root}/{filename}", "r+") as fp:
        doc = fp.read()
        tag_start_idx, tag_end_idx = doc.find(tag_start), doc.find(tag_end)
        after_tag_start_idx = tag_start_idx + len(tag_start)
        doc_parts = [
            doc[:after_tag_start_idx],
            markdown,
            doc[tag_end_idx:],
        ]

        output = "\n\n".join(doc_parts)
        if settings.display_generated_readme_output:
            print(output)
        fp.seek(0)
        fp.write(output)

    logging.info("Done")


def main():  # pragma: no cover
    markdown = generate_table()
    update_doc(markdown)


if __name__ == "__main__":
    main()
