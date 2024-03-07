import re


def get_schema_from_file():
    file = open("../inputs/input3.txt", "r")
    # file = open("inputs/rough_input.txt", "r")
    rows = []
    for line in file:
        rows.append(list(line.strip()))

    return rows


def get_surrounding_characters(schema, y, x):
    surrounding_characters = []

    # row above
    if y > 0:
        # top left
        if x > 0:
            surrounding_characters.append(schema[y - 1][x - 1])
        # top middle
        surrounding_characters.append(schema[y - 1][x])
        # top right
        if x < len(schema[y]) - 1:
            surrounding_characters.append(schema[y - 1][x + 1])

    # current row
    # left
    if x > 0:
        surrounding_characters.append(schema[y][x - 1])
    # right
    if x < len(schema[y]) - 1:
        surrounding_characters.append(schema[y][x + 1])

    # bottom
    if y < len(schema) - 1:
        # bottom left
        if x > 0:
            surrounding_characters.append(schema[y + 1][x - 1])
        # bottom middle
        surrounding_characters.append(schema[y + 1][x])
        # bottom right
        if x < len(schema[y]) - 1:
            surrounding_characters.append(schema[y + 1][x + 1])

    return surrounding_characters


def get_part_numbers(schema):
    part_numbers = []
    for y in range(0, len(schema)):
        # number_str = ''
        part_number_digits = []
        is_part_number = False
        for x in range(0, len(schema[y])):
            if schema[y][x].isdigit():
                # number_str += schema[y][x]
                part_number_digits.append({
                    "digit": schema[y][x],
                    "x": x,
                    "y": y
                })
                surrounding_characters = get_surrounding_characters(schema, y, x)
                if re.search("[^0-9^a-z^.]", ''.join(surrounding_characters)):
                    is_part_number = True
            # encounter a . or symbol -> store int
            else:
                if is_part_number:
                    part_numbers.append(part_number_digits)
                    # part_numbers.append(int(number_str))
                is_part_number = False
                # number_str = ''
                part_number_digits = []

            # if it's the end of the row, store the number
            if x == len(schema[y]) - 1 and is_part_number:
                part_numbers.append(part_number_digits)
                # part_numbers.append(int(number_str))

    return part_numbers


def get_part_numbers_for_gear(part_numbers, x, y):
    gear_part_numbers = []
    for part_number in part_numbers:
        for part_number_digit in part_number:
            if x - 1 <= part_number_digit["x"] <= x + 1\
                    and y - 1 <= part_number_digit["y"] <= y + 1\
                    and part_number not in gear_part_numbers:
                gear_part_numbers.append(part_number)

    return gear_part_numbers


def filter_gears_with_two_part_numbers(gear):
    return len(gear["part_numbers"]) == 2


def get_gears(schema, part_numbers):
    gears = []
    for y in range(0, len(schema)):
        for x in range(0, len(schema[y])):
            if schema[y][x] == "*":
                gears.append({
                    "x": x,
                    "y": y,
                    "part_numbers": get_part_numbers_for_gear(part_numbers, x, y)
                })

    return list(filter(filter_gears_with_two_part_numbers, gears))


def get_part_number_int(part_number):
    part_number_str = ''
    for digit in part_number:
        part_number_str += digit["digit"]
    return int(part_number_str)


def advent_solve_3a():
    schema = get_schema_from_file()
    part_numbers = get_part_numbers(schema)
    part_number_ints = list(map(get_part_number_int, part_numbers))

    return sum(part_number_ints)


def get_gear_ratios(gears):
    gear_ratios = []

    for gear in gears:
        ratio = 1
        for part_number in gear["part_numbers"]:
            ratio *= get_part_number_int(part_number)

        gear_ratios.append(ratio)

    return gear_ratios


def advent_solve_3b():
    schema = get_schema_from_file()
    part_numbers = get_part_numbers(schema)
    gears = get_gears(schema, part_numbers)
    gear_ratios = get_gear_ratios(gears)
    return sum(gear_ratios)


if __name__ == "__main__":
    answer1 = advent_solve_3a()
    answer2 = advent_solve_3b()
    # print(answer1)
    print(answer2)