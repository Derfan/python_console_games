from black_jack_game.game import BlackJack
from simple_tasks.tik_tak_toe_oop import TikTakToe

games = {
    'black': 'BlackJack',
    'tiktak': 'TikTakToe'
}
chosen_game = ''
games_instructions = ''

for key in games.keys():
    games_instructions += f'\n[{key}] - {games[key]}'


def start_game(game_key):
    game = ''

    if game_key == 'black':
        game = BlackJack()
    elif game_key == 'tiktak':
        game = TikTakToe('usr1', 'usr2')
    else:
        pass

    game.start()

    return game


while chosen_game not in games.keys():
    chosen_game = input(f'Which game I need to start?{games_instructions}\n:: ')

    if chosen_game in games.keys():
        start_game(chosen_game)
