import random

def display_board(board):
    empty = '   |   |   '
    template = lambda s: f' {s if s else " "} '

    print('\n'*3)
    print(empty)
    print('|'.join(map(template, board[:3])))
    print(empty)
    print('-' * len(empty))
    print(empty)
    print('|'.join(map(template, board[3:6])))
    print(empty)
    print('-' * len(empty))
    print(empty)
    print('|'.join(map(template, board[6:])))
    print(empty)
    print('\n'*3)

def player_input(current):
    valid = ['X', 'O']
    player = '#'

    while player not in valid:
        player = input(f'{current}: Do you want to be X or O? ').upper()

    second = 'player_2' if current == 'player_1' else 'player_1'
    return {
        current: player,
        second: valid[not valid.index(player)]
    }

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    win_combinations = (
        (0, 3, 1), (3, 6, 1), (6, 9, 1),
        (0, 7, 3), (1, 8, 3), (2, 9, 3),
        (0, 9, 4), (2, 7, 2)
    )

    for start, stop, step in win_combinations:
        if board[start:stop:step] == [mark] * 3:
            return True

    return False

def choose_first():
    rand = random.randint(0, 1)
    return 'player_2' if rand else 'player_1'

def space_check(board, position):
    return board[position] == ''

def full_board_check(board):
    return '' not in board

def player_choice(board):
    num = "#"

    while num not in range(0, 9):
        num = int(input('Pick a number (as a number 0-8): '))

    if space_check(board, num):
        return num

    print(f'{num} is unavailiable')
    return player_choice(board)


def replay():
    valid = ['no', 'yes']
    answer = '#'

    while answer not in valid:
        answer = input('Do you want to play one more time? (Yes/No) ').lower()

    return bool(valid.index(answer))

def start_game():
    print('Welcome to Tic Tac Toe!')

    while True:
        board = [''] * 9
        game_on = True
        current = choose_first()

        print(f'{current} will go first.')

        marks = player_input(current)
        marker = marks[current]

        while game_on:
            display_board(board)
            print(f'It is {current} turn with {marker}')
            position = player_choice(board)

            place_marker(board, marker, position)
            display_board(board)

            table_is_full = full_board_check(board)
            have_winner = win_check(board, marker)

            if table_is_full:
                game_on = False
                print('It looks like it is a DRAW')

            if have_winner:
                game_on = False
                print(f'{current} is win with his {marker.upper()}')

            current = 'player_1' if current == 'player_2' else 'player_2'
            marker = marks[current]

        if not replay():
            break
