class Input_output:
    def __init__(self) -> None:
        self._choice_lvl1 = ""
        self._name_player1 = ""
        self._name_player2 = "Computer"

    # This will print out level 1 choices
    # Read choice of level 1
    # and decide if its going to read the name of one player or two players
    def brain(self):
        self.lvl1()
        self.lvl1_input()
        if self._choice_lvl1 == "1":
            self.lvl2_choice1_input()
        else:
            self.lvl2_choice2_input()

    # Print out the choice of level 1
    def lvl1(self):
        print("1) VS. Computer")
        print("2) Two players")

    # Read the choice of the user of level 1
    def lvl1_input(self):
        self._choice_lvl1 = input("Choice: ")

    # Read the name of one player
    def lvl2_choice1_input(self):
        self._name_player1 = input("Name of the first player: ")

    # Read the names of two players
    def lvl2_choice2_input(self):
        self._name_player1 = input("Name of the first player: ")
        self._name_player2 = input("Name of the second player: ")
