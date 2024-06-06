# tests/test_game.py
import random
import string
import unittest
from longest_word.game import Game

class TestGame(unittest.TestCase):
    """Docstring"""
    def test_game_initialization(self):
            """Docstring"""
            # setup
            game = Game()
            # Exercice
            grid_word = game.grid
            # verify
            self.assertLessEqual(len(grid_word),9,"The lenght of the word is above 9")
            self.assertIs(type(grid_word),list,"not a list!")

    def test_is_valid(self):
            """Doctstring"""

            grid_word = [x for x in "OQUWRBAZE"]

            my_word = [x for x in "BAROQUE"]

            for letters in grid_word:
                if letters in my_word:
                    my_word.remove(letters)

            self.assertLessEqual(len(my_word),len(grid_word))
            self.assertEqual(len(my_word),0)