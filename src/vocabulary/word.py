from pydantic import BaseModel
import csv


class Word(BaseModel):
    theme: str
    french: str
    japanese: str
    hiragana: str
    romanji: str


def read_vocabulary() -> list[Word]:
    words = []
    with open("data/vocabulary.txt") as f:
        rows = csv.DictReader(f, delimiter=',')
        for row in rows:
            words.append(Word(**row))
    return words
