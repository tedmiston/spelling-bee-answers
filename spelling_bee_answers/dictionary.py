from typing import List

import yaml
from pydantic import BaseModel
from rich import print


class Word(BaseModel):
    word: str
    part_of_speech: str
    definitions: List[str]


def load_definitions():
    with open("data/definitions.yml") as fp:
        obj = yaml.safe_load(fp)
    # print(obj)

    words_list = obj["words"]
    # print(words_list)

    words_dict = {x["word"]: x for x in words_list}
    # print(words_dict)

    return words_dict


def lookup_word(words_dict, query):
    word_result = words_dict.get(query)

    if word_result is not None:
        # print(word_result)
        word = Word(
            word=word_result.get("word"),
            part_of_speech=word_result.get("part"),
            definitions=word_result.get("defs"),
        )
        # print(word)
        return word
    else:
        pass


def main():
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
