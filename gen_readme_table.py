"""
Generate the table of days in the readme file.
"""

import datetime
from datetime import timedelta

from utils import date_range


def main():
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

    print(markdown.lstrip())


if __name__ == "__main__":
    main()
