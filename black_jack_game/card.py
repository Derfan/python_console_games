from black_jack_game.constants import values


class Card:
    def __init__(self, card_name):
        [rank, _, suit] = card_name.split()
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'Suit: {self.suit.capitalize()}\nRank: {self.rank.capitalize()}\nValue: {self.value}'
