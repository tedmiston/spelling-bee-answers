"""
Unit tests - interfaces.
"""

from ..interfaces import SpellingBeeScraperInterface


def test_SpellingBeeScraperInterface():
    class FooScraper(SpellingBeeScraperInterface):
        """
        A trivial implementation of the SpellingBeeScraperInterface.
        """

        def fetch_page(self, url):
            pass

        def extract_game_data(self, response):
            pass

        def parse_game_data(self, soup):
            pass

        def output_game_data(self, puzzle):
            pass

        def run(self):
            pass

    foo = FooScraper()
    assert isinstance(foo, SpellingBeeScraperInterface)
