"""
This script is used to test class Game.

Authors: Abdullah Mallah, Eszter Kalmar and Hampus Gunnarsson.
"""
import unittest
import unittest.mock
from player import Player
from input_output import InputOutput
from game import Game


class TestGame(unittest.TestCase):
    """Responsible for tests of class Game."""

    def setUp(self):
        """Create objects before each test method."""
        self.player1 = Player("player1", "0", "0", "0.0")
        self.player2 = Player("player2", "0", "0", "0.0")
        self.in_out = InputOutput()
        self.game = Game()

    def test_flip_4_times(self):
        """Test the method to check the 4'th flipped card's number."""
        with unittest.mock.patch('builtins.print') as mock_print:
            deck = [["diamond", 1], ["diamond", 13], ["heart", 13],
                    ["diamond", 13], ["heart", 13]]
            self.player1.set_deck(deck)
            deck2 = [["diamond", 1], ["diamond", 13], ["heart", 13],
                     ["diamond", 8], ["heart", 13]]
            self.player2.set_deck(deck2)
            war_card1, war_card2 = self.game.flip_4_times(self.player1,
                                                          self.player2,
                                                          self.in_out)
            self.in_out.flipped_card(war_card1,
                                     self.player1.get_name(),
                                     self.player1.count_cards())
            self.in_out.flipped_card(war_card1,
                                     self.player2.get_name(),
                                     self.player2.count_cards())
            self.assertEqual(war_card1, 13)
            self.assertEqual(war_card2, 8)
            mock_print.assert_has_calls([
                unittest.mock.call("Flipped 4 times")
            ])

    def test_steal_1_card(self):
        """Test the method to check player's deck stealing one card."""
        deck = [["diamond", 1], ["diamond", 13], ["heart", 13],
                ["diamond", 13], ["heart", 13]]
        self.player1.set_deck(deck)
        deck2 = [["diamond", 1]]
        test_list = [["diamond", 1], ["diamond", 13], ["heart", 13],
                     ["diamond", 13], ["heart", 13], ["diamond", 1]]
        self.player2.set_deck(deck2)
        self.game.steal_1_card(self.player1, self.player2, 1)
        self.assertEqual(self.player1.get_card_list(), test_list)

        deck3 = [["diamond", 1], ["diamond", 13], ["heart", 13],
                 ["diamond", 13], ["heart", 13]]
        self.player2.set_deck(deck3)
        deck4 = [["diamond", 1]]
        self.player1.set_deck(deck4)
        test_list2 = [["diamond", 1], ["diamond", 13], ["heart", 13],
                      ["diamond", 13], ["heart", 13], ["diamond", 1]]
        self.game.steal_1_card(self.player1, self.player2, 2)
        self.assertEqual(self.player2.get_card_list(), test_list2)

    # def test_increase_chance(self):
    #     """Test the method to check the order of player's deck."""
    #     deck = [["diamond", 1], ["diamond", 10], ["heart", 13],
    #             ["spades", 13], ["diamonds", 11]]
    #     self.player1.set_deck(deck)
    #     deck2 = [["diamond", 1], ["diamond", 13], ["heart", 13],
    #              ["diamond", 8], ["heart", 13]]
    #     self.player2.set_deck(deck2)
    #     self.game.increase_chance(self.player1, self.player2, 1)
    #     self.game.increase_chance(self.player1, self.player2, 1)
    #     test_1 = [["diamond", 1], ["heart", 13], ["diamond", 10],
    #               ["spades", 13], ["diamonds", 11]]
    #     self.assertEqual(self.player1.get_card_list(), test_1)

    def test_chk_player_won_round(self):
        """Test the method to check which player won the war flipp."""
        self.assertEqual(self.game.chk_player_won_round(1, 2), 1)
        self.assertEqual(self.game.chk_player_won_round(1, 1), 0)
        self.assertEqual(self.game.chk_player_won_round(2, 1), 2)
        self.assertEqual(self.game.chk_player_won_round(10, 2), 1)
        self.assertEqual(self.game.chk_player_won_round(2, 3), 2)
        self.assertEqual(self.game.chk_player_won_round(3, 3), 0)

    def test_add_cards_to_round_winner(self):
        """Test the method to check deck of a player after add cards to it."""
        with unittest.mock.patch('builtins.print') as mock_print:
            deck = [["diamond", 1], ["diamond", 13], ["heart", 13],
                    ["spades", 13], ["diamonds", 11]]
            self.player1.set_deck(deck)
            deck2 = [["diamond", 2]]
            self.player2.set_deck(deck2)
            self.game.flip_1_auto(self.player1, self.player2, self.in_out)
            test_list = [["diamond", 13], ["heart", 13], ["spades", 13],
                         ["diamonds", 11], ["diamond", 1], ["diamond", 2]]
            self.game.add_cards_to_round_winner(self.player1, self.player2, 1)
            mock_print.assert_has_calls([
                unittest.mock.call(f"\n{self.player1.get_name().capitalize()} "
                                   f"won this round")
            ])
            self.assertEqual(self.player1.get_card_list(), test_list)

    def test_flipp_once(self):
        """Test the method to check the flipped card from the player's deck."""
        deck = [["diamond", 1], ["diamond", 13], ["heart", 13],
                ["spades", 13], ["diamonds", 11]]
        self.player1.set_deck(deck)
        self.assertEqual(self.game.flipp_once(self.player1), 1)

    def test_flip_once_auto(self):
        """Test the method to check player's deck after a flipp."""
        with unittest.mock.patch('builtins.print') as mock_print:
            deck = [["diamond", 1], ["diamond", 13], ["heart", 13],
                    ["spades", 13], ["diamonds", 11]]
            self.player1.set_deck(deck)
            deck2 = [["diamond", 2]]
            self.player2.set_deck(deck2)
            self.game.flip_1_auto(self.player1, self.player2, self.in_out)
            test_list = [["diamond", 13], ["heart", 13], ["spades", 13],
                         ["diamonds", 11], ["diamond", 1], ["diamond", 2]]
            self.game.add_cards_to_round_winner(self.player1, self.player2, 1)
            mock_print.assert_has_calls([
                unittest.mock.call(f"\n{self.player1.get_name().capitalize()} "
                                   f"won this round")
            ])
            self.assertEqual(self.player1.get_card_list(), test_list)


if __name__ == "__main__":
    unittest.main()
