from player import Player
from inputOutput import Input_output
from fileReaderWriter import FileRW
from game import Game


def activate_lvl1(inputOutput: Input_output):
    choice = ""
    choice = inputOutput.lvl1_brain()
    return choice


def activate_lvl2(inputOutput: Input_output, fileRW: FileRW):
    # will take the choice vs_computer or not and the name of player/s
    inputOutput.brain()

    # will creat players according to the choice of the user at main menue
    for player in range(1, 3):
        if player == 1:
            player1 = Player(inputOutput.get_name1(), player)
            fileRW.store_name(player1.get_name(), "0", "0")
        else:
            if inputOutput.get_choice_lvl2() == "1":
                player2 = Player(inputOutput.get_name2(), player)
            else:
                player2 = Player(inputOutput.get_name2(), player)
                fileRW.store_name(player2.get_name(), "0", "0")
    return player1, player2


def main():
    inputOutput = Input_output()
    game = Game()
    fileRW = FileRW("C:\\Users\\a\\Desktop\\war-card-game-examination2-sustainableProgramming\\Classes\\score.txt")
    choice = ""
    while choice != "1":
        choice = activate_lvl1(inputOutput)
        if choice == "1":  # the player choose to play
            player1, player2 = activate_lvl2(inputOutput, fileRW)
            game.activate_lvl_game(player1, player2, inputOutput, fileRW)
        elif choice == "2":  # the player choose to see scores
            names = fileRW.get_names()
            inputOutput.print_names(names)
        elif choice == "3":  # the player choose to change his name
            fileRW.uppdate_name(inputOutput.get_old_name(),
                                inputOutput.get_new_name())
        elif choice == "4":  # the player wanted to exit
            break


if __name__ == "__main__":
    main()
