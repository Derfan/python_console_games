from black_jack_game.card import Card


class Hand:
    def __init__(self):
        self.cards = []
        self.sum_of_values = 0

    def clear(self):
        self.cards = []
        self.sum_of_values = 0

    def add_card(self, cards):
        for card in cards:
            self.cards.append(card)
        self.calculate_sum()

    def check_sum(self):
        diff = 21 - self.sum_of_values

        return diff if diff >= 0 else 10000

    def calculate_sum(self):
        s = 0

        for card_name in self.cards:
            card = Card(card_name)
            s += card.value

        self.sum_of_values = s
