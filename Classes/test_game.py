from player import Player
from inputOutput import Input_output
from unittest.mock import patch
from fileReaderWriter import FileRW
from game import Game
import random
import unittest


class Test_game(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("player1", "0", "0", "0.0")
        self.player2 = Player("player2", "0", "0", "0.0")
        self.inOut = Input_output()
        self.game = Game()
        self.fileRW = FileRW("score.txt")

    def test_flip_4_times(self):
        with unittest.mock.patch('builtins.print') as mock_print:
            deck = [["diamond", 1], ["diamond", 13], ["heart", 13],
                    ["diamond", 13], ["heart", 13]]
            self.player1.set_deck(deck)
            deck2 = [["diamond", 1], ["diamond", 13], ["heart", 13],
                     ["diamond", 8], ["heart", 13]]
            self.player2.set_deck(deck2)
            war_card1, war_card2 = self.game.flip_4_times(self.player1,
                                                          self.player2,
                                                          self.inOut)
            self.inOut.flipped_card(war_card1,
                                    self.player1.get_name(),
                                    self.player1.count_cards())
            self.inOut.flipped_card(war_card1,
                                    self.player2.get_name(),
                                    self.player2.count_cards())
            self.assertEqual(war_card1, 13)
            self.assertEqual(war_card2, 8)
            mock_print.assert_has_calls([
                unittest.mock.call("flipped 4 times")
            ])

    # @patch("inputOutput.Input_output.lvl_game_menu_input", return_value="1")
    # def test_flip_once(self, input):
    #     with unittest.mock.patch('builtins.print') as mock_print:
    #         deck = [["diamond", 1], ["diamond", 13], ["heart", 13],
    #                 ["diamond", 13], ["heart", 13]]
    #         self.player1.set_deck(deck)
    #         deck2 = [["diamond", 1], ["diamond", 13], ["heart", 13],
    #                  ["diamond", 8], ["heart", 13]]
    #         self.player2.set_deck(deck2)
    #         self.inOut.lvl_game_menu_input()
    #         war_card1, war_card2 = self.game.flip_once(self.player1,
    #                                                    self.player2,
    #                                                    self.inOut)
    #         self.assertEqual(war_card1, 1)
    #         self.assertEqual(war_card2, 1)
    #         mock_print.assert_has_calls([
    #             unittest.mock.call("flipped once")
    #         ])

    def test_steal_1_card(self):
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

    def test_increase_chance(self):
        deck = [["diamond", 1], ["diamond", 10], ["heart", 13],
                ["spades", 13], ["diamonds", 11]]
        self.player1.set_deck(deck)
        deck2 = [["diamond", 1], ["diamond", 13], ["heart", 13],
                 ["diamond", 8], ["heart", 13]]
        self.player2.set_deck(deck2)
        self.game.increase_chance(self.player1, self.player2, 1)
        self.game.increase_chance(self.player1, self.player2, 1)
        test_1 = [["diamond", 1], ["heart", 13], ["diamond", 10],
                  ["spades", 13], ["diamonds", 11]]
        self.assertEqual(self.player1.get_card_list(), test_1)

    def test_chk_player_won_round(self):
        self.assertEqual(self.game.chk_player_won_round(1, 2), 1)
        self.assertEqual(self.game.chk_player_won_round(1, 1), 0)
        self.assertEqual(self.game.chk_player_won_round(2, 1), 2)
        self.assertEqual(self.game.chk_player_won_round(10, 2), 1)
        self.assertEqual(self.game.chk_player_won_round(2, 3), 2)
        self.assertEqual(self.game.chk_player_won_round(3, 3), 0)

    def test_add_cards_to_round_winner(self):
        with unittest.mock.patch('builtins.print') as mock_print:
            deck = [["diamond", 1], ["diamond", 13], ["heart", 13],
                    ["spades", 13], ["diamonds", 11]]
            self.player1.set_deck(deck)
            deck2 = [["diamond", 2]]
            self.player2.set_deck(deck2)
            self.game.flip_once_auto(self.player1, self.player2, self.inOut)
            test_list = [["diamond", 13], ["heart", 13], ["spades", 13],
                         ["diamonds", 11], ["diamond", 1], ["diamond", 2]]
            self.game.add_cards_to_round_winner(self.player1, self.player2, 1)
            mock_print.assert_has_calls([
                unittest.mock.call(f"\n{self.player1.get_name().capitalize()} "
                                   f"won this round")
            ])
            self.assertEqual(self.player1.get_card_list(), test_list)

    def test_flipp_once(self):
        deck = [["diamond", 1], ["diamond", 13], ["heart", 13],
                ["spades", 13], ["diamonds", 11]]
        self.player1.set_deck(deck)
        self.assertEqual(self.game.flipp_once(self.player1), 1)

    def test_flip_once_auto(self):
        with unittest.mock.patch('builtins.print') as mock_print:
            deck = [["diamond", 1], ["diamond", 13], ["heart", 13],
                    ["spades", 13], ["diamonds", 11]]
            self.player1.set_deck(deck)
            deck2 = [["diamond", 2]]
            self.player2.set_deck(deck2)
            self.game.flip_once_auto(self.player1, self.player2, self.inOut)
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
