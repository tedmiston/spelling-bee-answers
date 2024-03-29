"""
Scrape puzzle data from the SBSolver archive.

Example:
- https://www.sbsolver.com/archive/2018/05
- https://www.sbsolver.com/s/1
"""

import json
import logging
from pathlib import Path

import pendulum
import requests
from bs4 import BeautifulSoup
from rich import print

from ..interfaces import SpellingBeeScraperInterface
from ..models import Puzzle
from ..settings import settings

logging.basicConfig(
    level=logging.INFO,
)


class SBSolverScraper(SpellingBeeScraperInterface):
    """
    SBSolver Spelling Bee Archive scraper.
    """

    def _build_url(self, puzzle_id):
        """
        Construct an SBSolver puzzle URL.
        """
        # this puzzle id in the url *does not* correspond to the nytimes puzzle id
        url = f"https://www.sbsolver.com/s/{puzzle_id}"
        return url

    def fetch_page(self, url):
        """
        Fetch the contents of the page at the given URL.
        """
        logging.info("Fetching puzzle")

        response = requests.get(url)
        if not response.ok:
            raise Exception("HTTP response code was not successful")

        return response

    def extract_game_data(self, response):
        """
        Parse the webpage extracting the JavaScript game data.
        """
        logging.info("Extracting game data")

        soup = BeautifulSoup(response.content, "html.parser")
        return soup

    def parse_game_data(self, soup):
        """
        Parse the yesterday game data from JavaScript into a Python object.
        """
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

        # example with one pangrams - https://www.sbsolver.com/s/1
        # example with multiple pangrams - https://www.sbsolver.com/s/2
        grid = soup.find("table", attrs={"class": ["bee", "bee-grid"]})
        pangrams_str = grid.find_next("b").text
        pangrams = [x.strip() for x in pangrams_str.lower().split(",")]

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

    def output_game_data(self, puzzle):
        """
        Write the game data to disk.
        """
        logging.info("Writing game data")

        output = puzzle.json()

        # pretty print json output (not supported by the pydantic json encoder)
        output = json.dumps(json.loads(output), indent=2)

        path = Path(f"{settings.repo_root}/days/{puzzle.date}.json")
        if path.exists():
            logging.warning(f"Not overwriting existing file: `{path}`")
        else:
            logging.info(f"Creating new file: `{path}`")
            with open(path, "w") as fp:
                fp.write(output + "\n")

        logging.info("Done")

    def run(self):
        """
        Entrypoint for running the above functions.
        """
        # puzzle_id = 1  # 1...1721
        # puzzle_id = 2
        puzzle_id = 1721

        url = self._build_url(puzzle_id=puzzle_id)
        response = self.fetch_page(url=url)
        soup = self.extract_game_data(response=response)
        puzzle = self.parse_game_data(soup=soup)
        print(puzzle)
        self.output_game_data(puzzle=puzzle)


def main():  # pragma: no cover
    """
    Entrypoint for development of SBSolverScraper.
    """
    sbss = SBSolverScraper()
    sbss.run()


if __name__ == "__main__":
    main()
