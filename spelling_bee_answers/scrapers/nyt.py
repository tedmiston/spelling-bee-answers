"""
NYTimes Spelling Bee answers.

Fetch the Yesterday's Answers to the NYTimes Spelling Bee puzzle each day for archival purposes.
"""

import json
import logging
import re
from pathlib import Path
from typing import Any, Dict, Optional

import requests
from bs4 import BeautifulSoup
from requests import Response
from rich import print

from ..interfaces import SpellingBeeScraperInterface
from ..models import Puzzle
from ..settings import settings

logging.basicConfig(
    level=logging.INFO,
)


class NYTimesScraper(SpellingBeeScraperInterface):
    """
    NYTimes Spelling Bee scraper.
    """

    url: str = "https://www.nytimes.com/puzzles/spelling-bee"

    def fetch_page(self, url: Optional[str] = None) -> Response:
        logging.info("Fetching puzzle")

        if url is None:
            url = self.url

        response = requests.get(url)
        if not response.ok:
            raise Exception("HTTP response code was not successful")

        return response

    def extract_game_data(self, response: Response) -> Any:
        logging.info("Extracting game data")

        soup: BeautifulSoup = BeautifulSoup(response.content, "html.parser")
        game_data_script = soup.find("script", string=re.compile("^window.gameData.*"))

        if not game_data_script:
            raise Exception("Game data script was not found")

        return game_data_script

    def parse_game_data(self, game_data_script: Any) -> Dict[str, Any]:
        logging.info("Parsing game data")

        yesterday_start_index = game_data_script.text.find('"yesterday"')
        yesterday_script_text = game_data_script.text[yesterday_start_index:]
        yesterday_end_index = yesterday_script_text.find("}") + 1
        yesterday_script_text = yesterday_script_text[:yesterday_end_index]

        if yesterday_start_index < 0 or yesterday_end_index < 0:
            raise Exception("Yesterday game data could not be parsed")

        try:
            yesterday_dict: Dict[str, Any] = json.loads("{" + yesterday_script_text + "}")
        except json.decoder.JSONDecodeError:
            raise Exception("JSON decoding of yesterday game data failed")

        if settings.display_puzzle_output:
            print(yesterday_dict["yesterday"])

        return yesterday_dict["yesterday"]

    def output_game_data(self, puzzle_dict: Dict[str, Any]) -> None:
        logging.info("Writing game data")

        # todo: use Puzzle model here?
        output = json.dumps(puzzle_dict, indent=2)
        puzzle_date = puzzle_dict["printDate"]

        path = Path(f"{settings.repo_root}/days/{puzzle_date}.json")
        if path.exists():
            logging.warn(f"Not overwriting existing file: `{path}`")
        else:
            logging.info(f"Creating new file: `{path}`")
            with open(path, "w") as fp:
                fp.write(output + "\n")

        logging.info("Done")

    def run(self) -> None:
        response = self.fetch_page()
        soup = self.extract_game_data(response)
        puzzle = self.parse_game_data(soup)
        self.output_game_data(puzzle)


def main() -> None:  # pragma: no cover
    nyts: NYTimesScraper = NYTimesScraper()
    nyts.run()


if __name__ == "__main__":
    main()
