from math import lcm


def get_data_from_file():
    # file = open("inputs/rough_input.txt", "r")
    file = open("../inputs/input8.txt", "r")
    instructions = file.readline().strip()

    letter_map = {}

    for line in file:
        if "=" in line:
            source = line.split(" =")[0]
            letter_map[source] = {
                "L": line.split("(")[1].split(",")[0],
                "R": line.split(", ")[1].split(")")[0].strip()
            }

    return instructions, letter_map


def traverse_map(instructions, letter_map, current, destination):
    steps = 0
    while current != destination:
        for instruction in instructions:
            current = letter_map[current][instruction]
            steps += 1

            if current == destination:
                return steps


def check_if_done(current_nodes):
    for current_node in current_nodes:
        if current_node[2] != "Z":
            return False
    return True


def traverse_map_2(instructions, letter_map):
    steps = 0

    current_nodes = list(filter(lambda x: x[2] == "A", list(letter_map.keys())))
    z_node_steps = []
    while current_nodes:
        for instruction in instructions:
            current_nodes = list(map(lambda current_node: letter_map[current_node][instruction], current_nodes))
            steps += 1

            for current_node in current_nodes:
                if current_node[2] == "Z":
                    z_node_steps.append(steps)
                    current_nodes.remove(current_node)

            if not current_nodes:
                break

    return lcm(*z_node_steps)


def do_part_1():
    instructions, letter_map = get_data_from_file()
    steps = traverse_map(instructions, letter_map, "AAA", "ZZZ")
    return steps


def do_part_2():
    instructions, letter_map = get_data_from_file()
    steps = traverse_map_2(instructions, letter_map)
    return steps


# answer1 = do_part_1()
answer2 = do_part_2()
# print(answer1)
print(answer2)