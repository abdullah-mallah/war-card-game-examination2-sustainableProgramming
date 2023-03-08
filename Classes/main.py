"""
This script is used as controll panel of the entire game program.

Authors: Abdullah Mallah, Eszter Kalmar and Hampus Gunnarsson.
"""

import random
import sys
from player import Player
from input_output import InputOutput
from fileReaderWriter import FileRW
from game import Game


def create_deck_clubs():
    """Create clubs deck list."""
    card_type = "clubs"
    deck_clubs = []
    for number in range(1, 14):
        deck_clubs.append([card_type, number])
    return deck_clubs


def create_deck_diamonds():
    """Create diamonds deck list."""
    card_type = "diamonds"
    deck_diamond = []
    for number in range(1, 14):
        deck_diamond.append([card_type, number])
    return deck_diamond


def create_deck_hearts():
    """Create hearts deck list."""
    card_type = "hearts"
    deck_hearts = []
    for number in range(1, 14):
        deck_hearts.append([card_type, number])
    return deck_hearts


def create_deck_spades():
    """Create spades deck list."""
    card_type = "spades"
    deck_spades = []
    for number in range(1, 14):
        deck_spades.append([card_type, number])
    return deck_spades


def creat_deck():
    """Create a 52 cards deck list."""
    deck = create_deck_clubs() + create_deck_diamonds() + create_deck_hearts()\
        + create_deck_spades()
    random.shuffle(deck)
    middle = 26
    first_half = deck[:middle]
    second_half = deck[middle:]
    return first_half, second_half


def activate_lvl2(input_output: InputOutput, file_r_w: FileRW):
    """
    Take 1 object of the type Input_output.

    Take 1 object of the type FileRW.
    Use Input_output object to print to the user and read choices.
    Use FileRW object to check if the name exists in the text file.
    If the name exist then it will retrieve the details of that name.
    Create two objects of the type Player.
    """
    first_half, second_half = creat_deck()
    input_output.versus_menu_controller()
    name1_exist = file_r_w.check_name(input_output.get_name1())
    name2_exist = file_r_w.check_name(input_output.get_name2())
    if name1_exist:
        player1 = Player(input_output.get_name1(),
                         file_r_w.get_wins(input_output.get_name1()),
                         file_r_w.get_times_played(input_output.get_name1()),
                         file_r_w.get_percentage(input_output.get_name1()))
        player1.set_deck(first_half)
    else:
        player1 = Player(input_output.get_name1(), "0", "0", "0.0")
        player1.set_deck(first_half)
        file_r_w.store_name(input_output.get_name1(), "0", "0", "0.0")
    if name2_exist:
        player2 = Player(input_output.get_name2(),
                         file_r_w.get_wins(input_output.get_name1()),
                         file_r_w.get_times_played(input_output.get_name1()),
                         file_r_w.get_percentage(input_output.get_name1()))
        player2.set_deck(second_half)
    else:
        player2 = Player(input_output.get_name2(), "0", "0", "0.0")
        player2.set_deck(second_half)
        if input_output.get_name2() != "computer":
            file_r_w.store_name(input_output.get_name2(), "0", "0", "0.0")
    return player1, player2


def main():
    """Act like a controller of the entire game program."""
    try:
        file_name = sys.argv[1]
        input_output = InputOutput()
        game = Game()
        file_r_w = FileRW(file_name)
        choice = ""
        while choice != "1":
            choice = input_output.main_menu_controller()
            if choice == "1":  # The user choose to play
                player1, player2 = activate_lvl2(input_output, file_r_w)
                if input_output.get_difficulty_level() == "2":
                    player2.activate_intelligence_2()
                elif input_output.get_difficulty_level() == "3":
                    player2.activate_intelligence_3()
                game.activate_lvl_game(player1, player2, input_output,
                                       file_r_w)
            elif choice == "2":  # The user choose to print player's details
                names = file_r_w.get_names()
                input_output.scores(names)
            elif choice == "3":  # The user choose to change a name
                file_r_w.uppdate_name(input_output.get_old_name(),
                                      input_output.get_new_name())
            elif choice == "4":  # the use choose to exit
                break
    except FileNotFoundError:
        print('Error: The file given as arguments are not valid.')


if __name__ == "__main__":
    main()
