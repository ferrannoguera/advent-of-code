import aocd
import numpy as np


USER_SESSION = '53616c7465645f5f482bd5a563018311b6a153ca12437a8c490e82963acb708f58baf18173026ce6eb22b615d9957eae2f2589c99a75c636910f9637fd85aa53'


MAP_ADJACENT_SYMBOLS = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

SAMPLE_INPUT = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def _has_adjacent_symbol(_first_pos, _data, _found_num):
    _proc_row, _f_y = _first_pos
    range_pos = [(_proc_row, c) for c in [c for c in range(_f_y, _f_y + len(_found_num))]]
    check_pos = list(
        map(lambda x: [
            (x[0]+x_adj, x[1]+y_adj) for x_adj, y_adj in MAP_ADJACENT_SYMBOLS if 0 <= x[0]+x_adj < _data.shape[0] and 0 <= x[1]+y_adj < _data.shape[1] and (x[0]+x_adj, x[1]+y_adj) not in range_pos
        ], range_pos)
    )
    flattened_list = list(set(item for sublist in check_pos for item in sublist))
    for pos in flattened_list:
        if _data[pos[0]][pos[1]] != '.' and not _data[pos[0]][pos[1]].isdigit():
            return int(_found_num)
    return 0


if __name__ == '__main__':
    input_data = aocd.get_data(session=USER_SESSION, day=3, year=2023)
    parsed_input_data = np.array([list(x) for x in input_data.split('\n')])
    sum_valid_numbers = 0
    found_num = None
    first_pos = None
    for row in range(parsed_input_data.shape[0]):
        if found_num:
            sum_valid_numbers += _has_adjacent_symbol(first_pos, parsed_input_data, found_num)
        found_num = None
        first_pos = None
        for col in range(parsed_input_data.shape[1]):
            if not found_num and parsed_input_data[row][col].isdigit():
                first_pos = (row, col)
                found_num = parsed_input_data[row][col]
            elif found_num and parsed_input_data[row][col].isdigit():
                found_num += parsed_input_data[row][col]
            elif found_num and not parsed_input_data[row][col].isdigit():
                sum_valid_numbers += _has_adjacent_symbol(first_pos, parsed_input_data, found_num)
                found_num = None
                first_pos = None
    print(f'Part 1: {sum_valid_numbers}')


