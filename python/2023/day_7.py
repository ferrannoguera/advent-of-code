import aocd


USER_SESSION = 'my_token'

SAMPLE_DATA = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

def _count_bids(_hand_type, _shift):
    _hand_sorted = [item[1] for item in sorted(_hand_type.items())]
    hands_winnings = 0
    for idx, bid in enumerate(_hand_sorted):
        hands_winnings += int(bid) * (idx + _shift)
    return hands_winnings


def _get_hand_type(
        _round, _bid, _five_of_a_kind, _four_of_a_kind, _full_house, _three_of_a_kind, _two_pairs, _one_pair,
        _high_card, _part_2=False
):
    _hand = dict()
    for number in _round:
        if number[0] in _hand:
            _hand[number[0]] += 1
        else:
            _hand[number[0]] = 1

    if _bid == '19':
        test = True
    total_jokers = 0 if not _part_2 else _round.count('1')
    if total_jokers:
        del _hand['1']

    if total_jokers == 5:
        _five_of_a_kind[_round] = _bid
    elif max(_hand.values()) + total_jokers == 5:
        _five_of_a_kind[_round] = _bid
    elif max(_hand.values()) + total_jokers == 4 or total_jokers == 4:
        _four_of_a_kind[_round] = _bid
    elif total_jokers == 3:
        if list(_hand.values()).count(2) == 1:
            _full_house[_round] = _bid
        else:
            _three_of_a_kind[_round] = _bid
    elif max(_hand.values()) + total_jokers == 3:
        if total_jokers == 1 and list(_hand.values()).count(2) == 2:
            _full_house[_round] = _bid
        elif max(_hand.values()) == 3 and list(_hand.values()).count(2) == 1:
            _full_house[_round] = _bid
        else:
            _three_of_a_kind[_round] = _bid
    elif max(_hand.values()) + total_jokers == 2 or total_jokers == 2:
        from_joker = total_jokers == 2
        if list(_hand.values()).count(2) == 2 or (list(_hand.values()).count(2) == 1 and from_joker):
            _two_pairs[_round] = _bid
        else:
            _one_pair[_round] = _bid
    else:
        _high_card[_round] = _bid


if __name__ == '__main__':
    input_data = aocd.get_data(session=USER_SESSION, day=7, year=2023)
    parsed_input_data = [parsed_data.split() for parsed_data in input_data.split('\n')]

    _five_of_a_kind = {}
    _four_of_a_kind = {}
    _full_house = {}
    _three_of_a_kind = {}
    _two_pairs = {}
    _one_pair = {}
    _high_card = {}
    for _data_idx, data in enumerate(parsed_input_data):
        _round, _bid = data
        _round = _round.replace('T', 'V')
        _round = _round.replace('J', 'W')
        _round = _round.replace('Q', 'X')
        _round = _round.replace('K', 'Y')
        _round = _round.replace('A', 'Z')
        _get_hand_type(
            _round,
            _bid,
            _five_of_a_kind,
            _four_of_a_kind,
            _full_house,
            _three_of_a_kind,
            _two_pairs,
            _one_pair,
            _high_card,
        )
    total_winnings = 0
    shifted = 1
    if _high_card:
        total_winnings += _count_bids(_high_card, shifted)
        shifted += len(_high_card)
    if _one_pair:
        total_winnings += _count_bids(_one_pair, shifted)
        shifted += len(_one_pair)
    if _two_pairs:
        total_winnings += _count_bids(_two_pairs, shifted)
        shifted += len(_two_pairs)
    if _three_of_a_kind:
        total_winnings += _count_bids(_three_of_a_kind, shifted)
        shifted += len(_three_of_a_kind)
    if _full_house:
        total_winnings += _count_bids(_full_house, shifted)
        shifted += len(_full_house)
    if _four_of_a_kind:
        total_winnings += _count_bids(_four_of_a_kind, shifted)
        shifted += len(_four_of_a_kind)
    if _five_of_a_kind:
        total_winnings += _count_bids(_five_of_a_kind, shifted)
        shifted += len(_five_of_a_kind)
    print(f'Part 1: {total_winnings}')

    _five_of_a_kind = {}
    _four_of_a_kind = {}
    _full_house = {}
    _three_of_a_kind = {}
    _two_pairs = {}
    _one_pair = {}
    _high_card = {}
    for _data_idx, data in enumerate(parsed_input_data):
        _round, _bid = data
        _round = _round.replace('T', 'V')
        _round = _round.replace('J', '1')
        _round = _round.replace('Q', 'X')
        _round = _round.replace('K', 'Y')
        _round = _round.replace('A', 'Z')
        _get_hand_type(
            _round,
            _bid,
            _five_of_a_kind,
            _four_of_a_kind,
            _full_house,
            _three_of_a_kind,
            _two_pairs,
            _one_pair,
            _high_card,
            True
        )
    total_winnings = 0
    shifted = 1
    if _high_card:
        total_winnings += _count_bids(_high_card, shifted)
        shifted += len(_high_card)
    if _one_pair:
        total_winnings += _count_bids(_one_pair, shifted)
        shifted += len(_one_pair)
    if _two_pairs:
        total_winnings += _count_bids(_two_pairs, shifted)
        shifted += len(_two_pairs)
    if _three_of_a_kind:
        total_winnings += _count_bids(_three_of_a_kind, shifted)
        shifted += len(_three_of_a_kind)
    if _full_house:
        total_winnings += _count_bids(_full_house, shifted)
        shifted += len(_full_house)
    if _four_of_a_kind:
        total_winnings += _count_bids(_four_of_a_kind, shifted)
        shifted += len(_four_of_a_kind)
    if _five_of_a_kind:
        total_winnings += _count_bids(_five_of_a_kind, shifted)
        shifted += len(_five_of_a_kind)
    print(f'Part 2: {total_winnings}')
