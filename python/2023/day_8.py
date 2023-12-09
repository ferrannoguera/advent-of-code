import aocd
import math


USER_SESSION = 'my_token'

SAMPLE_DATA = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

SAMPLE_DATA_2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

SAMPLE_DATA_3 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

if __name__ == '__main__':
    input_data = aocd.get_data(session=USER_SESSION, day=8, year=2023)
    parsed_input_data = [parsed_data for parsed_data in input_data.split('\n')]
    instructions = parsed_input_data[0]
    rules = {
        rule.split(' = ')[0]: (rule.split(' = ')[1].split(',')[0][1:], rule.split(' = ')[1].split(',')[1][1:-1])
        for rule in parsed_input_data[2:]
    }
    # Part 1
    found_node = 'AAA'
    steps = 0
    instructions_idx = 0
    while True:
        if found_node == 'ZZZ':
            break
        else:
            found_node = rules[found_node][0] if instructions[instructions_idx] == 'L' else rules[found_node][1]
            steps += 1
            instructions_idx = (instructions_idx + 1) % len(instructions)
    print(f'Part 1: {steps}')
    # Part 2
    found_nodes = [nodes for nodes in rules.keys() if nodes.endswith('A')]
    solutions = []
    for found_node in found_nodes:
        steps = 0
        instructions_idx = 0
        while True:
            if found_node.endswith('Z'):
                break
            else:
                found_node = rules[found_node][0] if instructions[instructions_idx] == 'L' else rules[found_node][1]
                steps += 1
                instructions_idx = (instructions_idx + 1) % len(instructions)
        solutions.append(steps)
    print(f'Part 2: {math.lcm(*solutions)}')
