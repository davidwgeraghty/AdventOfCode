def get_data_from_file():
    # file = open("inputs/rough_input.txt", "r")
    file = open("inputs/input9.txt", "r")

    sequences = []
    for line in file:
        sequences.append(list(map(lambda x: int(x), line.split(" "))))
    return sequences


def add_one_to_either_end_of_sequence(sequences):
    for sequence in sequences:
        next_number = get_next_number(sequence)
        previous_number = get_previous_number(sequence)
        sequence.append(next_number)
        sequence.insert(0, previous_number)
    return sequences


def get_previous_number(sequence):
    while sequence.count(0) != len(sequence):
        differences = []
        for i in range(len(sequence) - 1):
            differences.append(sequence[i + 1] - sequence[i])
        if differences.count(0) == len(differences):
            return sequence[0]
        return sequence[0] - get_previous_number(differences)


def get_next_number(sequence):
    while sequence.count(0) != len(sequence):
        differences = []
        for i in range(len(sequence) - 1):
            differences.append(sequence[i + 1] - sequence[i])
        if differences.count(0) == len(differences):
            return sequence[-1]
        return sequence[-1] + get_next_number(differences)
    return 0


def do_part_1():
    sequences = get_data_from_file()
    sequences = add_one_to_either_end_of_sequence(sequences)

    return sum(list(map(lambda x: x[-1], sequences)))


def do_part_2():
    sequences = get_data_from_file()
    sequences = add_one_to_either_end_of_sequence(sequences)

    return sum(list(map(lambda x: x[0], sequences)))

if __name__ == '__main__':
    answer1 = do_part_1()
    answer2 = do_part_2()
    print(answer1)
    print(answer2)
