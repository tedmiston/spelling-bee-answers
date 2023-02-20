"""
Unit tests - interfaces.
"""


from ..interfaces import SpellingBeeScraperInterface


def test_SpellingBeeScraperInterface():
    """
    Test the interface for scrapers of Spelling Bee puzzles.
    """

    class FooScraper(SpellingBeeScraperInterface):
        """
        A trivial implementation of the SpellingBeeScraperInterface.
        """

        def fetch_page(self, url):
            """
            Fetch the contents of the page at the given URL.
            """
            pass

        def extract_game_data(self, response):
            """
            Parse the webpage extracting the JavaScript game data.
            """
            pass

        def parse_game_data(self, soup):
            """
            Parse the yesterday game data from JavaScript into a Python object.
            """
            pass

        def output_game_data(self, puzzle):
            """
            Write the game data to disk.
            """
            pass

        def run(self):
            """
            Entrypoint for running the above functions.
            """
            pass

    foo = FooScraper()
    assert isinstance(foo, SpellingBeeScraperInterface)
    # todo: implement
