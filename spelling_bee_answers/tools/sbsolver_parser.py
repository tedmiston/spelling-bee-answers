"""
Scrape puzzle data from the SBSolver archive.

Example:
- https://www.sbsolver.com/archive/2018/05
- https://www.sbsolver.com/s/1
"""

import pendulum
import requests
from bs4 import BeautifulSoup
from rich import print

from ..models import Puzzle


def main():
    # this puzzle id in the url *does not* correspond to the nytimes puzzle id
    url = "https://www.sbsolver.com/s/1"
    # url = "https://www.sbsolver.com/s/1721"
    response = requests.get(url)

    if not response.ok:
        raise Exception("ut oh")

    soup = BeautifulSoup(response.content, "html.parser")

    date = soup.find("span", attrs={"class": "bee-date"}).find("a").text
    date = pendulum.parse(
        date, strict=False
    ).date()  # non-strict falls back to the dateutil parser

    all_letters = [
        x["alt"]
        for x in soup.find("div", attrs={"id": "alpha-inner"})
        .find("div", attrs={"class": "bee-medium"})
        .find("div", attrs={"class": "thinner-space-after"})
        .find_all("img")
    ]
    # print(all_letters)

    # extract center letter and outer letters
    center_letter = None
    outer_letters = []
    for i in all_letters:
        if i.startswith("center letter"):
            center_letter = i.rsplit(" ")[-1].lower()
        else:
            outer_letters.append(i.lower())

    points = int(
        soup.find_all("span", attrs={"class": "bee-loud"})[-1].text.split(" ")[0]
    )
    # print(points)

    answers_table = soup.find("table", attrs={"class": "bee-set"})
    answers = [
        x.text for x in answers_table.find_all("td", attrs={"class": "bee-hover"})
    ]
    answers = sorted([x.lower() for x in answers])
    # print(answers)

    # todo: implement pangram parsing
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
    print(puzzle)


if __name__ == "__main__":
    main()
