from player import Player
from inputOutput import Input_output
from fileReaderWriter import FileRW
from game import Game
import random
import sys


# Creating a club deck
def create_deck_clubs():
    type = "clubs"
    deck_clubs = []
    for number in range(1, 14):
        deck_clubs.append([type, number])
    return deck_clubs


# Creating a diamond deck
def create_deck_diamonds():
    type = "diamonds"
    deck_diamond = []
    for number in range(1, 14):
        deck_diamond.append([type, number])
    return deck_diamond


# Creating a heart deck
def create_deck_hearts():
    type = "hearts"
    deck_hearts = []
    for number in range(1, 14):
        deck_hearts.append([type, number])
    return deck_hearts


# Creating a spade deck
def create_deck_spades():
    type = "spades"
    deck_spades = []
    for number in range(1, 14):
        deck_spades.append([type, number])
    return deck_spades


def creat_deck():
    deck = create_deck_clubs() + create_deck_diamonds() + create_deck_hearts()\
        + create_deck_spades()
    random.shuffle(deck)
    middle = 26
    first_half = deck[:middle]
    second_half = deck[middle:]
    return first_half, second_half


def activate_lvl1(inputOutput: Input_output):
    choice = ""
    choice = inputOutput.lvl1_brain()
    return choice


def activate_lvl2(inputOutput: Input_output, fileRW: FileRW):
    first_half, second_half = creat_deck()
    # will take the choice vs_computer or not and the name of player/s
    inputOutput.brain()
    name1_exist = fileRW.check_name(inputOutput.get_name1())
    name2_exist = fileRW.check_name(inputOutput.get_name2())
    if name1_exist:
        player1 = Player(inputOutput.get_name1(),
                         fileRW.get_wins(inputOutput.get_name1()),
                         fileRW.get_times_played(inputOutput.get_name1()),
                         fileRW.get_percentage(inputOutput.get_name1()))
        player1.set_deck(first_half)
    else:
        player1 = Player(inputOutput.get_name1(), "0", "0", "0")
        player1.set_deck(first_half)
        fileRW.store_name(inputOutput.get_name1(), "0", "0", "0")
    if name2_exist:
        player2 = Player(inputOutput.get_name2(),
                         fileRW.get_wins(inputOutput.get_name1()),
                         fileRW.get_times_played(inputOutput.get_name1()),
                         fileRW.get_percentage(inputOutput.get_name1()))
        player2.set_deck(second_half)
    else:
        player2 = Player(inputOutput.get_name2(), "0", "0", "0")
        player2.set_deck(second_half)
        if inputOutput.get_name2() != "computer":
            fileRW.store_name(inputOutput.get_name2(), "0", "0", "0")
    return player1, player2


def main():
    try:
        file_path_1 = sys.argv[1]
        inputOutput = Input_output()
        game = Game()
        fileRW = FileRW(file_path_1)
        choice = ""
        while choice != "1":
            choice = activate_lvl1(inputOutput)
            if choice == "1":  # the player choose to play
                player1, player2 = activate_lvl2(inputOutput, fileRW)
                if inputOutput.get_lvl_intelligence() == "2":
                    player2.activate_intelligence_2()
                elif inputOutput.get_lvl_intelligence() == "3":
                    player2.activate_intelligence_3()
                game.activate_lvl_game(player1, player2, inputOutput,
                                       fileRW)
            elif choice == "2":  # the player choose to see scores
                names = fileRW.get_names()
                inputOutput.print_names(names)
            elif choice == "3":  # the player choose to change his name
                fileRW.uppdate_name(inputOutput.get_old_name(),
                                    inputOutput.get_new_name())
            elif choice == "4":  # the player wanted to exit
                break
    except FileNotFoundError:
        print('Error: The file given as arguments are not valid.')


if __name__ == "__main__":
    main()
