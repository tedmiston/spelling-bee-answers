"""
Scrape puzzle data from the SBSolver archive.

Example:
- https://www.sbsolver.com/archive/2018/05
- https://www.sbsolver.com/s/1
"""

import json
import logging

import pendulum
import requests
from bs4 import BeautifulSoup
from rich import print

from ..models import Puzzle
from ..settings import settings

logging.basicConfig(
    level=logging.INFO,
)


def fetch_page(puzzle_id):
    logging.info("Fetching puzzle")

    # this puzzle id in the url *does not* correspond to the nytimes puzzle id
    url = f"https://www.sbsolver.com/s/{puzzle_id}"
    response = requests.get(url)

    if not response.ok:
        raise Exception("HTTP response code was not successful")

    return response


def extract_game_data(response):
    logging.info("Extracting game data")

    soup = BeautifulSoup(response.content, "html.parser")
    return soup


def parse_game_data(soup):
    date = soup.find("span", attrs={"class": "bee-date"}).find("a").text
    date = pendulum.parse(
        date, strict=False
    ).date()  # non-strict enables dateutil parser

    all_letters = [
        x["alt"]
        for x in soup.find("div", attrs={"id": "alpha-inner"})
        .find("div", attrs={"class": "bee-medium"})
        .find("div", attrs={"class": "thinner-space-after"})
        .find_all("img")
    ]

    # extract center letter and outer letters
    center_letter = None
    outer_letters = []
    for i in all_letters:
        if i.startswith("center letter"):
            center_letter = i.rsplit(" ")[-1].lower()
        else:
            outer_letters.append(i.lower())

    points_span = soup.find_all("span", attrs={"class": "bee-loud"})[-1]
    points = int(points_span.text.split(" ")[0])

    answers_table = soup.find("table", attrs={"class": "bee-set"})
    answers_tds = answers_table.find_all("td", attrs={"class": "bee-hover"})
    answers = [x.text for x in answers_tds]
    answers = sorted([x.lower() for x in answers])

    # fixme: implement pangram parsing
    # example with multiple pangrams - https://www.sbsolver.com/s/2
    pangrams = []

    puzzle = Puzzle(
        date=date,
        center_letter=center_letter,
        outer_letters=outer_letters,
        points=points,
        answers=answers,
        pangrams=pangrams,
        editor=None,  # in this context null means unknown
        verified=False,
    )
    return puzzle


def output_game_data(puzzle):
    logging.info("Writing game data")

    output = puzzle.json()

    # pretty print json output (not supported by the pydantic json encoder)
    output = json.dumps(json.loads(output), indent=2)

    with open(f"{settings.repo_root}/days/{puzzle.date}.json", "w") as fp:
        fp.write(output + "\n")

    logging.info("Done")


def main():  # pragma: no cover
    response = fetch_page(puzzle_id=1)  # 1...1721
    soup = extract_game_data(response)
    puzzle = parse_game_data(soup)
    print(puzzle)
    output_game_data(puzzle)


if __name__ == "__main__":
    main()
