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