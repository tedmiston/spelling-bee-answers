"""
Interfaces.
"""

import abc


class SpellingBeeScraperInterface(metaclass=abc.ABCMeta):
    """
    The interface for scrapers of Spelling Bee puzzles.
    """

    @abc.abstractmethod
    def fetch_page(self, url):
        """
        Fetch the contents of the page at the given URL.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def extract_game_data(self, response):
        """
        Parse the webpage extracting the JavaScript game data.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def parse_game_data(self, soup):
        """
        Parse the yesterday game data from JavaScript into a Python object.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def output_game_data(self, puzzle):
        """
        Write the game data to disk.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def run(self):
        """
        Entrypoint for running the above functions.
        """
        raise NotImplementedError
