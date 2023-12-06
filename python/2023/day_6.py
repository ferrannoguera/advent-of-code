import aocd


USER_SESSION = 'my_session'

SAMPLE_DATA = """Time:      7  15   30
Distance:  9  40  200"""


if __name__ == '__main__':
    input_data = aocd.get_data(session=USER_SESSION, day=6, year=2023)
    parsed_input_data = [parsed_data.split(':')[1].split() for parsed_data in input_data.split('\n')]
    time = [int(t) for t in parsed_input_data[0]]
    distance = [int(d) for d in parsed_input_data[1]]
    total_winning_possible_races = 0
    for race_time, race_distance in zip(time, distance):
        winning_races = list(
            filter(lambda y: y > race_distance, map(lambda x: x * (race_time - x), range(1, race_time)))
        )
        if total_winning_possible_races:
            total_winning_possible_races *= len(winning_races)
        else:
            total_winning_possible_races = len(winning_races)
    print(f'Part 1: {total_winning_possible_races}')
    time = int(''.join(parsed_input_data[0]))
    distance = int(''.join(parsed_input_data[1]))
    winning_races = list(filter(lambda y: y > distance, map(lambda x: x * (time - x), range(1, time))))
    print(f'Part 2: {len(winning_races)}')


