from player import Player
from inputOutput import Input_output
from fileReaderWriter import FileRW


def main():
    inputOutput = Input_output()
    # will take the choice vs_computer or not and the name of player/s
    inputOutput.brain()

    # will creat players according to the choice of the user at main menue
    for player in range(1, 3):
        if player == 1:
            player1 = Player(inputOutput.get_name1(), player)
        else:
            if inputOutput.get_choice_lvl1() == "1":
                player2 = Player("computer", player)
            else:
                player2 = Player(inputOutput.get_name2(), player)

if __name__ == "__main__":
    main()
