import random
import string
class Game:
    """Docstring"""
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = [random.choice(string.ascii_uppercase) for _ in range(9)]


    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        lst_word = [x for x in word]

        for letters in self.grid:
            if letters in lst_word:
                lst_word.remove(letters)

        if len(lst_word) > len(self.grid):
            return False
        elif len(lst_word) >= 1:
            return False
        else:
            return True
