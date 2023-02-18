"""
Interfaces.
"""

import abc
from typing import Any

import requests
from bs4 import BeautifulSoup

from .models import Puzzle


class SpellingBeeScraperInterface(metaclass=abc.ABCMeta):
    """
    A Spelling Bee scraper interface.
    """

    @abc.abstractmethod
    def fetch_page(self, url: str) -> requests.Response:
        raise NotImplementedError

    @abc.abstractmethod
    def extract_game_data(self, response: requests.Response) -> BeautifulSoup:
        raise NotImplementedError

    @abc.abstractmethod
    # def parse_game_data(self, soup: BeautifulSoup) -> Puzzle:
    def parse_game_data(self, soup: BeautifulSoup) -> Any:
        raise NotImplementedError

    @abc.abstractmethod
    def output_game_data(self, puzzle: Puzzle) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def run(self) -> None:
        raise NotImplementedError
