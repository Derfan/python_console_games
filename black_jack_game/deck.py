import random
from black_jack_game.constants import suits, ranks


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(f'{rank} of {suit}')

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_cards(self, num):
        cards = self.deck[0:num]
        self.deck = self.deck[num:]

        return cards
