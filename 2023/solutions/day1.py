number_list = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]


def advent_solve_a():
    total = 0

    file = open("../inputs/input.txt", "r")

    for line in file:
        total += get_number_for_line(line)

    return total


def get_number_for_line(line):
    number = ''
    # iterate through from start to find first number
    #   - stop when found
    #   - if there's no number return 0
    for char in line:
        if char.isdigit():
            number += char
            break

    if number == '':
        return 0

    # iterate through from end to find last number - stop when found
    # if no number found just return 0
    for char in reversed(line):
        if char.isdigit():
            number += char
            return int(number)


def advent_solve_b():
    total = 0

    file = open("../inputs/input.txt", "r")
    # file = open("inputs/rough_input.txt", "r")

    for line in file:
        total += get_number_for_line_b(line)

    return total


def get_first_digit_for_line(line):
    digit = ''
    digit_index = None

    for i in range(0, len(line)):
        if line[i].isdigit():
            digit_index = i
            break

    # check for 'one', 'two' etc
    word_index = None
    for i in range(0, len(number_list)):
        word = number_list[i]
        if word in line:
            if word_index is None or line.find(word) < word_index:
                word_index = line.find(word)
                digit = str(i)

    if word_index is None or (digit_index is not None and digit_index < word_index):
        digit = line[digit_index]

    return digit


def get_second_digit_for_line(line):
    digit = ''
    digit_index = None

    backwards_line = line[::-1]

    for i in range(0, len(backwards_line)):
        if backwards_line[i].isdigit():
            digit_index = len(backwards_line) - 1 - i
            break

    # check for 'one', 'two' etc
    word_index = None
    for i in range(0, len(number_list)):
        word = number_list[i]
        if word in line:
            if word_index is None or line.rfind(word) > word_index:
                word_index = line.rfind(word)
                digit = str(i)

    if word_index is None or (digit_index is not None and digit_index > word_index):
        digit = line[digit_index]

    return digit


def get_number_for_line_b(line):
    first_digit = get_first_digit_for_line(line.strip())

    # this doesn't work - need to keep the list intact and iterate backwards
    second_digit = get_second_digit_for_line(line.strip())

    number = first_digit + second_digit
    if number == '':
        return 0

    return int(number)


if __name__ == '__main__':
    answer1 = advent_solve_a()
    answer2 = advent_solve_b()
    print(answer2)
