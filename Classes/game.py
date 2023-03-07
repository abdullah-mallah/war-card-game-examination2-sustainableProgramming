"""
This script is used to display the needed menues and options during the game.

Authors: Abdullah Mallah, Eszter Kalmar and Hampus Gunnarsson.
"""

from player import Player
from inputOutput import Input_output
from fileReaderWriter import FileRW
import random


class Game:
    """Responsible for playing the game."""

    def flip_4_times(self, player1: Player, player2: Player,
                     inputOutput: Input_output):
        """
        Take 2 objects of the type Player and 1 of the type Input_output.

        Return two integers after it flipps four times.
        """
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
                                         player1.count_cards())
                inputOutput.flipped_card(war_card2,
                                         player2.get_name(),
                                         player2.count_cards())
        print("flipped 4 times")
        return war_card1, war_card2

    def flip_once(self, player1: Player, player2: Player,
                  inputOutput: Input_output):
        """
        Take 2 objects of the type Player and 1 of the type Input_output.

        Return two integers after it flipps one time.
        """
        war_card1 = 0
        war_card2 = 0
        for turn in range(1, 3):
            if turn == 1:
                print(f"\n{player1.get_name().capitalize()}'s turn")
                inputOutput.set_choice_game_menu("")
                while inputOutput.get_choice_game_menu() != "1":
                    inputOutput.game_menu_controller()
                    if inputOutput.get_choice_game_menu() == "1":
                        war_card1 = self.flipp_once(player1)
                        inputOutput.flipped_card(war_card1,
                                                 player1.get_name(),
                                                 player1.count_cards())
                        break
                    elif inputOutput.get_choice_game_menu() == "2":
                        if inputOutput.get_hack_type() == "1":
                            self.steal_1_card(player1, player2, turn)
                            if player2.count_cards() == 0:
                                war_card1 = 14
                                war_card2 = 0
                                break
                        else:
                            self.increase_chance(player1, player2, turn)
                    elif inputOutput.get_choice_game_menu() == "3":
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
                print(f"\n{player2.get_name().capitalize()}'s turn")
                if player2.get_name() == "computer":
                    war_card2 = self.flipp_once(player2)
                    inputOutput.flipped_card(war_card2,
                                             player2.get_name(),
                                             player2.count_cards())
                else:
                    inputOutput.set_choice_game_menu("")
                    while inputOutput.get_choice_game_menu != "1":
                        inputOutput.game_menu_controller()
                        if inputOutput.get_choice_game_menu() == "1":
                            war_card2 = self.flipp_once(player2)
                            inputOutput.flipped_card(war_card2,
                                                     player2.get_name(),
                                                     player2.count_cards())
                            break
                        elif inputOutput.get_choice_game_menu() == "2":
                            if inputOutput.get_hack_type() == "1":
                                self.steal_1_card(player1, player2, turn)
                                if player1.count_cards() == 0:
                                    war_card1 = 0
                                    war_card2 = 14
                                    break
                            else:
                                self.increase_chance(player1, player2, turn)
                        elif inputOutput.get_choice_game_menu() == "3":
                            war_card1 = 0
                            war_card2 = 0
                            break
                        else:
                            exit()
                    if war_card1 == 0 and war_card2 == 14:
                        break
                    elif war_card1 == 0 and war_card2 == 0:
                        break
        print("flipped once")
        return war_card1, war_card2

    def steal_1_card(self, player1: Player, player2: Player, turn):
        """
        Take two objects of the type Player and one integer.

        Move a card from one object to the other.
        """
        card = []
        length = 0
        rand_num = 0
        if turn == 1:
            length = player2.count_cards() - 1
            rand_num = random.randint(0, length)
            card = player2.steal_1_card(rand_num)
            player1.add_1_card(card)
        else:
            length = player1.count_cards() - 1
            rand_num = random.randint(0, length)
            card = player1.steal_1_card(rand_num)
            player2.add_1_card(card)

    def increase_chance(self, player1: Player, player2: Player, turn):
        """
        Take two objects of the type Player and one integer.

        Put the highest card in the Player object at the begining.
        """
        if turn == 1:
            player1.increase_chance()
        else:
            player2.increase_chance()

    def chk_player_won_round(self, war_card1, war_card2):
        """
        Take two integers.

        Check integer is bigger and returns 0, 1 or 2.
        """
        if war_card1 == 1 and war_card2 != 1:
            return 1
        elif war_card1 != 1 and war_card2 == 1:
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
        """
        Take two objects of the type Player and one integer.

        Add the cards on the floor to the hand of the winner.
        """
        if player_won_round == 1:
            print(f"\n{player1.get_name().capitalize()} won this round")
            player1.add_temp_list_to_deck(player1.get_temp(),
                                          player2.get_temp())
            player1.empty_temp()
            player2.empty_temp()
        else:
            print(f"\n{player2.get_name().capitalize()} won this round")
            player2.add_temp_list_to_deck(player1.get_temp(),
                                          player2.get_temp())
            player1.empty_temp()
            player2.empty_temp()

    def flipp_once(self, player: Player):
        """
        Take one object of the type Player.

        Take one card of that object and returns an integer.
        """
        war_card = player.get_next_card()
        return war_card

    def activate_lvl_game(self, player1: Player, player2: Player,
                          inputOutput: Input_output, fileRW: FileRW):
        """
        Take two objects of the type Player.

        Take one object of the type Input_output.
        Take one object of the typer FileRW.
        Call other methods in order to play the game.
        """
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
                    cards_in1 = player1.count_cards()
                    cards_in2 = player2.count_cards()
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
                        inputOutput.congrats(player2.get_name())
                        self.uppdate_wins(2, player1, player2, fileRW)
                        exit()
                    if cards_in2 < 4:
                        inputOutput.congrats(player1.get_name())
                        self.uppdate_wins(1, player1, player2, fileRW)
                        exit()
                else:
                    # loop on turns of players to show thier hands
                    cards_in1 = player1.count_cards()
                    cards_in2 = player2.count_cards()
                    if cards_in1 >= 1 and cards_in2 >= 1:
                        war_card1, war_card2 = self.flip_once(player1, player2,
                                                              inputOutput)
                        if war_card1 == 0 and war_card2 == 0:
                            self.continue_untill_the_end(player1, player2,
                                                         inputOutput, fileRW)
                        # after using hack
                        if war_card1 == 0 and war_card2 == 14:
                            inputOutput.congrats(player2.get_name())
                            self.uppdate_wins(2, player1, player2, fileRW)
                            exit()
                        if war_card1 == 14 and war_card2 == 0:
                            inputOutput.congrats(player1.get_name())
                            self.uppdate_wins(1, player1, player2, fileRW)
                            exit()
                        # if the card on floor big
                        player_won_round = self.chk_player_won_round(war_card1,
                                                                     war_card2)
                        if player_won_round != 0:
                            self.add_cards_to_round_winner(player1, player2,
                                                           player_won_round)
                            round_finished = True
                        else:
                            flipp_4_times = True
                    if cards_in1 < 1:
                        inputOutput.congrats(player2.get_name())
                        self.uppdate_wins(2, player1, player2, fileRW)
                        exit()
                    if cards_in2 < 1:
                        inputOutput.congrats(player1.get_name())
                        self.uppdate_wins(1, player1, player2, fileRW)
                        exit()

    def continue_untill_the_end(self, player1: Player, player2: Player,
                                inputOutput: Input_output, fileRW: FileRW):
        """
        Take two objects of the type Player.

        Take one object of the type Input_output.
        Take one object of the typer FileRW.
        Call other methods in order to continue automatically.
        """
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
                    cards_in1 = player1.count_cards()
                    cards_in2 = player2.count_cards()
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
                        inputOutput.congrats(player2.get_name())
                        self.uppdate_wins(2, player1, player2, fileRW)
                        exit()
                    if cards_in2 < 4:
                        inputOutput.congrats(player1.get_name())
                        self.uppdate_wins(1, player1, player2, fileRW)
                        exit()
                else:
                    # loop on turns of players to show thier hands
                    cards_in1 = player1.count_cards()
                    cards_in2 = player2.count_cards()
                    if cards_in1 >= 1 and cards_in2 >= 1:
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
                    if cards_in1 < 1:
                        inputOutput.congrats(player2.get_name())
                        self.uppdate_wins(2, player1, player2, fileRW)
                        exit()
                    if cards_in2 < 1:
                        inputOutput.congrats(player1.get_name())
                        self.uppdate_wins(1, player1, player2, fileRW)
                        exit()

    def uppdate_wins(self, turn, player1: Player, player2: Player,
                     fileRW: FileRW):
        """
        Take one integer.

        Take 2 objects of the type Player.
        Take 1 object of the type FileRW.
        Store the score of the players.
        """
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
        """
        Take two objects of the type Player.

        Take one object of the type Input_output.
        Return two integers after it flipps one time.
        """
        war_card1 = 0
        war_card2 = 0
        for turn in range(1, 3):
            if turn == 1:
                print(f"\n{player1.get_name().capitalize()}'s turn")
                war_card1 = self.flipp_once(player1)
                inputOutput.flipped_card(war_card1,
                                         player1.get_name(),
                                         player1.count_cards())
            else:
                print(f"\n{player2.get_name().capitalize()}'s turn")
                war_card2 = self.flipp_once(player2)
                inputOutput.flipped_card(war_card2,
                                         player2.get_name(),
                                         player2.count_cards())
        print("Flipped once")
        return war_card1, war_card2
