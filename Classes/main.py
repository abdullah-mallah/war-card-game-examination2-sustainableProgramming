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
    name1_exist = fileRW.check_name(inputOutput.get_name1())
    name2_exist = fileRW.check_name(inputOutput.get_name2())
    if name1_exist:
        player1 = Player(inputOutput.get_name1(), 1,
                         fileRW.get_wins(inputOutput.get_name1()),
                         fileRW.get_times_played(inputOutput.get_name1()),
                         fileRW.get_percentage(inputOutput.get_name1()))
    else:
        player1 = Player(inputOutput.get_name1(), 1, "0", "0", "0")
        fileRW.store_name(inputOutput.get_name1(), "0", "0", "0")
    if name2_exist:
        player2 = Player(inputOutput.get_name2(), 2,
                         fileRW.get_wins(inputOutput.get_name1()),
                         fileRW.get_times_played(inputOutput.get_name1()),
                         fileRW.get_percentage(inputOutput.get_name1()))
    else:
        player2 = Player(inputOutput.get_name2(), 2, "0", "0", "0")
        if inputOutput.get_name2() != "computer":
            fileRW.store_name(inputOutput.get_name2(), "0", "0", "0")
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
            if inputOutput.get_lvl_intelligence() == "2":
                player2.activate_intelligence_2()
            elif inputOutput.get_lvl_intelligence() == "3":
                player2.activate_intelligence_3()
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
