from aocd import get_data
from functools import reduce

USER_SESSION = 'my_token'


MATCH_WIN_OUTCOME_PART_1 = {
    'A': {'Y': 6, 'X': 3, 'Z': 0},
    'B': {'Z': 6, 'Y': 3, 'X': 0},
    'C': {'X': 6, 'Z': 3, 'Y': 0},
}

YOUR_CHOICE_PART_2 = {
    'X': {'A': 'Z', 'B': 'X', 'C': 'Y'},
    'Y': {'A': 'X', 'B': 'Y', 'C': 'Z'},
    'Z': {'A': 'Y', 'B': 'Z', 'C': 'X'},
}

RESULT_TRANSLATION_PART_2 = {
    'X': 0,  # You need to lose
    'Y': 3,  # You need to tie
    'Z': 6,  # You need to win
}

SHAPE_TRANSLATION = {
    'X': 1,  # Paper gives 1 point
    'Y': 2,  # Scissors gives 2 points
    'Z': 3,  # Rock gives 3 points
}


def __play_rock_paper_scissors_match_1(opponent_shape, my_shape):
    return MATCH_WIN_OUTCOME_PART_1[opponent_shape][my_shape] + SHAPE_TRANSLATION[my_shape]


def __play_rock_paper_scissors_match_2(opponent_shape, my_shape):
    my_choice = YOUR_CHOICE_PART_2[my_shape][opponent_shape]
    return RESULT_TRANSLATION_PART_2[my_shape] + SHAPE_TRANSLATION[my_choice]


def _reduce_match(already_played, current_match, part):
    if part == 1:
        return already_played + __play_rock_paper_scissors_match_1(current_match[0], current_match[1])
    elif part == 2:
        return already_played + __play_rock_paper_scissors_match_2(current_match[0], current_match[1])
    else:
        raise ValueError('Invalid part')


if __name__ == "__main__":
    input_rps_results = get_data(session=USER_SESSION, day=2, year=2022)
    parsed_rps_results = [[y for y in x.split(' ')] for x in input_rps_results.split('\n')]
    total_score_1 = reduce(
        lambda result, match_to_process: _reduce_match(result, match_to_process, 1), parsed_rps_results, 0
    )
    print(f'First question: {total_score_1}')
    total_score_2 = reduce(
        lambda result, match_to_process: _reduce_match(result, match_to_process, 2), parsed_rps_results, 0
    )
    print(f'Second question: {total_score_2}')
