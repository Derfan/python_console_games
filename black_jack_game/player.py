from black_jack_game.hand import Hand


class Player:
    default_budget = 100

    def __init__(self, name, budget=default_budget):
        self.name = name
        self.budget = budget
        self.hand = Hand()

    def __str__(self):
        return f'Player name: {self.name}\nCurrent budget: ${self.budget}'

    def deposit(self, amount):
        self.budget += amount

    def withdraw(self, amount):
        if amount > self.budget:
            raise ValueError('Sorry, you out of budget.')
        else:
            self.budget -= amount

    def add_cards(self, cards):
        self.hand.add_card(cards)
