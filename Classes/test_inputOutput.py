import unittest
from inputOutput import Input_output


class Test_inputoutput(unittest.TestCase):

    def setUp(self):
        self.inOut = Input_output()

    # def test_brain(self):
    #     self.inOut.brain()
    #     if self.inOut.get_choice_lvl2() == "1":
    #         self.assertEqual(self.inOut.get_choice_lvl2(), "1")
    #     else:
    #         self.assertEqual(self.inOut.get_choice_lvl2(), "2")

    def test_lvl1(self):
        pass

    def test_lvl2(self):
        pass

    def test_one_name_input(self):
        pass

    def test_two_names_input(self):
        pass

    def test_print_hacks(self):
        pass

    def lvl_game_choices(self):
        pass

    def test_flipped_card(self):
        pass

    def test_congrats(self):
        pass

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
        self.inOut._name_player2 = "test_NAME1"
        self.inOut._name_player2 = "TEST_name1"
        self.assertEqual(self.inOut.get_name1(), "test_name1")

    def test_get_name2(self):
        self.inOut._name_player2 = "TEST_NAME2"
        self.inOut._name_player2 = "test_NAME2"
        self.inOut._name_player2 = "TEST_name2"
        self.assertEqual(self.inOut.get_name2(), "test_name2")

    def test_get_old_name(self):
        self.inOut._old_name = "OLD_NAME"
        self.inOut._old_name = "old_NAME"
        self.inOut._old_name = "OLD_name"
        self.assertEqual(self.inOut.get_old_name(), "old_name")

    def test_get_new_name(self):
        self.inOut._new_name = "NEW_NAME"
        self.inOut._new_name = "new_NAME"
        self.inOut._new_name = "NEW_name"
        self.assertEqual(self.inOut.get_new_name(), "new_name")


if __name__ == "__main__":
    unittest.main()
