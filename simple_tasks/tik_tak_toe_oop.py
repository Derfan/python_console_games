import random

class TikTakToe:
  empty = '   |   |   '
  valid_marks = ['X', 'O']
  board = [''] * 9
  game_on = True

  def __init__(self, player_1, player_2):
    self.player_1 = player_1
    self.player_2 = player_2

  def display_board(self):
    template = lambda s: f' {s if s else " "} '

    print('\n'*3)
    print(self.empty)
    print('|'.join(map(template, TikTakToe.board[:3])))
    print(self.empty)
    print('-' * len(self.empty))
    print(self.empty)
    print('|'.join(map(template, TikTakToe.board[3:6])))
    print(self.empty)
    print('-' * len(self.empty))
    print(self.empty)
    print('|'.join(map(template, TikTakToe.board[6:])))
    print(self.empty)
    print('\n'*3)

  def player_input(self, current):
    player = '#'

    while player not in TikTakToe.valid_marks:
        player = input(f'{current}: Do you want to be X or O? ').upper()

    second = self.player_2 if current == self.player_1 else self.player_1

    return { current: player, second: TikTakToe.valid_marks[not(TikTakToe.valid_marks.index(player))] }

  def place_marker(self, marker, position):
    TikTakToe.board[position] = marker

  def win_check(self, mark):
    win_combinations = (
        (0, 3, 1), (3, 6, 1), (6, 9, 1),
        (0, 7, 3), (1, 8, 3), (2, 9, 3),
        (0, 9, 4), (2, 7, 2)
    )

    for start, stop, step in win_combinations:
        if TikTakToe.board[start:stop:step] == [mark] * 3:
            return True

    return False

  def choose_first(self):
    rand = random.randint(0, 1)
    return self.player_2 if rand else self.player_1

  def space_check(self, position):
    return TikTakToe.board[position] == ''

  def full_board_check(self):
    return '' not in TikTakToe.board

  def player_choice(self):
    num = "#"

    while num not in range(0,9):
        num = int(input('Pick a number (as a number 0-8): '))

    if self.space_check(num):
        return num
    else:
        print(f'{num} is unavailiable')
        return self.player_choice()

  def reset_params(self):
    TikTakToe.board = [''] * 9
    self.game_on = True

  def replay(self):
    valid = ['no', 'yes']
    answer = '#'

    while answer not in valid:
      answer = input('Do you want to play one more time? (Yes/No) ').lower()

    will_replay = bool(valid.index(answer))

    if will_replay: self.reset_params()

    return will_replay

  def start(self):
    print('Welcome to Tic Tac Toe!')

    while True:
        current = self.choose_first()

        print(f'{current} will go first.')

        marks = self.player_input(current)
        marker = marks[current]

        while self.game_on:
            self.display_board()
            print(f'It is {current} turn with {marker}')
            position = self.player_choice()

            self.place_marker(marker, position)
            self.display_board()

            table_is_full = self.full_board_check()
            have_winner = self.win_check(marker)

            if table_is_full:
                self.game_on = False
                print('It looks like it is a DRAW')

            if have_winner:
                self.game_on = False
                print(f'{current} is win with his {marker.upper()}')

            current = self.player_1 if current == self.player_2 else self.player_2
            marker = marks[current]

        if not self.replay():
            break
