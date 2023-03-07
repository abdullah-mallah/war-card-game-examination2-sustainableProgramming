"""
This script is used to test class Input_output.

Authors: Abdullah Mallah, Eszter Kalmar and Hampus Gunnarsson.
"""
import unittest
from unittest.mock import patch
from inputOutput import Input_output


class Test_inputoutput(unittest.TestCase):
    """A test class for the Input_output class in the card game."""

    def setUp(self):
        """Set up an instance of the Input_output class."""
        self.inOut = Input_output()

    def test_main_menu(self):
        """Test the main menu method using unittest.mock patch."""
        with unittest.mock.patch('builtins.print') as mock_print:
            self.inOut.main_menu()
            mock_print.assert_has_calls([
                unittest.mock.call("1) Play the game"),
                unittest.mock.call("2) See player details"),
                unittest.mock.call("3) Change name of player"),
                unittest.mock.call("4) Exit the game"),
            ])

    def test_versus_menu(self):
        """Test the versus menu method using unittest.mock patch."""
        with unittest.mock.patch('builtins.print') as mock_print:
            self.inOut.versus_menu()
            mock_print.assert_has_calls([
                unittest.mock.call("1) VS. Computer"),
                unittest.mock.call("2) VS. Another player"),
            ])

    @patch("inputOutput.Input_output.get_input", return_value="name1")
    def test_one_name_input(self, input):
        """Test the one_name_input method using unittest.mock patch."""
        self.inOut.one_name_input()
        self.assertEqual(self.inOut._name_player1, "name1")

    @patch("inputOutput.Input_output.get_input", return_value="name1")
    def test_two_names_input(self, input):
        """Test the two_names_input method using unittest.mock patch."""
        self.inOut.two_names_input()
        self.assertEqual(self.inOut._name_player1, "name1")
        self.assertEqual(self.inOut._name_player2, "name1")

    @patch("inputOutput.Input_output.get_input", return_value="old name")
    def test_read_old_name(self, input):
        """Test the read_old_name method using unittest.mock patch."""
        self.inOut.read_old_name()
        self.assertEqual(self.inOut._old_name, "old name")

    @patch("inputOutput.Input_output.get_input", return_value="new name")
    def test_read_new_name(self, input):
        """Test the read_new_name method using unittest.mock patch."""
        self.inOut.read_new_name()
        self.assertEqual(self.inOut._new_name, "new name")

    def test_hack_menu(self):
        """Verify that the hack menu method displays the correct options."""
        with unittest.mock.patch('builtins.print') as mock_print:
            self.inOut.hack_menu()
            mock_print.assert_has_calls([
                unittest.mock.call("1) Steal one card from opponent"),
                unittest.mock.call("2) Put the highest card in your "
                                   "deck at the beginning"),
            ])

    def test_game_menu(self):
        """Verify that the game menu method displays the correct options."""
        with unittest.mock.patch('builtins.print') as mock_print:
            self.inOut.game_menu()
            mock_print.assert_has_calls([
                unittest.mock.call("1) Flip card"),
                unittest.mock.call("2) Use hack"),
                unittest.mock.call("3) Continue automatically until "
                                   "a winner is found"),
                unittest.mock.call("4) Exit"),
            ])

    def test_flipped_card(self):
        """Verify that the flipped_card method displays the expected output."""
        war_card = "10"
        name = "Test name"
        cards_left = 10

        with unittest.mock.patch('builtins.print') as mock_print:
            self.inOut.flipped_card(war_card, name, cards_left)
            mock_print.assert_has_calls([
                unittest.mock.call(f"\nPlayer: {name:9} - flipped war card "
                                   f"{war_card} and has {cards_left} cards "
                                   f"left"),
            ])

    def test_congrats(self):
        """Verify that the congrats method prints out the expected winner."""
        name = "Test name"

        with unittest.mock.patch('builtins.print') as mock_print:
            self.inOut.congrats(name)
            mock_print.assert_has_calls([
                unittest.mock.call(f"Congrats to {name}! "
                                   f"You have won the game!")
            ])

    def test_get_choice_main_menu(self):
        """Test the method to get the user's choice from the main menu."""
        self.inOut._choice_main_menu = "1"
        self.assertEqual(self.inOut.get_choice_main_menu(), "1")

    def test_get_choice_versus_menu(self):
        """Test the method to get the user's choice from the versus menu."""
        self.inOut._choice_versus = "1"
        self.assertEqual(self.inOut.get_choice_versus_menu(), "1")

    def test_get_choice_game_menu(self):
        """Test the method to get the user's choice from the game menu."""
        self.inOut._choice_game_menu = "1"
        self.assertEqual(self.inOut.get_choice_game_menu(), "1")

    def test_get_difficulty_level(self):
        """Test the method to get the user's choice of difficulty level."""
        self.inOut._difficulty_level = "1"
        self.assertEqual(self.inOut.get_difficulty_level(), "1")

    def test_get_hack_type(self):
        """Test the method to get the user's choice on the hack type."""
        self.inOut._hack_type = "1"
        self.assertEqual(self.inOut.get_hack_type(), "1")

    def test_get_name1(self):
        """Test the get_name1 method of the Input_output class."""
        self.inOut._name_player1 = "TEST_NAME1"
        self.assertEqual(self.inOut.get_name1(), "test_name1")
        self.inOut._name_player1 = "test_NAME1"
        self.assertEqual(self.inOut.get_name1(), "test_name1")
        self.inOut._name_player1 = "TEST_name1"
        self.assertEqual(self.inOut.get_name1(), "test_name1")

    def test_get_name2(self):
        """Test the get_name2 method of the Input_output class."""
        self.inOut._name_player2 = "TEST_NAME2"
        self.assertEqual(self.inOut.get_name2(), "test_name2")
        self.inOut._name_player2 = "test_NAME2"
        self.assertEqual(self.inOut.get_name2(), "test_name2")
        self.inOut._name_player2 = "TEST_name2"
        self.assertEqual(self.inOut.get_name2(), "test_name2")

    def test_get_old_name(self):
        """Test the get_old_name method of the Input_output class."""
        self.inOut._old_name = "OLD_NAME"
        self.assertEqual(self.inOut.get_old_name(), "old_name")
        self.inOut._old_name = "old_NAME"
        self.assertEqual(self.inOut.get_old_name(), "old_name")
        self.inOut._old_name = "OLD_name"
        self.assertEqual(self.inOut.get_old_name(), "old_name")

    def test_get_new_name(self):
        """Test the get_new_name method of the Input_output class."""
        self.inOut._new_name = "NEW_NAME"
        self.assertEqual(self.inOut.get_new_name(), "new_name")
        self.inOut._new_name = "new_NAME"
        self.assertEqual(self.inOut.get_new_name(), "new_name")
        self.inOut._new_name = "NEW_name"
        self.assertEqual(self.inOut.get_new_name(), "new_name")


if __name__ == "__main__":
    unittest.main()
