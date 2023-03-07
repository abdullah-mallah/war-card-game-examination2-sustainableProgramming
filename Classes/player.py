

class Player:

    def __init__(self, name, wins, times_played, percentage):
        self._name = name
        self._deck = []
        self._temp_deck = []
        self._wins = wins
        self._times_played = times_played
        self._percentage = percentage
        self._chance_index = 0

    def activate_intelligence_2(self):
        max = 0
        index = -1
        for index_card, card in enumerate(self._deck):
            if card[1] > max:
                max = card[1]
                index = index_card
        self._deck.insert(0, self._deck[index])
        del self._deck[index + 1]

    def activate_intelligence_3(self):
        self.activate_intelligence_2()
        max = 0
        index = -1
        for index_card, card in enumerate(self._deck):
            if index_card == 0:
                continue
            else:
                if card[1] > max:
                    max = card[1]
                    index = index_card
        self._deck.insert(1, self._deck[index])
        del self._deck[index + 1]

    # It will take one card from the hand deck and add it to the floor deck
    def get_next_card(self):
        self._temp_deck.append(self._deck[0])
        del self._deck[0]
        # card is a list of two values, type and number
        for card in self._temp_deck:
            # check if the list is in the last place of the floor list
            if card == self._temp_deck[len(self._temp_deck) - 1]:
                return card[1]  # return only the number of the card
        self._chance_index = 0

    # Add the cards on the floor to the player's hand
    def add_temp_list_to_deck(self, temp_list1, temp_list2):
        for card in temp_list1:
            self._deck.append(card)
        for card1 in temp_list2:
            self._deck.append(card1)

    # Empty the cards on the floor
    def empty_temp(self):
        self._temp_deck = []

    def count_cards(self):
        return len(self._deck)

    def steal_1_card(self, rand_num):
        card = self._deck[rand_num]
        #  length = len(self._deck) - 1
        #  rand_num = random.randint(0, length)
        del self._deck[rand_num]
        return card

    def add_1_card(self, card):
        self._deck.append(card)

    def increase_chance(self):
        max = 0
        indexx = -1
        max_found = False
        if self._chance_index < len(self._deck):
            while not max_found:
                for index, card in enumerate(self._deck):
                    if index >= self._chance_index:
                        if card[1] == 1:
                            max = card[1]
                            indexx = self._deck.index(card)
                            self._deck.insert(self._chance_index,
                                              self._deck[indexx])
                            self._chance_index += 1
                            del self._deck[indexx + 1]
                            max_found = True
                            break
                        else:
                            if card[1] > max:
                                max = card[1]
                                indexx = self._deck.index(card)
                max_found = True
            if max != 1:
                self._deck.insert(self._chance_index, self._deck[indexx])
                self._chance_index += 1
                del self._deck[indexx + 1]
        else:
            self._chance_index = 0
            self.increase_chance()

    # Return the cards of the player
    def get_card_list(self):
        return self._deck

    # Return the cards on the floor
    def get_temp(self):
        return self._temp_deck

    # Get the name of the player
    def get_name(self):
        return self._name

    def get_wins(self):
        return self._wins

    def set_wins(self, wins):
        self._wins = wins

    def get_times_played(self):
        return self._times_played

    def set_times_played(self, times_played):
        self._times_played = times_played

    def get_percentage(self):
        return self._percentage

    def set_deck(self, deck):
        self._deck = deck

    def set_temp_deck(self, temp_deck):
        self._temp_deck = temp_deck
