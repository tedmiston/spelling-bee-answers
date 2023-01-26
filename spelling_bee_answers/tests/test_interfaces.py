"""
Unit tests - interfaces.
"""

from ..interfaces import SpellingBeeScraperInterface


def test_SpellingBeeScraperInterface():
    class FooScraper(SpellingBeeScraperInterface):
        """
        A trivial implementation of the SpellingBeeScraperInterface.
        """

        def fetch_page(url):
            pass

        def extract_game_data(response):
            pass

        def parse_game_data(soup):
            pass

        def output_game_data(puzzle):
            pass

        def run(self):
            pass

    foo = FooScraper()
    assert isinstance(foo, SpellingBeeScraperInterface)
