import random
from black_jack_game.constants import suits, ranks
from black_jack_game.card import Card


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_cards(self, num):
        cards = self.deck[0:num]
        self.deck = self.deck[num:]

        return cards
