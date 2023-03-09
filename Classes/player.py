"""
This script is used to create players.

Authors: Abdullah Mallah, Eszter Kalmar and Hampus Gunnarsson.
"""


class Player:
    """This class is responsible for player's information and cards."""

    def __init__(self, name, wins, times_played, percentage):
        """Store deck, temp_deck and player's information."""
        self._name = name
        self._deck = []
        self._temp_deck = []
        self._wins = wins
        self._times_played = times_played
        self._percentage = percentage
        self._chance_index = 0

    def activate_intelligence_2(self):
        """Responsible of cards order of computer player."""
        max_num = 0
        index = -1
        for index_card, card in enumerate(self._deck):
            if card[1] > max_num:
                max_num = card[1]
                index = index_card
        self._deck.insert(0, self._deck[index])
        del self._deck[index + 1]

    def activate_intelligence_3(self):
        """Responsible for cards order of computer player."""
        self.activate_intelligence_2()
        max_num = 0
        index = -1
        for index_card, card in enumerate(self._deck):
            if index_card == 0:
                continue
            else:
                if card[1] > max_num:
                    max_num = card[1]
                    index = index_card
        self._deck.insert(1, self._deck[index])
        del self._deck[index + 1]

    def get_next_card(self):
        """
        Take a card of the deck and add it to temp_deck variables.

        Return the number of last card in temp_deck variable.
        """
        self._temp_deck.append(self._deck[0])
        del self._deck[0]
        for card in self._temp_deck:
            if card == self._temp_deck[len(self._temp_deck) - 1]:
                return card[1]
        self._chance_index = 0

    def add_temp_list_to_deck(self, temp_list1, temp_list2):
        """Take two lists and add them to deck list."""
        for card in temp_list1:
            self._deck.append(card)
        for card1 in temp_list2:
            self._deck.append(card1)

    def empty_temp(self):
        """Empty temp_deck variable."""
        self._temp_deck = []

    def count_cards(self):
        """Return the length of deck variable."""
        return len(self._deck)

    def steal_1_card(self, rand_num):
        """
        Take random integer.

        Return a card in deck list at index of that random integer.
        Delete the returned card from deck list.
        """
        card = self._deck[rand_num]
        del self._deck[rand_num]
        return card

    def add_1_card(self, card):
        """
        Take card list.

        Add that card list to deck list.
        """
        self._deck.append(card)

    # def increase_chance(self):
    #     """Responsible of cards order of human player."""
    #     max_num = 0
    #     indexx = -1
    #     max_found = False
    #     if self._chance_index < len(self._deck):
    #         while not max_found:
    #             for index, card in enumerate(self._deck):
    #                 if index >= self._chance_index:
    #                     if card[1] == 1:
    #                         max_num = card[1]
    #                         indexx = self._deck.index(card)
    #                         self._deck.insert(self._chance_index,
    #                                           self._deck[indexx])
    #                         self._chance_index += 1
    #                         del self._deck[indexx + 1]
    #                         max_found = True
    #                         break
    #                     else:
    #                         if card[1] > max_num:
    #                             max_num = card[1]
    #                             indexx = self._deck.index(card)
    #             max_found = True
    #         if max_num != 1:
    #             self._deck.insert(self._chance_index, self._deck[indexx])
    #             self._chance_index += 1
    #             del self._deck[indexx + 1]
    #     else:
    #         self._chance_index = 0
    #         self.increase_chance()

    def get_card_list(self):
        """Return deck list."""
        return self._deck

    def get_temp(self):
        """Return temp_deck list."""
        return self._temp_deck

    def get_name(self):
        """Return the name of the player."""
        return self._name

    def get_wins(self):
        """Return the wins of the player."""
        return self._wins

    def get_percentage(self):
        """Return the percentage of wins of the player."""
        return self._percentage

    def get_times_played(self):
        """Return times of player playing the game."""
        return self._times_played

    def set_times_played(self, times_played):
        """
        Take a string.

        Set variable _times_played to the string parameter.
        """
        self._times_played = times_played

    def set_wins(self, wins):
        """
        Take a string.

        Set variable _wins to the string parameter.
        """
        self._wins = wins

    def set_deck(self, deck):
        """
        Take a list.

        Set variable _deck to the parameter's list.
        """
        self._deck = deck

    def set_temp_deck(self, temp_deck):
        """
        Take a list.

        Set variable _temp_deck to the parameter's list.
        """
        self._temp_deck = temp_deck

    def set_name(self, name):
        """
        Take a string.

        Set variable _name to the string parameter.
        """
        self._name = name

    def set_percentage(self, percentage):
        """
        Take a string.

        Set variable _percentage to the string parameter.
        """
        self._percentage = percentage
