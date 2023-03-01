from player import Player
from inputOutput import Input_output
from fileReaderWriter import FileRW
import random


class Game:
    def count_cards(self, player: Player):
        cards_in_hand = player.count_cards()
        return cards_in_hand

    def flip_4_times(self, player1: Player, player2: Player,
                     inputOutput: Input_output):
        war_card1 = 0
        war_card2 = 0
        for loop in range(4):
            for turn in range(1, 3):
                if turn == 1:
                    war_card1 = self.flipp_once(player1)
                else:
                    war_card2 = self.flipp_once(player2)
            if loop == 3:
                inputOutput.flipped_card(war_card1,
                                         player1.get_name(),
                                         self.count_cards(player1))
                inputOutput.flipped_card(war_card2,
                                         player2.get_name(),
                                         self.count_cards(player2))
        return war_card1, war_card2

    def flip_once(self, player1: Player, player2: Player,
                  inputOutput: Input_output):
        war_card1 = 0
        war_card2 = 0
        for turn in range(1, 3):
            if turn == 1:
                print("Player 1 turn")
                while inputOutput.get_choice_lvl_game != "1":
                    inputOutput.lvl_game_brain()
                    if inputOutput.get_choice_lvl_game() == "1":
                        war_card1 = self.flipp_once(player1)
                        inputOutput.flipped_card(war_card1,
                                                 player1.get_name(),
                                                 self.count_cards(player1))
                        break
                    elif inputOutput.get_choice_lvl_game() == "2":
                        if inputOutput.get_hack_type() == "1":
                            self.steal_1_card(player1, player2, turn)
                            if self.count_cards(player2) == 0:
                                war_card1 = 14
                                war_card2 = 0
                                break
                        else:
                            self.increase_chance(player1, player2, turn)
                    elif inputOutput.get_choice_lvl_game() == "3":
                        war_card1 = 0
                        war_card2 = 0
                        break
                    else:
                        exit()
                if war_card1 == 14 and war_card2 == 0:
                    break
                elif war_card1 == 0 and war_card2 == 0:
                    break
            else:
                print("Player 2 turn")
                if player2.get_name() == "computer":
                    war_card2 = self.flipp_once(player2)
                    inputOutput.flipped_card(war_card2,
                                             player2.get_name(),
                                             self.count_cards(player2))
                else:
                    while inputOutput.get_choice_lvl_game != "1":
                        inputOutput.lvl_game_brain()
                        if inputOutput.get_choice_lvl_game() == "1":
                            war_card2 = self.flipp_once(player2)
                            inputOutput.flipped_card(war_card2,
                                                     player1.get_name(),
                                                     self.count_cards(player2))
                            break
                        elif inputOutput.get_choice_lvl_game() == "2":
                            if inputOutput.get_hack_type() == "1":
                                self.steal_1_card(player1, player2, turn)
                                if self.count_cards(player1) == 0:
                                    war_card1 = 0
                                    war_card2 = 14
                                    break
                            else:
                                self.increase_chance(player1, player2, turn)
                        elif inputOutput.get_choice_lvl_game() == "3":
                            war_card1 = 0
                            war_card2 = 0
                            break
                        else:
                            exit()
                    if war_card1 == 0 and war_card2 == 14:
                        break
                    elif war_card1 == 0 and war_card2 == 0:
                        break
        return war_card1, war_card2

    def steal_1_card(self, player1: Player, player2: Player, turn):
        card = []
        length = 0
        rand_num = 0
        if turn == 1:
            length = player2.count_cards() - 1
            rand_num = random.randint(0, length)
            card = player2.steal_1_card(rand_num)
            player1.add_1_card(card)
        else:
            length = player2.count_cards() - 1
            rand_num = random.randint(0, length)
            card = player1.steal_1_card()
            player2.add_1_card(card)

    def increase_chance(self, player1: Player, player2: Player, turn):
        if turn == 1:
            player1.increase_chance()
        else:
            player2.increase_chance()

    def chk_player_won_round(self, war_card1, war_card2):
        if war_card1 == 1 and war_card2 != 1:
            return 1
        elif war_card2 == 1 and war_card1 != 1:
            return 2
        elif war_card1 == 1 and war_card2 == 1:
            return 0
        else:
            if war_card1 > war_card2:
                return 1
            elif war_card1 < war_card2:
                return 2
            else:
                return 0

    def add_cards_to_round_winner(self, player1: Player, player2: Player,
                                  player_won_round):
        if player_won_round == 1:
            print("Player 1 won this round")
            player1.add_temp_list_to_deck(player1.get_temp(),
                                          player2.get_temp())
            player1.empty_temp()
            player2.empty_temp()
        else:
            print("Player 2 won this round")
            player2.add_temp_list_to_deck(player1.get_temp(),
                                          player2.get_temp())
            player1.empty_temp()
            player2.empty_temp()

    def check_card(self, player: Player):
        card_found = player.check_cards_left(player.get_card_list())
        return card_found

    def flipp_once(self, player: Player):
        war_card = player.get_next_card()
        return war_card

    def activate_lvl_game(self, player1: Player, player2: Player,
                          inputOutput: Input_output, fileRW: FileRW):
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
                    cards_in1 = self.count_cards(player1)
                    cards_in2 = self.count_cards(player2)
                    if cards_in1 >= 4 and cards_in2 >= 4:
                        war_card1, war_card2 = self.flip_4_times(player1,
                                                                 player2,
                                                                 inputOutput)
                        player_won_round = self.chk_player_won_round(war_card1,
                                                                     war_card2)
                        if player_won_round != 0:
                            self.add_cards_to_round_winner(player1, player2,
                                                           player_won_round)
                            round_finished = True
                            flipp_4_times = False
                        else:
                            continue
                    if cards_in1 < 4:
                        inputOutput.congrats(2)
                        self.uppdate_wins(2, player1, player2, fileRW)
                        exit()
                    if cards_in2 < 4:
                        inputOutput.congrats(1)
                        self.uppdate_wins(1, player1, player2, fileRW)
                        exit()

                else:
                    # loop on turns of players to show thier hands
                    card_in1_found = self.check_card(player1)
                    card_in2_found = self.check_card(player2)
                    if card_in1_found and card_in2_found:
                        war_card1, war_card2 = self.flip_once(player1, player2,
                                                              inputOutput)
                        if war_card1 == 0 and war_card2 == 0:
                            self.continue_untill_the_end(player1, player2,
                                                         inputOutput, fileRW)
                        # after using hack
                        if war_card1 == 0 and war_card2 == 14:
                            winner2_found = True
                            inputOutput.congrats(2)
                            self.uppdate_wins(2, player1, player2, fileRW)
                        if war_card1 == 14 and war_card2 == 0:
                            winner1_found = True
                            inputOutput.congrats(1)
                            self.uppdate_wins(1, player1, player2, fileRW)
                        # if the card on floor big
                        player_won_round = self.chk_player_won_round(war_card1,
                                                                     war_card2)
                        if player_won_round != 0:
                            self.add_cards_to_round_winner(player1, player2,
                                                           player_won_round)
                            round_finished = True
                        else:
                            flipp_4_times = True
                    cards_in1 = self.count_cards(player1)
                    cards_in2 = self.count_cards(player2)
                    if cards_in1 < 1:
                        inputOutput.congrats(2)
                        self.uppdate_wins(2, player1, player2, fileRW)
                        exit()
                    if cards_in2 < 1:
                        inputOutput.congrats(1)
                        self.uppdate_wins(1, player1, player2, fileRW)
                        exit()

    def continue_untill_the_end(self, player1: Player, player2: Player,
                                inputOutput: Input_output, fileRW: FileRW):
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
                    cards_in1 = self.count_cards(player1)
                    cards_in2 = self.count_cards(player2)
                    if cards_in1 >= 4 and cards_in2 >= 4:
                        war_card1, war_card2 = self.flip_4_auto(player1,
                                                                player2)
                        player_won_round = self.chk_player_won_round(war_card1,
                                                                     war_card2)
                        if player_won_round != 0:
                            self.add_cards_to_round_winner(player1, player2,
                                                           player_won_round)
                            round_finished = True
                            flipp_4_times = False
                        else:
                            continue
                    cards_in1 = self.count_cards(player1)
                    cards_in2 = self.count_cards(player2)
                    if cards_in1 < 4:
                        inputOutput.congrats(2)
                        self.uppdate_wins(2, player1, player2, fileRW)
                        exit()
                    if cards_in2 < 4:
                        inputOutput.congrats(1)
                        self.uppdate_wins(1, player1, player2, fileRW)
                        exit()

                else:
                    # loop on turns of players to show thier hands
                    card_in1_found = self.check_card(player1)
                    card_in2_found = self.check_card(player2)
                    if card_in1_found and card_in2_found:
                        war_card1, war_card2 = self.flip_once_auto(player1,
                                                                   player2,
                                                                   inputOutput)
                        # if the card on floor big
                        player_won_round = self.chk_player_won_round(war_card1,
                                                                     war_card2)
                        if player_won_round != 0:
                            self.add_cards_to_round_winner(player1, player2,
                                                           player_won_round)
                            round_finished = True
                        else:
                            flipp_4_times = True
                    cards_in1 = self.count_cards(player1)
                    cards_in2 = self.count_cards(player2)
                    if cards_in1 < 1:
                        inputOutput.congrats(2)
                        self.uppdate_wins(2, player1, player2, fileRW)
                        exit()
                    if cards_in2 < 1:
                        inputOutput.congrats(1)
                        self.uppdate_wins(1, player1, player2, fileRW)
                        exit()

    def uppdate_wins(self, turn, player1: Player, player2: Player,
                     fileRW: FileRW):
        wins1 = (int)(player1.get_wins())
        times_played1 = (int)(player1.get_times_played())
        percentage1 = (float)(player1.get_percentage())
        wins2 = (int)(player2.get_wins())
        times_played2 = (int)(player2.get_times_played())
        percentage2 = (float)(player2.get_percentage())
        if turn == 1:
            fileRW.update_wins(player1.get_name(),
                               wins1 + 1,
                               times_played1 + 1,
                               percentage1)
            if player2.get_name() != "computer":
                fileRW.update_wins(player2.get_name(),
                                   wins2,
                                   times_played2 + 1,
                                   percentage2)
        else:
            if player2.get_name() != "computer":
                fileRW.update_wins(player2.get_name(),
                                   wins2 + 1,
                                   times_played2 + 1,
                                   percentage2)
            fileRW.update_wins(player1.get_name(),
                               wins1,
                               times_played1 + 1,
                               percentage1)

    def flip_once_auto(self, player1: Player, player2: Player,
                       inputOutput: Input_output):
        war_card1 = 0
        war_card2 = 0
        for turn in range(1, 3):
            if turn == 1:
                war_card1 = self.flipp_once(player1)
                inputOutput.flipped_card(war_card1,
                                         player1.get_name(),
                                         self.count_cards(player1))
            else:
                war_card2 = self.flipp_once(player2)
                inputOutput.flipped_card(war_card2,
                                         player2.get_name(),
                                         self.count_cards(player2))
        print("Flipped once")
        return war_card1, war_card2

    def flip_4_auto(self, player1: Player, player2: Player):
        war_card1 = 0
        war_card2 = 0
        for loop in range(4):
            for turn in range(1, 3):
                if turn == 1:
                    war_card1 = self.flipp_once(player1)
                else:
                    war_card2 = self.flipp_once(player2)
        print("Flipped 4 times")
        return war_card1, war_card2
