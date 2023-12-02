import aocd
import re


USER_SESSION = 'my_session'


REPLACEMENT_VALUES = {
    'one': 'o1e',
    'two': 't2o',
    'three': 't3e',
    'four': 'f4r',
    'five': 'f5e',
    'six': 's6x',
    'seven': 's7n',
    'eight': 'e8t',
    'nine': 'n9e',
}


def _get_calibration(x):
    for substring_letters, replacement in REPLACEMENT_VALUES.items():
        if substring_letters in x:
            x= x.replace(substring_letters, replacement)
    return int(f"{re.sub('[^0-9]', '', x)[0]}{re.sub('[^0-9]', '', x)[-1]}")


if __name__ == '__main__':
    input_data = aocd.get_data(session=USER_SESSION, day=1, year=2023)
    parsed_input_data = [x for x in input_data.split('\n')]
    final_calibration_1 = sum(
        map(
            lambda x: int(f"{re.sub('[^0-9]', '', x)[0]}{re.sub('[^0-9]', '', x)[-1]}"),
            parsed_input_data
        )
    )
    print(f'Part 1: {final_calibration_1}')
    final_calibration_2 = sum(map(_get_calibration, parsed_input_data))
    print(f'Part 2: {final_calibration_2}')
