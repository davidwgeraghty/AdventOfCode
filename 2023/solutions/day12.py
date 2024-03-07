import itertools
from copy import copy
from enum import Enum


class SpringState(Enum):
    WORKING = "."
    DAMAGED = "#"
    UNKNOWN = "?"


def get_data_from_file():
    # file = open("../inputs/input12.txt")
    file = open("../inputs/rough_input.txt")
    records = []
    for line in file:
        record_symbols = line.split(" ")[0]
        record_tallies = list(map(int, (line.split(" ")[1].strip().split(","))))
        records.append({
            "symbols": record_symbols,
            "tallies": record_tallies
        })
    return records


def check_if_valid(symbols, tally_from_file):
    if SpringState.UNKNOWN.value in symbols:
        return False

    tally_from_symbols = []
    damaged_count = 0
    for symbol in symbols:
        if symbol == SpringState.DAMAGED.value:
            damaged_count += 1
        elif damaged_count > 0:
            tally_from_symbols.append(damaged_count)
            damaged_count = 0
    if damaged_count > 0:
        tally_from_symbols.append(damaged_count)

    return tally_from_file == tally_from_symbols


def get_possible_substitutions(unknown_count, spring_states):
    possible_substitutions = []
    # use itertools.product to get all possible combinations of [0,1] for the substitutions needed
    # then map them to the spring states
    # TODO should really factor in the fact that we can't go over the sum of the tallies
    for possible_substitution_numbers in itertools.product(range(0, 2), repeat=unknown_count):
        sub = []
        for number in possible_substitution_numbers:
            sub.append(spring_states[number])
        possible_substitutions.append(sub)
    return possible_substitutions


def get_all_possible_arrangements_for_record(symbols):
    # get unknown count to see how many substitutions we need to make
    unknown_count = symbols.count(SpringState.UNKNOWN.value)
    # get every possible combination of broken and unbroken springs for that number
    spring_states = [SpringState.WORKING.value, SpringState.DAMAGED.value]

    possible_substitutions = get_possible_substitutions(unknown_count, spring_states)
    possible_configurations = []
    for possible_substitution in possible_substitutions:
        configuration = ""
        j = 0
        for i in range(len(symbols)):
            if symbols[i] == SpringState.UNKNOWN.value:
                configuration += possible_substitution[j]
                j += 1
            else:
                configuration += symbols[i]
        possible_configurations.append(configuration)

    return possible_configurations


def get_all_possible_arrangements_for_record_2(record, checksum):
    positions = {0: 1}
    # go through each tally in checksum
    for i, contiguous in enumerate(checksum):
        new_positions = {}
        for k, v in positions.items():
            for n in range(k, len(record) - sum(checksum[i + 1:]) + len(checksum[i + 1:])):
                if n + contiguous - 1 < len(record) and '.' not in record[n:n + contiguous]:
                    if (i == len(checksum) - 1 and '#' not in record[n + contiguous:]) \
                            or (
                            i < len(checksum) - 1 and n + contiguous < len(record) and record[n + contiguous] != '#'):
                        new_positions[n + contiguous + 1] = new_positions[
                                                                n + contiguous + 1] + v if n + contiguous + 1 in new_positions else v
                if record[n] == '#':
                    break
        positions = new_positions
    return positions.values()


def get_records_with_all_possible_arrangements(records):
    for record in records:
        record["possible_arrangements"] = get_all_possible_arrangements_for_record(record["symbols"])
    return records


def get_valid_arrangements(records_with_possible_arrangements):
    valid_arrangements = []
    for record in records_with_possible_arrangements:
        valid_arrangements_for_record = []
        for arrangement in record["possible_arrangements"]:
            if check_if_valid(arrangement, record["tallies"]):
                valid_arrangements_for_record.append(arrangement)
        valid_arrangements.append(valid_arrangements_for_record)
    return valid_arrangements


def unfold_data(records):
    for record in records:
        symbols = copy(record["symbols"])
        tallies = copy(record["tallies"])
        for i in range(0, 5):
            record["symbols"] += "?" + symbols
            record["tallies"].extend(tallies)
    return records


def get_answer(records):
    ways = 0
    for record_row in records:
        record = record_row["symbols"]
        checksum = record_row["tallies"]
        positions = {0: 1}
        for i, contiguous in enumerate(checksum):
            new_positions = {}
            for k, v in positions.items():
                for n in range(k, len(record) - sum(checksum[i + 1:]) + len(checksum[i + 1:])):
                    if n + contiguous - 1 < len(record) and '.' not in record[n:n + contiguous]:
                        if (i == len(checksum) - 1 and '#' not in record[n + contiguous:]) or (
                                i < len(checksum) - 1 and n + contiguous < len(record) and record[
                            n + contiguous] != '#'):
                            new_positions[n + contiguous + 1] = new_positions[
                                                                    n + contiguous + 1] + v if n + contiguous + 1 in new_positions else v
                    if record[n] == '#':
                        break
            positions = new_positions
        ways += sum(positions.values())
    return ways


def part_2_cheat():
    ways = 0
    for row in open("../inputs/rough_input.txt"):
        record, checksum = row.split()
        checksum = [int(n) for n in checksum.split(',')]
        record = '?'.join([record for i in range(5)])
        checksum *= 5
        positions = {0: 1}
        for i, contiguous in enumerate(checksum):
            new_positions = {}
            for k, v in positions.items():
                for n in range(k, len(record) - sum(checksum[i + 1:]) + len(checksum[i + 1:])):
                    if n + contiguous - 1 < len(record) and '.' not in record[n:n + contiguous]:
                        if (i == len(checksum) - 1 and '#' not in record[n + contiguous:]) or (i < len(checksum) - 1 and n + contiguous < len(record) and record[n + contiguous] != '#'):
                            new_positions[n + contiguous + 1] = new_positions[n + contiguous + 1] + v if n + contiguous + 1 in new_positions else v
                    if record[n] == '#':
                        break
            positions = new_positions
        ways += sum(positions.values())
    print(ways)


def do_part_1():
    records = get_data_from_file()
    records_with_possible_arrangements = get_records_with_all_possible_arrangements(records)
    valid_arrangements = get_valid_arrangements(records_with_possible_arrangements)
    sum_of_valid_arrangements = sum(list(map(lambda x: len(x), valid_arrangements)))
    return sum_of_valid_arrangements


def do_part_2():
    records = get_data_from_file()
    unfolded_records = unfold_data(records)
    records_with_possible_arrangements = get_records_with_all_possible_arrangements(unfolded_records)
    valid_arrangements = get_valid_arrangements(records_with_possible_arrangements)
    sum_of_valid_arrangements = sum(list(map(lambda x: len(x), valid_arrangements)))
    return sum_of_valid_arrangements


if __name__ == '__main__':
    # answer1 = do_part_1()
    # answer2 = do_part_2()
    # print(answer1)
    # print(answer2)

    # TODO this is a function copied from https://github.com/tmo1/adventofcode/blob/main/2023/12b.py
    # TODO use stuff from here to make my own (correct) answer
    part_2_cheat()


