def get_data_from_file():
    # file = open("../inputs/rough_input.txt")
    file = open("../inputs/input11.txt")

    universe = []
    for line in file:
        universe.append(line.strip())

    return universe


def get_expanded_universe(universe, expansion_coefficient):
    temp_universe = []
    for line in universe:
        # add universe expansion
        if line.count(".") == len(line.strip()):
            for i in range(0, expansion_coefficient):
                temp_universe.append(line.strip())
        else:
            temp_universe.append(line.strip())

    rotated_universe = []
    for column in zip(*temp_universe):
        if column.count(".") == len(column):
            for i in range(0, expansion_coefficient):
                rotated_universe.append(column)
        else:
            rotated_universe.append(column)

    # rotate back
    return list(zip(*rotated_universe))


def get_galaxies(expanded_universe):
    galaxies = []
    for y in range(0, len(expanded_universe)):
        for x in range(0, len(expanded_universe[y])):
            if expanded_universe[y][x] == "#":
                galaxies.append({
                    "x": x,
                    "y": y
                })
    return galaxies


def get_galaxies_distances(galaxies, empty_rows, empty_columns):
    distances = []
    for i in range(0, len(galaxies)):
        for j in range(i+1, len(galaxies)):
            distance = abs(galaxies[i]["x"] - galaxies[j]["x"]) + abs(galaxies[i]["y"] - galaxies[j]["y"])
            for row_number in empty_rows:
                if galaxies[i]["y"] < row_number < galaxies[j]["y"] or galaxies[i]["y"] > row_number > galaxies[j]["y"]:
                    distance += 999999
            for column_number in empty_columns:
                if galaxies[i]["x"] < column_number < galaxies[j]["x"] or galaxies[i]["x"] > column_number > galaxies[j]["x"]:
                    distance += 999999
            distances.append(distance)
    return distances


def get_empty_rows_and_columns(universe):
    empty_rows = []
    for i in range(0, len(universe)):
        if universe[i].count(".") == len(universe[i].strip()):
            empty_rows.append(i)

    empty_columns = []
    for i, column in enumerate(list(zip(*universe))):
        if column.count(".") == len(column):
            empty_columns.append(i)

    return empty_rows, empty_columns


def do_part_1():
    universe = get_data_from_file()
    expanded_universe = get_expanded_universe(universe, 2)
    galaxies = get_galaxies(expanded_universe)
    distances = get_galaxies_distances(galaxies, [], [])
    return sum(distances)


def do_part_2():
    universe = get_data_from_file()
    galaxies = get_galaxies(universe)
    empty_rows, empty_columns = get_empty_rows_and_columns(universe)
    distances = get_galaxies_distances(galaxies, empty_rows, empty_columns)

    return sum(distances)


if __name__ == '__main__':
    # answer1 = do_part_1()
    answer2 = do_part_2()
    # print(answer1)
    print(answer2)