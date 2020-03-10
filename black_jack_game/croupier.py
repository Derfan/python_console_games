from black_jack_game.player import Player


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
            print('-' * 50)
            print('Croupier:')
            print(self.hand)
            print('-' * 50)
        else:
            print('-' * 10)
            print('Croupier:')
            print('\n*** HIDDEN ***')
            print(self.hand.cards[1])
            print(f'Value: {self.hand.value - self.hand.cards[0].value}')
            print('-' * 10)
