from player import Player
from inputOutput import Input_output
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

    def test_count_cards(self):
        deck = [["diamond", 1], ["diamond", 13], ["heart", 13]]
        self.player1.set_deck(deck)
        self.assertEqual(Game.count_cards(self, self.player1), 3)

    def test_flip_4_times(self):
        deck = [["diamond", 1], ["diamond", 13], ["heart", 13],
                ["diamond", 13], ["heart", 13]]
        self.player1.set_deck(deck)
        deck2 = [["diamond", 1], ["diamond", 13], ["heart", 13],
                 ["diamond", 8], ["heart", 13]]
        self.player2.set_deck(deck2)
        war_card1, war_card2 = self.game.flip_4_times(self.player1,
                                                      self.player2, self.inOut)
        self.assertEqual(war_card1, 13)
        self.assertEqual(war_card2, 8)

    def test_increase_chance(self):
        deck = [["diamond", 1], ["diamond", 13], ["heart", 13],
                ["spades", 13], ["diamonds", 11]]
        self.player1.set_deck(deck)
        deck2 = [["diamond", 1], ["diamond", 13], ["heart", 13],
                 ["diamond", 8], ["heart", 13]]
        self.player2.set_deck(deck2)
        self.game.increase_chance(self.player1, self.player2, 1)
        test_1 = [["diamond", 13], ["diamond", 1], ["heart", 13],
                  ["spades", 13], ["diamonds", 11]]
        self.assertEqual(self.player1.get_card_list(), test_1)
        self.game.increase_chance(self.player1, self.player2, 2)
        test_2 = [["diamond", 13], ["diamond", 1], ["heart", 13],
                  ["diamond", 8], ["heart", 13]]
        self.assertEqual(self.player2.get_card_list(), test_2)

    def test_chk_player_won_round(self):
        pass


if __name__ == "__main__":
    unittest.main()
