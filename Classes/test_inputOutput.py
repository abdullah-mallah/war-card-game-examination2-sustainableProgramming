import unittest
from unittest.mock import patch
from inputOutput import Input_output


class Test_inputoutput(unittest.TestCase):

    def setUp(self):
        self.inOut = Input_output()

    def test_lvl1(self):
        with unittest.mock.patch('builtins.print') as mock_print:
            self.inOut.lvl1()
            mock_print.assert_has_calls([
                unittest.mock.call("1) Play the game"),
                unittest.mock.call("2) See player details"),
                unittest.mock.call("3) Change name of player"),
                unittest.mock.call("4) Exit the game"),
            ])

    def test_lvl2(self):
        with unittest.mock.patch('builtins.print') as mock_print:
            self.inOut.lvl2()
            mock_print.assert_has_calls([
                unittest.mock.call("1) VS. Computer"),
                unittest.mock.call("2) Two players"),
            ])

    @patch("inputOutput.Input_output.get_input", return_value="name1")
    def test_one_name_input(self, input):
        self.inOut.one_name_input()
        self.assertEqual(self.inOut._name_player1, "name1")

    @patch("inputOutput.Input_output.get_input", return_value="name1")
    def test_two_names_input(self, input):
        self.inOut.two_names_input()
        self.assertEqual(self.inOut._name_player1, "name1")
        self.assertEqual(self.inOut._name_player2, "name1")

    @patch("inputOutput.Input_output.get_input", return_value="old name")
    def test_read_old_name(self, input):
        self.inOut.read_old_name()
        self.assertEqual(self.inOut._old_name, "old name")

    @patch("inputOutput.Input_output.get_input", return_value="new name")
    def test_read_new_name(self, input):
        self.inOut.read_new_name()
        self.assertEqual(self.inOut._new_name, "new name")

    def test_print_hacks(self):
        with unittest.mock.patch('builtins.print') as mock_print:
            self.inOut.print_hacks()
            mock_print.assert_has_calls([
                unittest.mock.call("1) Steal one card from opponent"),
                unittest.mock.call("2) Put the highest card in your "
                                   "deck at the beginning"),
            ])

    def test_lvl_game_choices(self):
        with unittest.mock.patch('builtins.print') as mock_print:
            self.inOut.lvl_game_choices()
            mock_print.assert_has_calls([
                unittest.mock.call("1) Flip card"),
                unittest.mock.call("2) Use hack"),
                unittest.mock.call("3) Continue automatically until "
                                   "a winner is found"),
                unittest.mock.call("4) Exit"),
            ])

    def test_flipped_card(self):
        war_card = "10"
        name = "Test name"
        cards_left = 10

        with unittest.mock.patch('builtins.print') as mock_print:
            self.inOut.flipped_card(war_card, name, cards_left)
            mock_print.assert_has_calls([
                unittest.mock.call(f"\nPlayer: {name:10} - flipped war card "
                                   f"{war_card} and has {cards_left} cards "
                                   f"left"),
            ])

    def test_congrats(self):
        turn = 1

        with unittest.mock.patch('builtins.print') as mock_print:
            self.inOut.congrats(turn)
            mock_print.assert_has_calls([
                unittest.mock.call(f"Congrats to player {turn}! "
                                   f"You have won the game!")
            ])

    def test_get_choice_lvl1(self):
        self.inOut._choice_lvl1 = "1"
        self.assertEqual(self.inOut.get_choice_lvl1(), "1")

    def test_get_choice_lvl2(self):
        self.inOut._choice_lvl2 = "1"
        self.assertEqual(self.inOut.get_choice_lvl2(), "1")

    def test_get_choice_lvl_game(self):
        self.inOut._choice_lvl_game = "1"
        self.assertEqual(self.inOut.get_choice_lvl_game(), "1")

    def test_get_lvl_intelligence(self):
        self.inOut._lvl_intelligence = "1"
        self.assertEqual(self.inOut.get_lvl_intelligence(), "1")

    def test_get_hack_type(self):
        self.inOut._hack_type = "1"
        self.assertEqual(self.inOut.get_hack_type(), "1")

    def test_get_name1(self):
        self.inOut._name_player1 = "TEST_NAME1"
        self.assertEqual(self.inOut.get_name1(), "test_name1")
        self.inOut._name_player1 = "test_NAME1"
        self.assertEqual(self.inOut.get_name1(), "test_name1")
        self.inOut._name_player1 = "TEST_name1"
        self.assertEqual(self.inOut.get_name1(), "test_name1")

    def test_get_name2(self):
        self.inOut._name_player2 = "TEST_NAME2"
        self.assertEqual(self.inOut.get_name2(), "test_name2")
        self.inOut._name_player2 = "test_NAME2"
        self.assertEqual(self.inOut.get_name2(), "test_name2")
        self.inOut._name_player2 = "TEST_name2"
        self.assertEqual(self.inOut.get_name2(), "test_name2")

    def test_get_old_name(self):
        self.inOut._old_name = "OLD_NAME"
        self.assertEqual(self.inOut.get_old_name(), "old_name")
        self.inOut._old_name = "old_NAME"
        self.assertEqual(self.inOut.get_old_name(), "old_name")
        self.inOut._old_name = "OLD_name"
        self.assertEqual(self.inOut.get_old_name(), "old_name")

    def test_get_new_name(self):
        self.inOut._new_name = "NEW_NAME"
        self.assertEqual(self.inOut.get_new_name(), "new_name")
        self.inOut._new_name = "new_NAME"
        self.assertEqual(self.inOut.get_new_name(), "new_name")
        self.inOut._new_name = "NEW_name"
        self.assertEqual(self.inOut.get_new_name(), "new_name")


if __name__ == "__main__":
    unittest.main()
