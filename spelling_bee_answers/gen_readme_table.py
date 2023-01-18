"""
Generate the table of days in the readme file.
"""

import datetime
import json
import logging
from datetime import timedelta

from tabulate import tabulate

from .settings import settings
from .utils import date_range

logging.basicConfig(
    level=getattr(logging, settings.log_level),
)


def get_days_word_count(filepath):
    with open(filepath) as fp:
        day = json.load(fp)

    word_count = len(day["answers"])
    return word_count


def generate_table():
    logging.info("Generating table")

    # fixme: if the time is after 12 am but before 3 am (+ some small buffer?), then the
    # current day should *NOT* be included yet (see
    # `test_integration.py:test_daily_answers_complete` for details)
    puzzle_dates = date_range(
        start_date=datetime.date(2023, 1, 1),
        end_date=datetime.date.today() - timedelta(days=1),
    )

    headers = ["Date", "File", "Forum", "Word Count", "Notes"]
    table = []
    for date in puzzle_dates:
        filepath = f"days/{date}.json"
        path_link = f"[{date}.json]({filepath})"
        date_str = date.strftime("%Y/%m/%d")
        forum_link = f"[Forum](https://www.nytimes.com/{date_str}/crosswords/spelling-bee-forum.html)"
        word_count = get_days_word_count(f"{settings.repo_root}/{filepath}")
        notes = ""
        row = [date, path_link, forum_link, word_count, notes]
        table.append(row)

    return tabulate(table, headers=headers, tablefmt="github")


def update_readme(markdown):
    logging.info("Updating readme")

    tag_start, tag_end = (
        "<!-- generated table start -->",
        "<!-- generated table end -->",
    )

    with open(f"{settings.repo_root}/README.md", "r+") as fp:
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


def main():
    markdown = generate_table()
    if settings.display_generated_readme_table:
        print(markdown)
    update_readme(markdown)


if __name__ == "__main__":
    main()
