"""
Interfaces.
"""

import abc


class SpellingBeeScraperInterface(metaclass=abc.ABCMeta):
    """
    A Spelling Bee scraper interface.
    """

    @abc.abstractmethod
    def fetch_page(self, url):
        raise NotImplementedError

    @abc.abstractmethod
    def extract_game_data(self, response):
        raise NotImplementedError

    @abc.abstractmethod
    def parse_game_data(self, soup):
        raise NotImplementedError

    @abc.abstractmethod
    def output_game_data(self, puzzle):
        raise NotImplementedError

    @abc.abstractmethod
    def run(self):
        raise NotImplementedError
