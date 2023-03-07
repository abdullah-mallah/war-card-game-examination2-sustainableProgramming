import unittest
#  import sys
#  sys.path.insert(0, 'c:\\Users\\a\\Desktop\\training-on-testing\\
#                  war-card-game-examination2-sustainableProgramming')
from player import Player


class Test_player(unittest.TestCase):

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
