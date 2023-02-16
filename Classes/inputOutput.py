class Input_output:
    def __init__(self) -> None:
        self._choice_lvl1 = ""
        self._choice_lvl_game = ""
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
    
    # Print out the choices of level Game
    def lvl_game_choices(self):
        print("1 - Show card")

    # Read the choice of level Game
    def lvl_game_input(self):
        self._input_lvl_game = input("Choice: ")

    # Print out flipped card of level Game
    def lvl_game_flipped_card(self, war_card):
        print(f"card is: {war_card}")

    def congrats(self, turn):
        print(f"Congrats to player {turn}! You have won!")

    # Getters
    def get_choice_lvl1(self):
        return self._choice_lvl1

    def get_name1(self):
        return self._name_player1

    def get_name2(self):
        return self._name_player2

    def get_choice_lvl_game(self):
        return self._choice_lvl_game
