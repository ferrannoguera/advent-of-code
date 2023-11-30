from aocd import get_data

USER_SESSION = 'my_user_session'

if __name__ == "__main__":
    input_calories = get_data(session=USER_SESSION, day=1, year=2022)
    input_calories_parsed = [
        [int(elem) for elem in list_of_elems.split('\n')] for list_of_elems in input_calories.split('\n\n')
    ]
    elf_with_max_calories = max(sum(elf_calories) for elf_calories in input_calories_parsed)
    print(elf_with_max_calories)


