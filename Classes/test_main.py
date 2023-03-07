"""
This script is used to test main.py.

Authors: Abdullah Mallah, Eszter Kalmar and Hampus Gunnarsson.
"""
import unittest
import main


class TestMain(unittest.TestCase):
    """Responsible for tests of methods in main.py."""

    def test_create_deck_clubs(self):
        """Test the method to check the returned list."""
        test_clubs = [["clubs", 1], ["clubs", 2], ["clubs", 3], ["clubs", 4],
                      ["clubs", 5], ["clubs", 6], ["clubs", 7], ["clubs", 8],
                      ["clubs", 9], ["clubs", 10], ["clubs", 11],
                      ["clubs", 12], ["clubs", 13]]
        self.assertEqual(main.create_deck_clubs(), test_clubs)

    def test_create_deck_diamonds(self):
        """Test the method to check the returned list."""
        test_diamonds = [["diamonds", 1], ["diamonds", 2], ["diamonds", 3],
                         ["diamonds", 4], ["diamonds", 5], ["diamonds", 6],
                         ["diamonds", 7], ["diamonds", 8], ["diamonds", 9],
                         ["diamonds", 10], ["diamonds", 11], ["diamonds", 12],
                         ["diamonds", 13]]
        self.assertEqual(main.create_deck_diamonds(), test_diamonds)

    def test_create_deck_hearts(self):
        """Test the method to check the returned list."""
        test_hearts = [["hearts", 1], ["hearts", 2], ["hearts", 3],
                       ["hearts", 4], ["hearts", 5], ["hearts", 6],
                       ["hearts", 7], ["hearts", 8], ["hearts", 9],
                       ["hearts", 10], ["hearts", 11], ["hearts", 12],
                       ["hearts", 13]]
        self.assertEqual(main.create_deck_hearts(), test_hearts)

    def test_create_deck_spades(self):
        """Test the method to check the returned list."""
        test_spades = [["spades", 1], ["spades", 2], ["spades", 3],
                       ["spades", 4], ["spades", 5], ["spades", 6],
                       ["spades", 7], ["spades", 8], ["spades", 9],
                       ["spades", 10], ["spades", 11], ["spades", 12],
                       ["spades", 13]]
        self.assertEqual(main.create_deck_spades(), test_spades)


if __name__ == "__main__":
    unittest.main()
