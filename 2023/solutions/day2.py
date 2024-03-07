from enum import Enum


class Color(Enum):
    red = 1
    green = 2
    blue = 3


def get_game_from_line(line):
    game_id = int(line.split("Game ")[1].split(":")[0])
    sets_str_list = line.split(": ")[1].split(";")
    set_dicts = []
    for set in sets_str_list:
        set_dict = {i.name: 0 for i in Color}
        cube_colour_count = set.split(",")

        for cube_colour in cube_colour_count:
            for key in set_dict:
                if key in cube_colour:
                    cube_count = int(''.join(x for x in cube_colour if x.isdigit()))
                    set_dict[key] = cube_count

                    break

        set_dicts.append(set_dict)

    return {
        "game_id": game_id,
        "set_dicts": set_dicts
    }


def get_games_from_file():
    file = open("../inputs/input2.txt", "r")
    # file = open("inputs/rough_input.txt", "r")

    games = []
    for line in file:
        games.append(get_game_from_line(line))

    return games


def check_possible(game):
    max_cubes_by_colour = {
        Color.red.name: 12,
        Color.green.name: 13,
        Color.blue.name: 14
    }
    for set in game["set_dicts"]:
        for colour in max_cubes_by_colour:
            if set[colour] > max_cubes_by_colour[colour]:
                return False

    return True


def get_possible_games(games):
    return list(filter(check_possible, games))


def get_games_ids(games):
    ids = []
    for game in games:
        ids.append(game["game_id"])
    return ids


def advent_solve_2a():
    games = get_games_from_file()
    possible_games = get_possible_games(games)
    possible_game_ids = get_games_ids(possible_games)
    total = sum(possible_game_ids)
    return total


def calculate_fewest(game):
    fewest = {i.name: 0 for i in Color}

    for set in game["set_dicts"]:
        for colour in fewest:
            if set[colour] > fewest[colour]:
                fewest[colour] = set[colour]

    return fewest



def get_fewest_cubes_per_game(games):
    return list(map(calculate_fewest, games))


def get_power(fewest_cubes_per_game):
    power = 1
    for key in fewest_cubes_per_game:
        power *= fewest_cubes_per_game[key]

    return power


def get_powers_from_fewest_list(fewest_cubes_per_game):
    return list(map(get_power, fewest_cubes_per_game))


def advent_solve_2b():
    games = get_games_from_file()
    fewest_cubes_per_game = get_fewest_cubes_per_game(games)
    powers = get_powers_from_fewest_list(fewest_cubes_per_game)
    return sum(powers)


if __name__ == '__main__':
    answer1 = advent_solve_2a()
    answer2 = advent_solve_2b()
    # print(answer1)
    print(answer2)
