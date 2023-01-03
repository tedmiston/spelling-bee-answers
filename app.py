"""
NYTimes Spelling Bee answers.

Fetch the Yesterday's Answers to the NYTimes Spelling Bee puzzle each day for archival purposes.
"""

import datetime
import json
import logging
import re
from pprint import pprint

import requests
from bs4 import BeautifulSoup

logging.basicConfig(
    level=logging.INFO,
)


def fetch_page():
    logging.info("Fetching puzzle")

    url = "https://www.nytimes.com/puzzles/spelling-bee"
    response = requests.get(url)

    return response


def extract_game_data(response):
    logging.info("Extracting game data")

    if not response.ok:
        raise Exception("HTTP response code was not successful")

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

    pprint(yesterday_dict["yesterday"], sort_dicts=False)

    return yesterday_dict["yesterday"]


def output_game_answers_data(yesterday_dict):
    logging.info("Writing game data")

    yesterday_date = datetime.date.today() - datetime.timedelta(days=1)
    output = json.dumps(yesterday_dict, indent=2)
    with open(f"days/{yesterday_date}.json", "w") as fp:
        fp.write(output + "\n")


def main():
    response = fetch_page()
    game_data_script = extract_game_data(response)
    yesterday_dict = parse_game_data(game_data_script)
    output_game_answers_data(yesterday_dict)


if __name__ == "__main__":
    main()
