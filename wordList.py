from typing import List


class WordList:
    def __init__(self, path) -> None:
        self.words: List = []
        self.loaded = False
        self.path = path




all_words = []
target_words = []

target_words_path = ""

def load_word_list(file_name: str):
    with open(file_name, "r") as f:
        return f.read().split()

def get_target_word():
    if len(target_words) == 0:
        target_words = load_word_list()

        if len(target_words) == 0:
            raise RuntimeError(f"The word list loaded zero words")





