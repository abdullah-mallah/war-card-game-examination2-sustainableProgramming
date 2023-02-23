import random


class Player:

    def __init__(self, name, player):
        self._name = name
        if player == 1:
            self._deck = self.create_deck1()
        else:
            self._deck = self.create_deck2()
        self._temp_deck = []
        self._wins = 0
        self._times_played = 0

    # Creating a deck for player 1
    def create_deck1(self):
        deck = []
        deck = self.create_deck_clubs() + self.create_deck_diamonds()
        random.shuffle(deck)
        return deck

    # Creating a deck for player 2
    def create_deck2(self):
        deck = []
        deck = self.create_deck_hearts() + self.create_deck_spades()
        random.shuffle(deck)
        return deck

    # Creating a club deck
    def create_deck_clubs(self):
        type = "clubs"
        deck_clubs = []
        for number in range(1, 14):
            deck_clubs.append([type, number])
        return deck_clubs

    # Creating a diamond deck
    def create_deck_diamonds(self):
        type = "diamonds"
        deck_diamond = []
        for number in range(1, 14):
            deck_diamond.append([type, number])
        return deck_diamond

    # Creating a heart deck
    def create_deck_hearts(self):
        type = "hearts"
        deck_hearts = []
        for number in range(1, 14):
            deck_hearts.append([type, number])
        return deck_hearts

    # Creating a spade deck
    def create_deck_spades(self):
        type = "spades"
        deck_spades = []
        for number in range(1, 14):
            deck_spades.append([type, number])
        return deck_spades

    # Check if the player has cards in his hand
    def check_cards_left(self, cards_list):
        cards_left = False
        if len(cards_list) > 0:
            cards_left = True
        return cards_left

    # It will take one card from the hand deck and add it to the floor deck
    def get_next_card(self):
        self._temp_deck.append(self._deck[0])
        del self._deck[0]
        # card is a list of two values, type and number
        for card in self._temp_deck:
            # check if the list is in the last place of the floor list
            if card == self._temp_deck[len(self._temp_deck) - 1]:
                return card[1]  # return only the number of the card

    # Add the cards on the floor to the player's hand
    def add_temp_list_to_deck(self, temp_list1, temp_list2):
        self._deck += temp_list1 + temp_list2

    # Empty the cards on the floor
    def empty_temp(self):
        self._temp_deck = []

    def count_cards(self):
        return len(self._deck)

    def steal_1_card(self):
        card = []
        length = len(self._deck) - 1
        rand_num = random.randint(0, length)
        card += self._deck[rand_num]
        del self._deck[rand_num]
        return card

    def add_1_card(self, card):
        self._deck += card

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
