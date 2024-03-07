# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def advent_solve():
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    answer = advent_solve()
    print(answer)

