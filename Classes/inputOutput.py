class Input_output:
    def __init__(self) -> None:
        self._choice_lvl1 = ""
        self._choice_lvl2 = ""
        self._choice_lvl_game = ""
        self._name_player1 = ""
        self._name_player2 = "computer"
        self._hack_type = ""
        self._old_name = ""
        self._new_name = ""
        self._lvl_intelligence = ""

    def lvl1_brain(self):
        self.print_lvl1_menu()
        self.lvl1_menu_input()
        if self._choice_lvl1 == "3":
            self.read_old_name()
            self.read_new_name()
        return self._choice_lvl1

    def print_lvl1_menu(self):
        """
        This method prints the available choices for level 1 of the game.
        """
        print("1) Play the game")
        print("2) See player details")
        print("3) Change name of player")
        print("4) Exit the game")

    def lvl1_menu_input(self):
        """
        Prompt the user to choose an option for level 1 of the game.
        """
        valid_choices = ["1", "2", "3", "4"]
        while valid_choices:
            self._choice_lvl1 = input("Choice: ")
            if self._choice_lvl1 in valid_choices:
                break
            else:
                print("Invalid choice. Please choose 1, 2, 3 or 4.")

    def read_old_name(self):
        self._old_name = self.get_input("Old name: ")

    def read_new_name(self):
        self._new_name = self.get_input("New name: ")

    # This will print out level 1 choices
    # Read choice of level 1
    # and decide if its going to read the name of one player or two players
    def lvl2_brain(self):
        self.print_lvl2_menu()
        self.lvl2_menu_input()
        if self._choice_lvl2 == "1":
            self.one_name_input()
            self.print_lvl_intelligence_menu()
            self.lvl_intelligence_menu_input()
        else:
            self.two_names_input()

    def print_lvl2_menu(self):
        """
        This method prints out the available choices for level 2 of the game.
        """
        print("1) VS. Computer")
        print("2) Two players")

    def lvl2_menu_input(self):
        """
        Prompt the user to choose an option for level 2 of the game.
        """
        while True:
            self._choice_lvl2 = input("Choice: ")
            if self._choice_lvl2 == "1" or self._choice_lvl2 == "2":
                break
            else:
                print("Invalid choice. Please choose either 1 or 2.")

    def print_lvl_intelligence_menu(self):
        """
        This method prints the available levels of intelligence
        (difficulty) when playing against the computer.
        """
        print("1) Level 1 (Easy)")
        print("2) Level 2 (Medium)")
        print("3) Level 3 (Hard)")

    def lvl_intelligence_menu_input(self):
        """
        Prompt the user to choose a level of intelligence (difficulty).
        """
        while True:
            self._lvl_intelligence = input("Choice: ")
            if self._lvl_intelligence in ["1", "2", "3"]:
                break
            else:
                print("Invalid choice. Please choose either 1, 2 or 3.")

    def lvl_game_menu(self):
        """
        This method prints the first available choices once
        the game has started.
        """
        print("1) Flip card")
        print("2) Use hack")
        print("3) Continue automatically until a winner is found")
        print("4) Exit")

    def lvl_game_menu_input(self):
        """
        Prompt the user to choose an option what to do
        once the game has started.
        """
        while True:
            self._choice_lvl_game = input("Choice: ")
            if self._choice_lvl_game in ["1", "2", "3", "4"]:
                break
            else:
                print("Invalid choice. Please choose either 1, 2, 3, or 4.")

    # Print list of names
    def scores(self, names):
        for name in names:
            print(f"Name: {name[0]:10} | Wins: {name[1]:10} | Times played: "
                  f"{name[2]} | Winning's percentage: {name[3]} %")

    # Read the name of one player
    def one_name_input(self):
        self._name_player1 = self.get_input("Name of the first player: ")

    # Read the names of two players
    def two_names_input(self):
        self._name_player1 = self.get_input("Name of the first player: ")
        self._name_player2 = self.get_input("Name of the second player: ")

    # This method is responsible printing out choices of lvl game
    # and to read input from user when playing the game
    def lvl_game_brain(self):
        self.lvl_game_menu()
        self.lvl_game_menu_input()
        if self._choice_lvl_game == "2":
            self.print_hacks()
            self.hack_input()

    def print_hacks(self):
        print("1) Steal one card from opponent")
        print("2) Put the highest card in your deck at the beginning")

    # Reads the choice of hack type from user
    # with added error handling
    def hack_input(self):
        while True:
            self._hack_type = input("Choice: ")
            if self._hack_type == "1" or self._hack_type == "2":
                break
            else:
                print("Invalid choice. Please choose either 1 or 2.")

    # Print out flipped card of level Game
    def flipped_card(self, war_card, name, cards_left):
        print(f"\nPlayer: {name.capitalize():9} - flipped war card {war_card} "
              f"and has {cards_left} cards left")

    def congrats(self, name):
        print(f"Congrats to {name.capitalize()}! You have won the game!")

    # Getters
    def get_choice_lvl1(self):
        return self._choice_lvl1

    def get_choice_lvl2(self):
        return self._choice_lvl2

    def get_choice_lvl_game(self):
        return self._choice_lvl_game

    def get_lvl_intelligence(self):
        return self._lvl_intelligence

    def get_name1(self):
        return self._name_player1.lower()

    def get_name2(self):
        return self._name_player2.lower()

    def get_hack_type(self):
        return self._hack_type

    def get_old_name(self):
        return self._old_name.lower()

    def get_new_name(self):
        return self._new_name.lower()

    def get_input(self, text):
        return input(text)
