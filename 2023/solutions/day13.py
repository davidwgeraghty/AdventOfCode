import math

def get_data_from_file():
    # file = open("../inputs/input12.txt")
    file = open("../inputs/rough_input.txt")
    patterns = []
    rows = []
    for line in file:
        if line == "\n":
            patterns.append({"pattern": rows})
            rows = []
        rows.append(line.strip())
    # don't forget last pattern
    patterns.append(rows)
    return patterns


def is_mirror(pattern_rows, possible_mirror):
    for i in range(math.ceil(possible_mirror)):
        mirrored_row = 2 * possible_mirror - i
        if mirrored_row < len(pattern_rows) and pattern_rows[i] != pattern_rows[mirrored_row]:
            return False
    return True


def get_mirror_positions(patterns):
    for pattern in patterns:
        pattern_rows = pattern["pattern"]

        horizontal_mirrors = []
        for i, row in enumerate(pattern_rows):
            for j in range(i + 1, len(pattern_rows)):
                if row == pattern_rows[j]:
                    # TODO this bit is probably wrong
                    possible_mirror = (j - i)/2
                    if is_mirror(pattern_rows, possible_mirror):
                        horizontal_mirrors.append(possible_mirror)

        vertical_mirrors = []
        for i, column in enumerate(zip(*pattern_rows)):
            for j in range(i+1, len(pattern_rows)):
                if column == pattern_rows[j]:
                    possible_mirror = (j - i) / 2
                    if is_mirror(pattern_rows, possible_mirror):
                        vertical_mirrors.append(possible_mirror)

        pattern["horizontal_mirrors"] = horizontal_mirrors
        pattern["vertical_mirrors"] = vertical_mirrors
    return patterns


def do_part_1():
    patterns = get_data_from_file()
    # think about cases where there are multiple reflection lines
    patterns = get_mirror_positions(patterns)

    return patterns


if __name__ == '__main__':
    answer1 = do_part_1()
    print(answer1)
    # answer2 = do_part_2()
    # print(answer2)