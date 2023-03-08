"""
This script is used to print to user and read from the user.

Authors: Abdullah Mallah, Eszter Kalmar and Hampus Gunnarsson.
"""


class InputOutput:
    """A class for handling input and output operations in the game."""

    def __init__(self) -> None:
        """Initialize a new instance of the class."""
        self._choice_main_menu = ""
        self._choice_versus = ""
        self._choice_game_menu = ""
        self._name_player1 = ""
        self._name_player2 = "computer"
        self._hack_type = ""
        self._old_name = ""
        self._new_name = ""
        self._difficulty_level = ""

    def main_menu_controller(self):
        """
        Control the flow of the main menu.

        This method displays the main menu, prompts the user for input,
        and then either proceeds to the appropriate submenu.
        """
        self.main_menu()
        self.main_menu_input()
        if self._choice_main_menu == "3":
            self.read_old_name()
            self.read_new_name()
        return self._choice_main_menu

    def main_menu(self):
        """Print the available choices for the main menu of the game."""
        print("1) Play the game")
        print("2) See player details")
        print("3) Change name of player")
        print("4) Exit the game")

    def main_menu_input(self):
        """Prompt the user to choose an option for the main menu."""
        valid_choices = ["1", "2", "3", "4"]
        while valid_choices:
            self._choice_main_menu = input("Choice: ")
            if self._choice_main_menu in valid_choices:
                break
            print("Invalid choice. Please choose 1, 2, 3 or 4.")

    def read_old_name(self):
        """Read the old name from the user."""
        self._old_name = self.get_input("Old name: ")

    def read_new_name(self):
        """Read the new name from the user."""
        self._new_name = self.get_input("New name: ")

    def scores(self, names):
        """Display the scores for a list of player names."""
        for name in names:
            print(f"Name: {name[0]:10} | Wins: {name[1]:10} | Times played: "
                  f"{name[2]} | Winning's percentage: {name[3]} %")

    def versus_menu_controller(self):
        """
        Control the flow fo the versus menu.

        This method displays the versus menu, prompts the user for input,
        and then either proceeds to the one-player or two-player game modes.
        """
        self.versus_menu()
        self.versus_menu_input()
        if self._choice_versus == "1":
            self.one_name_input()
            self.difficulty_level_menu()
            self.difficulty_level_menu_input()
        else:
            self.two_names_input()

    def versus_menu(self):
        """Print menu to play against either the computer or another player."""
        print("1) VS. Computer")
        print("2) VS. Another player")

    def versus_menu_input(self):
        """Prompt the user to choose an option for versus menu of the game."""
        while True:
            self._choice_versus = input("Choice: ")
            if self._choice_versus == "1" or self._choice_versus == "2":
                break
            else:
                print("Invalid choice. Please choose either 1 or 2.")

    def one_name_input(self):
        """Read and store the name of the first player from the user."""
        self._name_player1 = self.get_input("Name of the first player: ")

    def two_names_input(self):
        """Read and store the name of first and second player from the user."""
        self._name_player1 = self.get_input("Name of the first player: ")
        self._name_player2 = self.get_input("Name of the second player: ")

    def difficulty_level_menu(self):
        """Print the difficulty levels when playing against the computer."""
        print("1) Level 1 (Easy)")
        print("2) Level 2 (Medium)")
        print("3) Level 3 (Hard)")

    def difficulty_level_menu_input(self):
        """Prompt the user to choose a level of difficulty."""
        while True:
            self._difficulty_level = input("Choice: ")
            if self._difficulty_level in ["1", "2", "3"]:
                break
            else:
                print("Invalid choice. Please choose either 1, 2 or 3.")

    def game_menu_controller(self):
        """
        Control the flow of the game menu.

        This method displays the game menu, prompts the user for input,
        and if the user chooses to hack, proceeds to the hacking menu.
        """
        self.game_menu()
        self.game_menu_input()
        if self._choice_game_menu == "2":
            self.hack_menu()
            self.hack_menu_input()

    def game_menu(self):
        """Print the available choices once the game has started."""
        print("1) Flip card")
        print("2) Use hack")
        print("3) Continue automatically until a winner is found")
        print("4) Exit")

    def game_menu_input(self):
        """Prompt the user to choose an option once the game has started."""
        while True:
            self._choice_game_menu = input("Choice: ")
            if self._choice_game_menu in ["1", "2", "3", "4"]:
                break
            else:
                print("Invalid choice. Please choose either 1, 2, 3, or 4.")

    def hack_menu(self):
        """Print out the choices of hack types to the user."""
        print("1) Steal one card from opponent")
        print("2) Put the highest card in your deck at the beginning")

    def hack_menu_input(self):
        """Read the choice of hack type from the user."""
        while True:
            self._hack_type = input("Choice: ")
            if self._hack_type == "1" or self._hack_type == "2":
                break
            else:
                print("Invalid choice. Please choose either 1 or 2.")

    def flipped_card(self, war_card, name, cards_left):
        """Print a message showing that a player has flipped a war card."""
        print(f"\nPlayer: {name.capitalize():9} - flipped war card {war_card} "
              f"and has {cards_left} cards left")

    def congrats(self, name):
        """Print out a congratulation message with the name of the winner."""
        print(f"Congrats to {name.capitalize()}! You have won the game!")

    def get_choice_main_menu(self):
        """Return the user's choice from the main menu."""
        return self._choice_main_menu

    def get_choice_versus_menu(self):
        """Return the user's choice from the versus menu."""
        return self._choice_versus

    def get_choice_game_menu(self):
        """Return the user's choice from the game menu."""
        return self._choice_game_menu

    def get_difficulty_level(self):
        """Return the user's choice of difficulty VS computer."""
        return self._difficulty_level

    def get_name1(self):
        """Return the name of the first player."""
        return self._name_player1.lower()

    def get_name2(self):
        """Return the name of the second player."""
        return self._name_player2.lower()

    def get_hack_type(self):
        """Return the user's choice of which hack type they've chosen."""
        return self._hack_type

    def get_old_name(self):
        """Return the old name of the player."""
        return self._old_name.lower()

    def get_new_name(self):
        """Return the new name of the player."""
        return self._new_name.lower()

    def get_input(self, text):
        """Prompt the user for input and returns the text."""
        return input(text)

    def set_choice_main_menu(self, choice_main_menu):
        """Set the user's choice for the main menu."""
        self._choice_main_menu = choice_main_menu

    def set_choice_versus_menu(self, choice_versus):
        """Set the user's choice for the versus menu."""
        self._choice_versus = choice_versus

    def set_choice_game_menu(self, choice_game_menu):
        """Set the user's choice for the game menu."""
        self._choice_game_menu = choice_game_menu

    def set_difficulty_level(self, difficulty_level):
        """Set the user's choice for the difficulty level vs computer."""
        self._difficulty_level = difficulty_level

    def set_name1(self, name_player1):
        """Set the name of the first player."""
        self._name_player1 = name_player1.lower()

    def set_name2(self, name_player2):
        """Set the name of the second player."""
        self._name_player2 = name_player2.lower()

    def set_hack_type(self, hack_type):
        """Set the user's choice for the hack type."""
        self._hack_type = hack_type

    def set_old_name(self, old_name):
        """Set the old name of the player."""
        self._old_name = old_name.lower()

    def set_new_name(self, new_name):
        """Set the new name of the player."""
        self._new_name = new_name.lower()
