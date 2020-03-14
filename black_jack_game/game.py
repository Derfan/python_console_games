from black_jack_game.player import Player
from black_jack_game.croupier import Croupier
from black_jack_game.deck import Deck


class BlackJack:
    def __init__(self):
        self.game_on = False
        self.deck = Deck()
        self.croupier = Croupier()
        self.player = Player('N/A')
        self.bank = 0

    @staticmethod
    def replay_round():
        answer = ''

        while answer not in ['n', 'y']:
            answer = input('Do you want to continue (y/n)? ')

        return answer == 'y'

    def auth(self):
        valid_answers = ['n', 'y']
        name = ''
        answer = ''

        while len(name) < 3:
            name = input('What is your name? ')

        while answer not in valid_answers:
            answer = input(f'Do you want to use default budget ${Player.default_budget} (y/n)? ')

        if bool(valid_answers.index(answer)):
            self.player = Player(name)
        else:
            while True:
                try:
                    budget = int(input('Please indicate the sum: '))
                except ValueError:
                    print('Please indicate number value')
                    continue
                else:
                    self.player = Player(name, budget)
                    break

    def make_bets(self):
        incorrect_bet = True

        while incorrect_bet:
            try:
                bet = int(input('Please provide a bet: '))
                self.player.withdraw(bet)
                self.croupier.withdraw(bet)
            except ValueError as error:
                print(error)
            else:
                incorrect_bet = False
                self.bank += bet * 2

    def give_cards(self, person, num):
        cards = self.deck.deal_cards(num)
        person.add_cards(cards)

    def initial_distribution(self):
        self.give_cards(self.croupier, 2)
        self.give_cards(self.player, 2)

    def player_move(self):
        answer = ''

        while answer != 'n' and self.player.hand.value <= 21:
            answer = input('Would you like to hit (y/n)? ')
            if answer == 'y':
                self.give_cards(self.player, 1)
            else:
                break

    def croupier_move(self):
        self.croupier.open_card()
        self.croupier.print_cards()
        while self.croupier.hand.value < 17:
            self.give_cards(self.croupier, 1)

    def get_round_winner(self):
        player_result = self.player.hand.check_sum()
        croupier_result = self.croupier.hand.check_sum()

        if player_result < croupier_result:
            return self.player
        elif player_result == croupier_result:
            return 'DRAW'
        else:
            return self.croupier

    def send_winnings(self, person):
        person.deposit(self.bank)

        self.bank = 0
        print(f'{person.name} win in this round')
        print('#'*10)
        print(f'Croupier Budget ${self.croupier.budget}')
        print(f'{self.player.name} Budget ${self.player.budget}')

    def start_round(self):
        self.make_bets()
        self.initial_distribution()
        self.player_move()
        self.croupier_move()

        round_winner = self.get_round_winner()

        if round_winner == 'DRAW':
            print(f'It is DRAW, on bank ${self.bank}')
            print('#' * 10)
            print(f'Croupier Budget ${self.croupier.budget}')
            print(f'{self.player.name} Budget ${self.player.budget}')
        else:
            self.send_winnings(round_winner)

        self.player.hand.clear()
        self.croupier.hand.clear()
        self.croupier.close_card()

    def print_game_stat(self):
        print('$' * 50)
        print('\n' * 2)
        print(f'{self.player.name} goes home with ${self.player.budget}')
        print('\n' * 2)
        print('$' * 50)

    def budget_is_empty(self):
        if self.player.budget == 0:
            return self.player
        elif self.croupier.budget == 0:
            return self.croupier
        else:
            return False

    def start(self):
        self.auth()
        self.game_on = input(f'{self.player.name} are you ready to start the game (y/n)? ') == 'y'

        while self.game_on:
            self.deck.shuffle()
            self.start_round()

            looser = self.budget_is_empty()

            if looser:
                print(f'{self.player.name if self.player.budget == 0 else self.croupier.name} out of budget')
                break

            if not self.replay_round():
                self.game_on = False
                break

        self.print_game_stat()
