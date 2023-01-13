"""
Generate the table of days in the readme file.
"""

import datetime
import logging
from datetime import timedelta

from tabulate import tabulate

from utils import date_range

logging.basicConfig(
    level=logging.INFO,
)


def generate_table():
    logging.info("Generating table")

    # fixme: if the time is after 3 am (+ some small buffer?), the current day should be
    # included too (see `test_integration.py:test_daily_answers_complete` for details)
    puzzle_dates = date_range(
        start_date=datetime.date(2023, 1, 1),
        end_date=datetime.date.today() - timedelta(days=1),
    )

    headers = ["Date", "File", "Forum", "Notes"]
    table = []
    for date in puzzle_dates:
        path_link = f"[{date}.json](days/{date}.json)"
        date_str = date.strftime("%Y/%m/%d")
        forum_link = f"[Forum](https://www.nytimes.com/{date_str}/crosswords/spelling-bee-forum.html)"
        notes = ""
        row = [date, path_link, forum_link, notes]
        table.append(row)

    return tabulate(table, headers=headers, tablefmt="github")


# def update_readme(markdown):
#     logging.info("Updating readme")
#     tag_start = "<!-- generated table start -->"
#     tag_end = "<!-- generated table end -->"
#     ...
#     pass  # todo


def main():
    markdown = generate_table()
    print(markdown)
    # update_readme(markdown)


if __name__ == "__main__":
    main()
