import unittest
#  import sys
#  sys.path.insert(0, 'c:\\Users\\a\\Desktop\\training-on-testing\\
#                  war-card-game-examination2-sustainableProgramming')
from player import Player


class Test_player(unittest.TestCase):
    #  def test_add(self):
    #      list_1 = [1, 2]
    #      results = Player.check_cards_left(self, list_1)
    #      self.assertEqual(results, True)
    #      #  testing error
    #      self.assertRaises(ValueError, Player.check_cards_left, 1, 2)
    #      # testing error using context manager
    #      with self.assertRaises(ValueError):
    #          Player.check_cards_left(1, 2)

    def setUp(self):
        self.player1 = Player("player1", "0", "0", "0.0")
        self.player2 = Player("player2", "0", "0", "0.0")

    def test_activate_intelligence_2(self):
        test_deck = [["diamond", 1], ["diamond", 13], ["heart", 13]]
        self.player2.set_deck(test_deck)
        test_deck2 = [["diamond", 13], ["diamond", 1], ["heart", 13]]
        self.player2.activate_intelligence_2()
        self.assertEqual(self.player2.get_card_list(), test_deck2)

    def test_activate_intelligence_3(self):
        test_deck = [["diamond", 1], ["diamond", 13], ["heart", 13]]
        self.player2.set_deck(test_deck)
        test_deck2 = [["diamond", 13], ["heart", 13], ["diamond", 1]]
        self.player2.activate_intelligence_3()
        self.assertEqual(self.player2.get_card_list(), test_deck2)

    #  def test_create_deck1(self):
    #      test_deck = [["clubs", 1], ["clubs", 2], ["clubs", 3], ["clubs", 4],
    #                   ["clubs", 5], ["clubs", 6], ["clubs", 7], ["clubs", 8],
    #                   ["clubs", 9], ["clubs", 10], ["clubs", 11], ["clubs", 12],
    #                   ["clubs", 13], ["diamonds", 1], ["diamonds", 2],
    #                   ["diamonds", 3], ["diamonds", 4], ["diamonds", 5],
    #                   ["diamonds", 6], ["diamonds", 7], ["diamonds", 8],
    #                   ["diamonds", 9], ["diamonds", 10], ["diamonds", 11],
    #                   ["diamonds", 12], ["diamonds", 13]]
    #      self.assertEqual(self.player1.get_card_list(), test_deck)
#  
    #  def test_create_deck2(self):
    #      test_deck = [["hearts", 1], ["hearts", 2], ["hearts", 3],
    #                   ["hearts", 4], ["hearts", 5], ["hearts", 6],
    #                   ["hearts", 7], ["hearts", 8], ["hearts", 9],
    #                   ["hearts", 10], ["hearts", 11], ["hearts", 12],
    #                   ["hearts", 13], ["spades", 1], ["spades", 2],
    #                   ["spades", 3], ["spades", 4], ["spades", 5],
    #                   ["spades", 6], ["spades", 7], ["spades", 8],
    #                   ["spades", 9], ["spades", 10], ["spades", 11],
    #                   ["spades", 12], ["spades", 13]]
    #      self.assertEqual(self.player2.get_card_list(), test_deck)

    def test_check_cards_left(self):
        test_list = [["spades", 1], ["spades", 2]]
        test_list2 = []
        self.assertEqual(Player.check_cards_left(self, test_list), True)
        self.assertEqual(Player.check_cards_left(self, test_list2), False)

    def test_get_next_card(self):
        test_deck = [["spades", 1], ["spades", 2], ["spades", 3],
                     ["spades", 4]]
        test_temp = [["spades", 1]]
        test_deck2 = [["spades", 2], ["spades", 3], ["spades", 4]]
        self.player2.set_deck(test_deck)
        self.assertEqual(self.player2.get_next_card(), 1)
        self.assertEqual(self.player2.get_temp(), test_temp)
        self.assertEqual(self.player2.get_card_list(), test_deck2)

    def test_add_temp_list_to_deck(self):
        deck = [["spades", 3], ["spades", 4]]
        self.player2.set_deck(deck)
        temp_list1 = [["spades", 1]]
        temp_list2 = [["spades", 2]]
        self.player2.set_deck(deck)
        deck2 = [["spades", 3], ["spades", 4], ["spades", 1], ["spades", 2]]
        self.player2.add_temp_list_to_deck(temp_list1, temp_list2)
        self.assertEqual(self.player2.get_card_list(), deck2)

    def test_empty_temp(self):
        test = [["spades", 3], ["spades", 4]]
        self.player1.set_temp_deck(test)
        self.player1.empty_temp()
        self.assertEqual(self.player1.get_temp(), [])

    def test_count_cards(self):
        deck = [["spades", 3], ["spades", 4]]
        self.player1.set_deck(deck)
        self.player2.set_deck(deck)
        self.assertEqual(self.player1.count_cards(), 2)
        self.assertEqual(self.player2.count_cards(), 2)

    def test_steal_1_card(self):
        test = [["spades", 3], ["spades", 4]]
        self.player1.set_deck(test)
        self.assertEqual(self.player1.steal_1_card(0), ["spades", 3])
        test2 = [["spades", 3], ["spades", 4]]
        self.player1.set_deck(test2)
        self.assertEqual(self.player1.steal_1_card(1), ["spades", 4])

    def test_add_1_card(self):
        card = ["diamonds", 1]
        deck = [["spades", 3], ["spades", 4]]
        test = [["spades", 3], ["spades", 4], ["diamonds", 1]]
        self.player1.set_deck(deck)
        self.player1.add_1_card(card)
        self.assertEqual(self.player1.get_card_list(), test)

    def test_increase_chance(self):
        test_deck = [["diamond", 1], ["diamond", 8], ["heart", 9]]
        self.player2.set_deck(test_deck)
        test_deck2 = [["heart", 9], ["diamond", 1], ["diamond", 8]]
        self.player2.increase_chance()
        self.assertEqual(self.player2.get_card_list(), test_deck2)
        test_deck3 = [["heart", 9], ["diamond", 8], ["diamond", 1]]
        self.player2.increase_chance()
        self.assertEqual(self.player2.get_card_list(), test_deck3)


if __name__ == "__main__":
    unittest.main()
