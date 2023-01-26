"""
NYTimes Spelling Bee answers.

Fetch the Yesterday's Answers to the NYTimes Spelling Bee puzzle each day for archival purposes.
"""

import json
import logging
import re
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from rich import print

from .settings import settings

logging.basicConfig(
    level=logging.INFO,
)


def fetch_page():
    logging.info("Fetching puzzle")

    url = "https://www.nytimes.com/puzzles/spelling-bee"
    response = requests.get(url)

    if not response.ok:
        raise Exception("HTTP response code was not successful")

    return response


def extract_game_data(response):
    logging.info("Extracting game data")

    soup = BeautifulSoup(response.content, "html.parser")
    game_data_script = soup.find("script", string=re.compile("^window.gameData.*"))

    if not game_data_script:
        raise Exception("Game data script was not found")

    return game_data_script


def parse_game_data(game_data_script):
    logging.info("Parsing game data")

    yesterday_start_index = game_data_script.text.find('"yesterday"')
    yesterday_script_text = game_data_script.text[yesterday_start_index:]
    yesterday_end_index = yesterday_script_text.find("}") + 1
    yesterday_script_text = yesterday_script_text[:yesterday_end_index]

    if yesterday_start_index < 0 or yesterday_end_index < 0:
        raise Exception("Yesterday game data could not be parsed")

    try:
        yesterday_dict = json.loads("{" + yesterday_script_text + "}")
    except json.decoder.JSONDecodeError:
        raise Exception("JSON decoding of yesterday game data failed")

    if settings.display_puzzle_output:
        print(yesterday_dict["yesterday"])

    return yesterday_dict["yesterday"]


def output_game_data(puzzle_dict):
    logging.info("Writing game data")

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


def main():  # pragma: no cover
    response = fetch_page()
    game_data_script = extract_game_data(response)
    puzzle_dict = parse_game_data(game_data_script)
    output_game_data(puzzle_dict)


if __name__ == "__main__":
    main()
