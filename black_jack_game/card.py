from black_jack_game.constants import values


class Card:
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self) -> str:
        return f'{self.rank} of {self.suit}'
