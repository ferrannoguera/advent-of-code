from aocd import get_data
from functools import reduce

USER_SESSION = 'my_user_session'


OPPONENT_WIN_OUTCOME = {
    'A': {'Y': 6, 'X': 3, 'Z': 0},
    'B': {'Z': 6, 'Y': 3, 'X': 0},
    'C': {'X': 6, 'Z': 3, 'Y': 0},
}

SHAPE_TRANSLATION = {
    'X': 1,  # Paper gives 1 point
    'Y': 2,  # Scissors gives 2 points
    'Z': 3,  # Rock gives 3 points
}


def __play_rock_paper_scissors_match(opponent_shape, my_shape):
    return OPPONENT_WIN_OUTCOME[opponent_shape][my_shape] + SHAPE_TRANSLATION[my_shape]


def _reduce_match(already_played, current_match):
    return already_played + __play_rock_paper_scissors_match(current_match[0], current_match[1])


if __name__ == "__main__":
    input_rps_results = get_data(session=USER_SESSION, day=2, year=2022)
    parsed_rps_results = [[y for y in x.split(' ')] for x in input_rps_results.split('\n')]
    total_score = reduce(_reduce_match, parsed_rps_results, 0)
    print(total_score)
