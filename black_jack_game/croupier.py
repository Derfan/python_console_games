from black_jack_game.player import Player
from black_jack_game.card import Card


class Croupier(Player):
    def __init__(self):
        super().__init__('Croupier', 5000)
        self.card_is_open = False

    def open_card(self):
        self.card_is_open = True

    def close_card(self):
        self.card_is_open = False

    def print_cards(self):
        if self.card_is_open:
            print('-' * 10)
            print(f'Croupier cards: {self.hand.cards}\nValue: {self.hand.sum_of_values}')
            print('-' * 10)
        else:
            cards = ['HIDDEN', self.hand.cards[1]]
            value = self.hand.sum_of_values - Card(self.hand.cards[0]).value

            print('-' * 10)
            print(f'Croupier cards: {cards}\nValue: {value}')
            print('-' * 10)
