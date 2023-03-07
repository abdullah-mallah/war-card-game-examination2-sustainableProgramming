"""
This script is used as controll panel of the entire game program.

Authors: Abdullah Mallah, Eszter Kalmar and Hampus Gunnarsson.
"""

from player import Player
from inputOutput import Input_output
from fileReaderWriter import FileRW
from game import Game
import random
import sys


def create_deck_clubs():
    """This method creates clubs deck list."""
    type = "clubs"
    deck_clubs = []
    for number in range(1, 14):
        deck_clubs.append([type, number])
    return deck_clubs


def create_deck_diamonds():
    """This method creates diamonds deck list."""
    type = "diamonds"
    deck_diamond = []
    for number in range(1, 14):
        deck_diamond.append([type, number])
    return deck_diamond


def create_deck_hearts():
    """This method creates hearts deck list."""
    type = "hearts"
    deck_hearts = []
    for number in range(1, 14):
        deck_hearts.append([type, number])
    return deck_hearts


def create_deck_spades():
    """This method creates spades deck list."""
    type = "spades"
    deck_spades = []
    for number in range(1, 14):
        deck_spades.append([type, number])
    return deck_spades


def creat_deck():
    """This method creates a 52 cards deck list."""
    deck = create_deck_clubs() + create_deck_diamonds() + create_deck_hearts()\
        + create_deck_spades()
    random.shuffle(deck)
    middle = 26
    first_half = deck[:middle]
    second_half = deck[middle:]
    return first_half, second_half


def activate_lvl2(inputOutput: Input_output, fileRW: FileRW):
    """
    It takes 1 object of the type Input_output.

    It takes 1 object of the type FileRW.
    It uses Input_output object to print to the user and read choices.
    It uses FileRW object to check if the name exists in the text file.
    If the name exist then it will retrieve the details of that name.
    it creates two objects of the type Player."""
    first_half, second_half = creat_deck()
    inputOutput.lvl2_brain()
    name1_exist = fileRW.check_name(inputOutput.get_name1())
    name2_exist = fileRW.check_name(inputOutput.get_name2())
    if name1_exist:
        player1 = Player(inputOutput.get_name1(),
                         fileRW.get_wins(inputOutput.get_name1()),
                         fileRW.get_times_played(inputOutput.get_name1()),
                         fileRW.get_percentage(inputOutput.get_name1()))
        player1.set_deck(first_half)
    else:
        player1 = Player(inputOutput.get_name1(), "0", "0", "0.0")
        player1.set_deck(first_half)
        fileRW.store_name(inputOutput.get_name1(), "0", "0", "0.0")
    if name2_exist:
        player2 = Player(inputOutput.get_name2(),
                         fileRW.get_wins(inputOutput.get_name1()),
                         fileRW.get_times_played(inputOutput.get_name1()),
                         fileRW.get_percentage(inputOutput.get_name1()))
        player2.set_deck(second_half)
    else:
        player2 = Player(inputOutput.get_name2(), "0", "0", "0.0")
        player2.set_deck(second_half)
        if inputOutput.get_name2() != "computer":
            fileRW.store_name(inputOutput.get_name2(), "0", "0", "0.0")
    return player1, player2


def main():
    """
    It acts as the controller of the entire game program.
    """
    try:
        file_name = sys.argv[1]
        inputOutput = Input_output()
        game = Game()
        fileRW = FileRW(file_name)
        choice = ""
        while choice != "1":
            choice = inputOutput.lvl1_brain()
            if choice == "1":  # The user choose to play
                player1, player2 = activate_lvl2(inputOutput, fileRW)
                if inputOutput.get_difficulty_level() == "2":
                    player2.activate_intelligence_2()
                elif inputOutput.get_difficulty_level() == "3":
                    player2.activate_intelligence_3()
                game.activate_lvl_game(player1, player2, inputOutput,
                                       fileRW)
            elif choice == "2":  # The user choose to print player's details
                names = fileRW.get_names()
                inputOutput.scores(names)
            elif choice == "3":  # The user choose to change a name
                fileRW.uppdate_name(inputOutput.get_old_name(),
                                    inputOutput.get_new_name())
            elif choice == "4":  # the use choose to exit
                break
    except FileNotFoundError:
        print('Error: The file given as arguments are not valid.')


if __name__ == "__main__":
    main()
