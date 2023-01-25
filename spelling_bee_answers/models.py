"""
Models.
"""

import json
from datetime import date
from typing import List, Optional

from pydantic import BaseModel
from rich import print


class Puzzle(BaseModel):
    date: date
    center_letter: str
    outer_letters: List[str]
    points: Optional[int]
    answers: List[str]
    pangrams: List[str]
    editor: Optional[str]
    verified: bool


def main():
    filepath = "days/2023-01-01.json"
    # filepath = "days/2023-01-23.json"
    with open(filepath) as fp:
        obj = json.load(fp)
        # print(obj)
        p = Puzzle(
            date=obj["printDate"],
            center_letter=obj["centerLetter"],
            outer_letters=obj["outerLetters"],
            points=None,  # todo: see if i can get this from somewhere
            answers=obj["answers"],
            pangrams=obj["pangrams"],
            editor=obj["editor"],
            verified=True,
        )
        print(p)


if __name__ == "__main__":
    main()
