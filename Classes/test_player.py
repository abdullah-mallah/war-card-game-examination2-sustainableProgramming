"""
This script is used to test class Player.

Authors: Abdullah Mallah, Eszter Kalmar and Hampus Gunnarsson.
"""
import unittest
from player import Player


class TestPlayer(unittest.TestCase):
    """Responsible for tests of class Player."""

    def setUp(self):
        """Create objects before each test method."""
        self.player1 = Player("player1", "0", "0", "0.0")
        self.player2 = Player("player2", "0", "0", "0.0")

    def test_activate_intelligence_2(self):
        """Test the method to check player's deck after rearranging it."""
        test_deck = [["diamond", 1], ["diamond", 13], ["heart", 13]]
        self.player2.set_deck(test_deck)
        test_deck2 = [["diamond", 13], ["diamond", 1], ["heart", 13]]
        self.player2.activate_intelligence_2()
        self.assertEqual(self.player2.get_card_list(), test_deck2)

    def test_activate_intelligence_3(self):
        """Test the method to check player's deck after rearranging it."""
        test_deck = [["diamond", 1], ["diamond", 13], ["heart", 13]]
        self.player2.set_deck(test_deck)
        test_deck2 = [["diamond", 13], ["heart", 13], ["diamond", 1]]
        self.player2.activate_intelligence_3()
        self.assertEqual(self.player2.get_card_list(), test_deck2)

    def test_get_next_card(self):
        """Test the method to check player's deck after taking one card."""
        test_deck = [["spades", 1], ["spades", 2], ["spades", 3],
                     ["spades", 4]]
        test_temp = [["spades", 1]]
        test_deck2 = [["spades", 2], ["spades", 3], ["spades", 4]]
        self.player2.set_deck(test_deck)
        self.assertEqual(self.player2.get_next_card(), 1)
        self.assertEqual(self.player2.get_temp(), test_temp)
        self.assertEqual(self.player2.get_card_list(), test_deck2)

    def test_add_temp_list_to_deck(self):
        """Test the method to check player's deck after adding one card."""
        deck = [["spades", 3], ["spades", 4]]
        self.player2.set_deck(deck)
        temp_list1 = [["spades", 1]]
        temp_list2 = [["spades", 2]]
        deck2 = [["spades", 3], ["spades", 4], ["spades", 1], ["spades", 2]]
        self.player2.add_temp_list_to_deck(temp_list1, temp_list2)
        self.assertEqual(self.player2.get_card_list(), deck2)

    def test_empty_temp(self):
        """Test the method to check player's temp_deck after emptying it."""
        test = [["spades", 3], ["spades", 4]]
        self.player1.set_temp_deck(test)
        self.player1.empty_temp()
        self.assertEqual(self.player1.get_temp(), [])

    def test_count_cards(self):
        """Test the method to check player deck's length."""
        deck = [["spades", 3], ["spades", 4]]
        self.player1.set_deck(deck)
        self.player2.set_deck(deck)
        self.assertEqual(self.player1.count_cards(), 2)
        self.assertEqual(self.player2.count_cards(), 2)

    def test_steal_1_card(self):
        """Test the method to check player's deck after stealing one card."""
        test = [["spades", 3], ["spades", 4]]
        self.player1.set_deck(test)
        self.assertEqual(self.player1.steal_1_card(0), ["spades", 3])
        test2 = [["spades", 3], ["spades", 4]]
        self.player1.set_deck(test2)
        self.assertEqual(self.player1.steal_1_card(1), ["spades", 4])

    def test_add_1_card(self):
        """Test the method to check player's deck after adding one card."""
        card = ["diamonds", 1]
        deck = [["spades", 3], ["spades", 4]]
        test = [["spades", 3], ["spades", 4], ["diamonds", 1]]
        self.player1.set_deck(deck)
        self.player1.add_1_card(card)
        self.assertEqual(self.player1.get_card_list(), test)

    def test_get_card_list(self):
        """Test the get_card_list method of the InputOutput class."""
        deck = [["spades", 3], ["spades", 4]]
        self.player1.set_deck(deck)
        self.assertEqual(self.player1.get_card_list(), deck)

    def test_get_temp(self):
        """Test the get_temp method of the Player class."""
        deck = [["spades", 3], ["spades", 4]]
        self.player1.set_temp_deck(deck)
        self.assertEqual(self.player1.get_temp(), deck)

    def test_get_name(self):
        """Test the get_name method of the Player class.."""
        self.player1.set_name("test_name")
        self.assertEqual(self.player1.get_name(), "test_name")

    def test_get_wins(self):
        """Test the get_wins method of the Player class."""
        self.player1.set_wins("5")
        self.assertEqual(self.player1.get_wins(), "5")

    def test_get_percentage(self):
        """Test the get_percentage method of the Player class."""
        self.player1.set_percentage("6")
        self.assertEqual(self.player1.get_percentage(), "6")

    def test_get_times_played(self):
        """Test the get_times_played method of the Player class."""
        self.player1.set_times_played("7")
        self.assertEqual(self.player1.get_times_played(), "7")

    def test_set_times_played(self):
        """Test the set_times_played method of the Player class."""
        self.player1.set_times_played("6")
        self.assertEqual(self.player1.get_times_played(), "6")

    def test_set_wins(self):
        """Test the set_wins method of the Player class."""
        self.player1.set_wins("6")
        self.assertEqual(self.player1.get_wins(), "6")

    def test_set_deck(self):
        """Test the set_deck method of the Player class."""
        deck = [["spades", 3], ["spades", 4]]
        self.player1.set_deck(deck)
        self.assertEqual(self.player1.get_card_list(), deck)

    def test_set_temp_deck(self):
        """Test the set_temp_deck method of the Player class."""
        deck = [["spades", 3], ["spades", 4]]
        self.player1.set_temp_deck(deck)
        self.assertEqual(self.player1.get_temp(), deck)

    def test_set_name(self):
        """Test the set_wins method of the Player class."""
        self.player1.set_name("test_name")
        self.assertEqual(self.player1.get_name(), "test_name")

    def test_set_percentage(self):
        """Test the set_wins method of the Player class."""
        self.player1.set_percentage("50.0")
        self.assertEqual(self.player1.get_percentage(), "50.0")


if __name__ == "__main__":
    unittest.main()
