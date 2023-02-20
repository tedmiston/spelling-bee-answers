"""
Models.
"""

import json
from datetime import date
from enum import StrEnum
from typing import List, Optional

from pydantic import BaseModel
from rich import print


class PartOfSpeech(StrEnum):
    """
    Parts of speech constants.
    """

    ADJECTIVE = "adj."
    ADVERB = "adv."
    NOUN = "n."
    VERB = "v."


class Word(BaseModel):
    """
    A single word and its related traits.
    """

    word: str
    # word: PartOfSpeech
    part_of_speech: str
    definitions: List[str]


class Puzzle(BaseModel):
    """
    A Spelling Bee daily puzzle.
    """

    date: date
    center_letter: str
    outer_letters: List[str]
    points: Optional[int]
    answers: List[str]
    pangrams: List[str]
    editor: Optional[str]
    verified: bool


def load_puzzle_from_json(filepath):
    """
    Load a JSON puzzle file from disk.

    Note: The data shape is different for puzzles from the NYTimes (verified) vs
    backfill data aggregated from third party sources (non-verified).
    """
    with open(filepath) as fp:
        obj = json.load(fp)

    verified = obj.get("verified")
    if verified is None:
        # puzzle data from nytimes does not have this field in json representation
        puzzle = Puzzle(
            date=obj["printDate"],
            center_letter=obj["centerLetter"],
            outer_letters=obj["outerLetters"],
            points=None,  # todo: see if i can get this from somewhere
            answers=obj["answers"],
            pangrams=obj["pangrams"],
            editor=obj["editor"],
            verified=True,
        )
    elif verified is False:
        # puzzle data from sbsolver does have this field in json representation
        puzzle = Puzzle(
            date=obj["date"],
            center_letter=obj["center_letter"],
            outer_letters=obj["outer_letters"],
            points=obj["points"],
            answers=obj["answers"],
            pangrams=obj["pangrams"],
            editor=obj["editor"],
            verified=verified,
        )
    else:
        raise Exception("Invalid value for verified")

    return puzzle


def main():  # pragma: no cover
    """
    Entrypoint to quick test loading a single puzzle.
    """
    # todo: update main to take filepath as a sysarg

    # todo: copy this code to `test_load_puzzle_from_json`
    filepath = "days/2023-01-01.json"
    # filepath = "days/2023-01-23.json"
    puzzle = load_puzzle_from_json(filepath)
    print(puzzle)


if __name__ == "__main__":
    main()
