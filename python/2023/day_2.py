import aocd
import re

from functools import reduce

USER_SESSION = 'my_token'

BAG_CONFIGURATION = {
    'red': 12,
    'green': 13,
    'blue': 14,
}


def _fewer_color_cubes(already_counted, game_info):
    # We do not care about the game number
    game_info = game_info[1]
    game_info = game_info.replace(';', ',')
    fewer_cubes_x_color = {'red': 0, 'green': 0, 'blue': 0}
    for cube_info in game_info.split(','):
        cube_color = re.sub('[^a-z]', '', cube_info)
        num_cubes = int(re.sub('[^0-9]', '', cube_info))
        if num_cubes > fewer_cubes_x_color[cube_color]:
            fewer_cubes_x_color[cube_color] = num_cubes
    return already_counted + (fewer_cubes_x_color['red'] * fewer_cubes_x_color['green'] * fewer_cubes_x_color['blue'])


def game_info_1(game_info):
    for game in game_info[1].split(';'):
        for cube_info in game.split(','):
            cube_color = re.sub('[^a-z]', '', cube_info)
            num_cubes = int(re.sub('[^0-9]', '', cube_info))
            if num_cubes > BAG_CONFIGURATION[cube_color]:
                return False
    return True


if __name__ == '__main__':
    input_data = aocd.get_data(session=USER_SESSION, day=2, year=2023)
    parsed_input_data = [parsed_data.split(':') for parsed_data in input_data.split('\n')]
    valid_games = filter(game_info_1, parsed_input_data)
    sum_of_valid_games = sum(int(re.sub('[^0-9]', '', valid_game[0])) for valid_game in valid_games)
    print(f'Part 1: {sum_of_valid_games}')
    sum_of_fewer_cubes = reduce(_fewer_color_cubes, parsed_input_data, 0)
    print(f'Part 2: {sum_of_fewer_cubes}')

