import random


class Player:

    def __init__(self, name, player):
        self._name = name
        if player == 1:
            self._deck = self.create_deck1()
        else:
            self._deck = self.create_deck2()
        self._temp_deck = []

    def create_deck1(self):
        deck = []
        deck = self.create_deck_clubs() + self.create_deck_diamonds()
        random.shuffle(deck)
        return deck

    def create_deck2(self):
        deck = []
        deck = self.create_deck_hearts() + self.create_deck_spades()
        random.shuffle(deck)
        return deck

    def create_deck_clubs(self):
        type = "clubs"
        deck_clubs = []
        for number in range(1, 14):
            deck_clubs.append([type, number])
        return deck_clubs

    def create_deck_diamonds(self):
        type = "diamonds"
        deck_diamond = []
        for number in range(1, 14):
            deck_diamond.append([type, number])
        return deck_diamond

    def create_deck_hearts(self):
        type = "hearts"
        deck_hearts = []
        for number in range(1, 14):
            deck_hearts.append([type, number])
        return deck_hearts

    def create_deck_spades(self):
        type = "spades"
        deck_spades = []
        for number in range(1, 14):
            deck_spades.append([type, number])
        return deck_spades

    def check_cards_left(self, cards_list):
        cards_left = False
        if len(cards_list) > 0:
            cards_left = True
        return cards_left

    def get_card_list(self):
        return self._deck
