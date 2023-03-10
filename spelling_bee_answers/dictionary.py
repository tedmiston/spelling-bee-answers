"""
The dictionary provides definitions of words.
"""

from rich import print

from .definitions import words


def load_definitions():
    """
    Generate a dictionary of definitions of words.
    """
    words_dict = {x.word: x for x in words}

    # if this fails, a word has been duplicated in the definitions file
    assert len(words) == len(words_dict)

    return words_dict


def lookup_word(words_dict, query):
    """
    Query the dictionary.
    """
    word_result = words_dict.get(query)
    return word_result


def main():
    """
    Entrypoint for development of the dictionary.
    """
    words_dict = load_definitions()

    query = "aground"
    # query = "potato"
    word = lookup_word(words_dict, query)

    if word is not None:
        print(f"{word.word} *{word.part_of_speech}*")
        for definition in word.definitions:
            print(f"- {definition}")
    else:
        print(f'no definition found for query "{query}"')


if __name__ == "__main__":
    main()
