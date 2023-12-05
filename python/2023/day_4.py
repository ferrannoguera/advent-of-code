import aocd
from functools import reduce


USER_SESSION = 'my_token'

SAMPLE_DATA = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


def _process_scratching_cards(processed_scratching_card, current_card):
    current_card_num = int(current_card[0])
    if processed_scratching_card['cards'].get(current_card_num):
        num_current_cards = processed_scratching_card['cards'][current_card_num] + 1
    else:
        num_current_cards = 1
    processed_scratching_card['result'] += num_current_cards
    won_copies = len(current_card[1][0]) - len(set(current_card[1][0]) - set(current_card[1][1]))
    for idx_copy_current_card in range(num_current_cards):
        for copy in range(current_card_num + 1, current_card_num + won_copies + 1):
            if processed_scratching_card['cards'].get(copy):
                processed_scratching_card['cards'][copy] += 1
            else:
                processed_scratching_card['cards'][copy] = 1
    return processed_scratching_card


if __name__ == '__main__':
    input_data = aocd.get_data(session=USER_SESSION, day=4, year=2023)
    parsed_input_data = [
        (
            parsed_data.split(':')[0].split('Card')[1].strip(),
            [
                [nums.strip() for nums in category_nums.split(' ') if nums]
                for category_nums in parsed_data.split(':')[1].split('|')
            ]
        )
        for parsed_data in input_data.split('\n')
    ]
    total_result_1 = reduce(
        lambda x, y: x + 2 ** ((len(y[1][0]) - len(set(y[1][0]) - set(y[1][1])))-1) if len(y[1][0]) != len(set(y[1][0]) - set(y[1][1]))
        else x,
        parsed_input_data,
        0,
    )
    print(f'Part 1: {total_result_1}')
    total_result_2 = reduce(_process_scratching_cards, parsed_input_data, {'cards': {}, 'result': 0})
    print(f"Part 2: {total_result_2['result']}")

