class Input_output:
    def __init__(self) -> None:
        self._input_choice_lvl1 = ""
        self._name_player1 = ""
        self._name_player2 = "Computer"

    def brain(self):
        self.lvl1()
        self.lvl1_input()
        if self._input_choice_lvl1 == "1":
            self.lvl2_choice1_input()
        else:
            self.lvl2_choice2_input()

    def lvl1(self):
        print("1) VS. Computer")
        print("2) Two players")

    def lvl1_input(self):
        self._input_choice_lvl1 = input("Choice: ")

    def lvl2_choice1_input(self):
        self._name_player1 = input("Name of the first player: ")

    def lvl2_choice2_input(self):
        self._name_player1 = input("Name of the first player: ")
        self._name_player2 = input("Name of the second player: ")
