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

    # This will print out level 1 choices
    # Read choice of level 1
    # and decide if its going to read the name of one player or two players
    def brain(self):
        self.lvl2()
        self.lvl2_input()
        if self._choice_lvl2 == "1":
            self.one_name_input()
            self.print_lvl_intelligence()
            self.read_lvl_intelligence()
        else:
            self.two_names_input()

    def lvl1_brain(self):
        self.lvl1()
        self.lvl1_input()
        if self._choice_lvl1 == "3":
            self.read_old_name()
            self.read_new_name()
        return self._choice_lvl1

    def print_lvl_intelligence(self):
        print("1) Level 1 (Easy)")
        print("2) Level 2 (Medium)")
        print("3) Level 3 (Hard)")

    def read_lvl_intelligence(self):
        while True:
            self._lvl_intelligence = input("Choice: ")
            if self._lvl_intelligence in ["1", "2", "3"]:
                break
            else:
                print("Invalid choice. Please choose either 1, 2 or 3.")

    # Print out the choice of level 1
    def lvl1(self):
        print("1) Play the game")
        print("2) See player details")
        print("3) Change name of player")
        print("4) Exit the game")

    # Reads the choice of the user of level 1
    # with added error handling
    def lvl1_input(self):
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

    # Print list of names
    def print_names(self, names):
        for name in names:
            times = " | Times played: " + name[2]
            percentage = " | Winning's percentage: " + name[3]
            print(f"Name: {name[0]:10}| Wins: {name[1]:10}{times}{percentage}")

    # Print out the choice of level 2
    def lvl2(self):
        print("1) VS. Computer")
        print("2) Two players")

    # Read the choice of the user of level 2
    # with added error handling
    def lvl2_input(self):
        while True:
            self._choice_lvl2 = input("Choice: ")
            if self._choice_lvl2 == "1" or self._choice_lvl2 == "2":
                break
            else:
                print("Invalid choice. Please choose either 1 or 2.")

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
        self.lvl_game_choices()
        self.lvl_game_input()
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

    # Print out the choices of level Game
    def lvl_game_choices(self):
        print("1) Flip card")
        print("2) Use hack")
        print("3) Continue automatically until a winner is found")
        print("4) Exit")

    # Read the choice of level Game from user
    # with added error handling
    def lvl_game_input(self):
        while True:
            self._choice_lvl_game = input("Choice: ")
            if self._choice_lvl_game in ["1", "2", "3", "4"]:
                break
            else:
                print("Invalid choice. Please choose either 1, 2, 3, or 4.")

    # Print out flipped card of level Game
    def flipped_card(self, war_card, name, cards_left):
        war_cards = "flipped war card " + (str)(war_card)
        card_left = (str)(cards_left) + " cards left"
        print(f"\nPlayer: {name:10} - {war_cards} and has {card_left}")

    def congrats(self, turn):
        print(f"Congrats to player {turn}! You have won the game!")

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

    def get_input(text):
        return input(text)
