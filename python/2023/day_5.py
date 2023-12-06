import aocd


USER_SESSION = 'my_token'

SAMPLE_DATA = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


def __do_stuff(_source, interval, result, final_map):
    # Both in the same range
    if interval[0] <= _source[0] <= interval[1] and interval[0] <= _source[1] <= interval[1]:
        start_range = result[0] + _source[0] - interval[0]
        end_range = start_range + _source[1] - _source[0]
        final_map.append((start_range, end_range))
        return final_map, None, False
    # In the range from the bottom
    elif interval[0] <= _source[0] <= interval[1] and not interval[0] <= _source[1] <= interval[1]:
        start_range = result[0] + _source[0] - interval[0]
        end_range = result[1]
        final_map.append((start_range, end_range))
        return final_map, (interval[1]+1, _source[1]), False
    # In the range from the top
    elif not interval[0] <= _source[0] <= interval[1] and interval[0] <= _source[1] <= interval[1]:
        start_range = result[0]
        end_range = result[0] + _source[1] - interval[0]
        final_map.append((start_range, end_range))
        return final_map, (_source[0], interval[0]-1), False
    # Not in the range
    else:
        return final_map, _source, True


def _map_source_to_destination_2(_source_list, _source_to_destination_map):
    final_map = []
    missing_thresholds = []
    for _source in _source_list:
        continue_check = True
        for interval, result in _source_to_destination_map.items():
            final_map, missing_threshold, continue_check = __do_stuff(_source, interval, result, final_map)
            if not continue_check:
                if missing_threshold:
                    missing_thresholds.append(missing_threshold)
                break
        if continue_check:
            final_map.append(_source)

    if missing_thresholds:
        return final_map + _map_source_to_destination_2(missing_thresholds, _source_to_destination_map)
    else:
        return final_map


def _map_source_to_destination(_source_list, _source_to_destination_map):
    final_map = []
    found = False
    for _source in _source_list:
        for s_t_d_map in _source_to_destination_map:
            if s_t_d_map[1] <= _source < s_t_d_map[1] + s_t_d_map[2]:
                final_map.append(s_t_d_map[0] + _source - s_t_d_map[1])
                found = True
                break
        if not found:
            final_map.append(_source)
        found = False
    return final_map


if __name__ == '__main__':
    input_data = aocd.get_data(session=USER_SESSION, day=5, year=2023)
    parsed_input_data = input_data.split('\n\n')
    source = [int(seed) for seed in parsed_input_data[0].split(':')[1].strip().split(' ')]
    for source_to_destination_maps in parsed_input_data[1:]:
        source_to_destination_map = [
            [int(destination) for destination in row.split(' ')] for row in source_to_destination_maps.split('\n')[1:]
        ]
        source = _map_source_to_destination(source, source_to_destination_map)
    print(f'Part 1: {min(source)}')
    source_list = [int(seed) for seed in parsed_input_data[0].split(':')[1].strip().split(' ')]
    source_list = [
        (source_list[source_idx], source_list[source_idx]+source_list[source_idx+1]-1)
        for source_idx in range(0, len(source_list), 2)
    ]
    for source_to_destination_maps in parsed_input_data[1:]:
        source_to_destination_map = [
            [int(destination) for destination in row.split(' ')] for row in source_to_destination_maps.split('\n')[1:]
        ]
        source_to_destination_map = {(x[1], x[1]+x[2]-1): (x[0],x[0]+x[2]-1) for x in source_to_destination_map}
        source_list = _map_source_to_destination_2(source_list, source_to_destination_map)
    print(f'Part 2: {min(source_list, key=lambda x: x[0])[0]}')
