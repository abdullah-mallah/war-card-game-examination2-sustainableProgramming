from player import Player
from inputOutput import Input_output
from fileReaderWriter import FileRW


def turn_loop(player1: Player, player2: Player, inputOutput: Input_output):
    for turn in range(1, 3):
        inputOutput.lvl_game_choices()
        inputOutput.lvl_game_input()
        if inputOutput.get_choice_lvl_game() == "1":
            if turn == 1:
                war_card1 = flipp_once(player1)
                inputOutput.lvl_game_flipped_card(war_card1)
            else:
                war_card2 = flipp_once(player2)
                inputOutput.lvl_game_flipped_card(war_card2)
    return war_card1, war_card2


def check_card(player: Player):
    card_found = player.check_cards_left(player.get_card_list())
    return card_found


def flipp_once(player: Player):
    war_card = player.get_next_card()
    return war_card


def check_player_won_round(war_card1, war_card2):
    if war_card1 > war_card2:
        return 1
    elif war_card1 < war_card2:
        return 2
    else:
        return 0


def add_cards_to_round_winner(player1: Player, player2: Player,
                              player_won_round):
    if player_won_round == 1:
        player1.add_temp_list_to_deck(player1.get_temp(), player2.get_temp())
        player1.empty_temp()
        player2.empty_temp()
    else:
        player2.add_temp_list_to_deck(player1.get_temp(), player2.get_temp())
        player1.empty_temp()
        player2.empty_temp()


def count_cards(player: Player):
    cards_in_hand = player.count_cards()
    return cards_in_hand


def turn_loop_4_times(player1: Player, player2: Player,
                      inputOutput: Input_output):
    for loop in range(4):
        for turn in range(1, 3):
            if turn == 1:
                war_card1 = flipp_once(player1)
            else:
                war_card2 = flipp_once(player2)
        if loop == 3:
            inputOutput.lvl_game_flipped_card(war_card1)
            inputOutput.lvl_game_flipped_card(war_card2)
    return war_card1, war_card2


def activate_lvl1(inputOutput: Input_output):
    choice = ""
    inputOutput.lvl1()
    inputOutput.lvl1_input()
    choice = inputOutput.get_choice_lvl1()
    return choice


def activate_lvl2(inputOutput: Input_output, fileRW: FileRW):
    # will take the choice vs_computer or not and the name of player/s
    inputOutput.brain()

    # will creat players according to the choice of the user at main menue
    for player in range(1, 3):
        if player == 1:
            player1 = Player(inputOutput.get_name1(), player)
            fileRW.store_name(player1.get_name(), (str)(player1.get_wins()))
        else:
            if inputOutput.get_choice_lvl2() == "1":
                player2 = Player("computer", player)
            else:
                player2 = Player(inputOutput.get_name2(), player)
                fileRW.store_name(player2.get_name(),
                                  (str)(player2.get_wins()))
    return player1, player2


def activate_lvl_game(player1: Player, player2: Player,
                      inputOutput: Input_output):
    card_in1_found = True
    card_in2_found = True
    cards_in1 = 0
    cards_in2 = 0
    round_finished = False
    winner1_found = False
    winner2_found = False
    war_card1 = 0
    war_card2 = 0
    player_won_round = 0
    flipp_4_times = False

    # will keep looping untill one player has no more cards
    while not winner1_found and not winner2_found:
        round_finished = False
        while not round_finished:
            if flipp_4_times:
                cards_in1 = count_cards(player1)
                cards_in2 = count_cards(player2)
                if cards_in1 >= 4 and cards_in2 >= 4:
                    war_card1, war_card2 = turn_loop_4_times(player1,
                                                             player2,
                                                             inputOutput)
                    player_won_round = check_player_won_round(war_card1,
                                                              war_card2)
                    if player_won_round != 0:
                        add_cards_to_round_winner(player1, player2,
                                                  player_won_round)
                        round_finished = True
                        flipp_4_times = False
                    else:
                        continue
                elif cards_in1 < 4:
                    round_finished = True
                    flipp_4_times = False
                    winner2_found = True
                    inputOutput.congrats(2)
                elif cards_in2 < 4:
                    round_finished = True
                    flipp_4_times = False
                    winner1_found = True
                    inputOutput.congrats(1)

            else:
                # loop on turns of players to show thier hands
                card_in1_found = check_card(player1)
                card_in2_found = check_card(player2)
                if card_in1_found and card_in2_found:
                    war_card1, war_card2 = turn_loop(player1, player2,
                                                     inputOutput)
                    # if the card on floor big
                    player_won_round = check_player_won_round(war_card1,
                                                              war_card2)
                    if player_won_round != 0:
                        add_cards_to_round_winner(player1, player2,
                                                  player_won_round)
                        round_finished = True
                    else:
                        flipp_4_times = True
                elif not card_in1_found:
                    winner2_found = True
                    inputOutput.congrats(2)
                elif not card_in2_found:
                    winner1_found = True
                    inputOutput.congrats(1)


def main():
    inputOutput = Input_output()
    fileRW = FileRW("C:\\Users\\a\\Desktop\\war-card-game-examination2-sustainableProgramming\\Classes\\score.txt")
    choice = ""
    while choice != "1":
        choice = activate_lvl1(inputOutput)
        if choice == "1":  # the player choose to play
            player1, player2 = activate_lvl2(inputOutput, fileRW)
            activate_lvl_game(player1, player2, inputOutput)
        elif choice == "2":  # the player choose to see scores
            names = fileRW.get_names()
            inputOutput.print_names(names)
        elif choice == "3":  # the player choose to change his name
            pass
        elif choice == "4":  # the player wanted to exit
            break


if __name__ == "__main__":
    main()
