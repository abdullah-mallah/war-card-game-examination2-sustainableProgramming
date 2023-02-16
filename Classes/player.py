class Player:

    def __init__(self, name, player):
        self._name = name
        if player == 1:
            self._deck = self.create_deck1()
            self._deck1_used = True
        else:
            self._deck = self.create_deck2()
        self._temp_deck = []
