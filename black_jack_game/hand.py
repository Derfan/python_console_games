class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0

    def __str__(self):
        hand_comp = ''

        for card in self.cards:
            hand_comp += f'\n{card}'

        return hand_comp + f'\nValue: {self.value}'

    def clear(self):
        self.cards = []
        self.value = 0

    def add_card(self, cards):
        for card in cards:
            self.cards.append(card)
            self.value += card.value

    def check_sum(self):
        diff = 21 - self.value

        return diff if diff >= 0 else 10000
