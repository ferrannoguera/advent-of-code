from aocd import get_data

USER_SESSION = '53616c7465645f5f482bd5a563018311b6a153ca12437a8c490e82963acb708f58baf18173026ce6eb22b615d9957eae2f2589c99a75c636910f9637fd85aa53'

if __name__ == "__main__":
    # Reading input
    input_calories = get_data(session=USER_SESSION, day=1, year=2022)
    input_calories_parsed = [
        [int(elem) for elem in list_of_elems.split('\n')] for list_of_elems in input_calories.split('\n\n')
    ]
    # First star
    elf_with_max_calories = max(sum(elf_calories) for elf_calories in input_calories_parsed)
    print(f'First question: {elf_with_max_calories}')
    # Second star
    three_elfs_max_calories = sorted(input_calories_parsed, key=sum, reverse=True)[:3]
    print(f'Second question: {sum(sum(elf_calories) for elf_calories in three_elfs_max_calories)}')



