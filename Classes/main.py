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

    winner_found = False
    cards_found = True
    war_card1 = 0
    war_card2 = 0

    # will keep looping untill one player has no more cards
    while not winner_found:
        # loop on turns of players to show thier hands
        for turn in range(1, 3):
            inputOutput.lvl_game_choices()
            inputOutput.lvl_game_input()
            if inputOutput.get_input_lvl_game() == "1" and turn == 1:
                # check if the player has cards in his deck
                cards_found = player1.check_cards_left(player1.get_card_list())
                if cards_found:
                    war_card1 = player1.get_next_card()
                    inputOutput.lvl_game_score(war_card1)
                # if no cards with first player
                else:
                    winner_found = True
                    inputOutput.congrats(turn + 1)
                    break


if __name__ == "__main__":
    main()
