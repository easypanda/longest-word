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

            # setup
            game = Game()
            # Exercice
            game.grid = list("OQUWRBAZE")

            my_word = list("BAROQUE")

            for letters in game.grid:
                if letters in my_word:
                    my_word.remove(letters)

            self.assertLessEqual(len(my_word),len(game.grid))
            self.assertEqual(len(my_word),0)

    def test_unknown_word_is_invalid(self):
            """A word that is not in the English dictionary should not be valid"""
            new_game = Game()
            new_game.grid = list('KWIENFUQW') # Force the grid to a test case:
            assert new_game.is_valid('FEUN') is False
