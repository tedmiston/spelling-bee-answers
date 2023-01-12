"""
Generate the table of days in the readme file.
"""

import datetime
import logging
from datetime import timedelta

from utils import date_range

logging.basicConfig(
    level=logging.INFO,
)


def generate_table():
    logging.info("Generating table")
    puzzle_dates = date_range(
        start_date=datetime.date(2023, 1, 1),
        end_date=datetime.date.today() - timedelta(days=1),
    )

    markdown = """
| Date       | File                                    | Notes |
|:-----------|:----------------------------------------|:------|
"""
    for date in puzzle_dates:
        markdown += f"| {date} | [{date}.json](days/{date}.json) |       |" + "\n"

    return markdown.strip()


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
