import operator
from copy import deepcopy

directions = {
    "|": [(0, 1), (0, -1)],
    "-": [(1, 0), (-1, 0)],
    "L": [(0, -1), (1, 0)],
    "J": [(0, -1), (-1, 0)],
    "7": [(-1, 0), (0, 1)],
    "F": [(0, 1), (1, 0)]
}
 

def get_data_from_file():
    # file = open("../inputs/rough_input.txt")
    file = open("../inputs/input10.txt")

    file_lists = file.readlines()
    rows = []
    for i in range(len(file_lists)):
        rows.append(list(file_lists[i].strip()))
        if "S" in file_lists[i]:
            start_point_coords = (file_lists[i].index("S"), i)

    return rows, start_point_coords


def get_next_node(sketch, previous_coordinates, current_coordinates):
    vector_to_previous = tuple(map(operator.sub, previous_coordinates, current_coordinates))
    current_symbol = sketch[current_coordinates[1]][current_coordinates[0]]

    if current_symbol != "S":
        next_node_vector = list(filter(lambda x: x != vector_to_previous, directions[current_symbol]))[0]
        next_node_coords = (current_coordinates[0] + next_node_vector[0], current_coordinates[1] + next_node_vector[1])
        next_node_symbol = sketch[next_node_coords[1]][next_node_coords[0]]
        return next_node_symbol, next_node_coords
    else:
        surrounding_nodes = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                if (x, y) != (0, 0) and (x, y) != vector_to_previous:
                    symbol = sketch[current_coordinates[1] + y][current_coordinates[0] + x]
                    surrounding_nodes.append({
                        "symbol": symbol,
                        "coordinates": (x, y)
                    })
        for surrounding_node in surrounding_nodes:
            if surrounding_node["symbol"] != ".":
                vectors_for_symbol = directions[surrounding_node["symbol"]]
                opposite_vectors = []
                for vector in vectors_for_symbol:
                    opposite_vectors.append(tuple([-1*i for i in vector]))
                if surrounding_node["coordinates"] in opposite_vectors:
                    return surrounding_node["symbol"], tuple(map(lambda i, j: i + j, current_coordinates, surrounding_node["coordinates"]))


def get_full_route(sketch, previous_node_coords, current_node_coords):
    route = [current_node_coords]
    current_node_symbol, current_node_coords = get_next_node(sketch, previous_node_coords, current_node_coords)

    while current_node_symbol != "S":
        route.append(current_node_coords)
        temp_coords = deepcopy(current_node_coords)
        current_node_symbol, current_node_coords = get_next_node(sketch, previous_node_coords, current_node_coords)
        previous_node_coords = temp_coords

    return route


def do_part_1():
    sketch, start_point_coords = get_data_from_file()
    route = get_full_route(sketch, start_point_coords, start_point_coords)

    return int(len(route) / 2)


def do_part_2():
    pass


if __name__ == '__main__':
    answer1 = do_part_1()
    # answer2 = do_part_2()
    print(answer1)
    # print(answer2)