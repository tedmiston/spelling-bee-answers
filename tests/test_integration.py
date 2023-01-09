"""
Integration tests.
"""

import datetime
import json
from datetime import timedelta
from pathlib import Path

from utils import date_range


def test_output_json_schema():
    """
    Assert that the JSON output file format is being maintained.
    """
    # todo: update this to use the most recent available day filepath
    # note: 2023-01-02 also has "expiration" key when pulled remotely, but not when
    # pulled locally for some reason
    with open("days/2023-01-01.json") as fp:
        doc = json.load(fp)

    assert sorted(doc.keys()) == [
        "answers",
        "centerLetter",
        "displayDate",
        "displayWeekday",
        "editor",
        "freeExpiration",
        "id",
        "outerLetters",
        "pangrams",
        "printDate",
        "validLetters",
    ]

    assert len(doc["outerLetters"]) > 0
    assert len(doc["validLetters"]) > 0
    assert len(doc["pangrams"]) > 0
    assert len(doc["answers"]) > 0


def test_daily_answers_complete():
    """
    Assert that a daily answer file exists for each day from the start through the present (yesterday).
    """
    # fix for when the test is run between midnight and 3 am on the following day when
    # the previous day's puzzle hasn't closed yet (it's live until just before 3 am
    # eastern on the following day)
    days_offset = 2 if datetime.datetime.now().hour < 3 else 1

    date_list = date_range(
        start_date=datetime.date(2023, 1, 1),
        end_date=datetime.date.today() - timedelta(days=days_offset),
    )

    for date in date_list:
        path = Path(f"days/{date}.json")
        assert path.exists()
