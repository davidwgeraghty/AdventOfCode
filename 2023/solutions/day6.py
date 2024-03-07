import numpy


def read_file():
    # lines = open("inputs/rough_input.txt", "r").readlines()
    lines = open("../inputs/input6.txt", "r").readlines()
    times = list(map(int, lines[0].split(":")[1].split()))
    distances = list(map(int, lines[1].split(":")[1].split()))
    return times, distances


def get_games(times, distances):
    games = []
    for i in range(0, len(times)):
        games.append({
            "time": times[i],
            "distance": distances[i]
        })
    return games


def get_winning_charge_times_for_game(game):
    game["winning_times"] = []
    for charge_time in range(0, game["time"]):
        time_left_after_charging = game["time"] - charge_time
        distance = time_left_after_charging * charge_time
        if distance > game["distance"]:
            game["winning_times"].append(charge_time)
    return game


def solve_6a():
    times, distances = read_file()
    games = get_games(times, distances)
    winning_charge_times_for_each_game = list(map(get_winning_charge_times_for_game, games))
    winning_possibilities = list(map(lambda game: len(game["winning_times"]), winning_charge_times_for_each_game))

    return numpy.prod(winning_possibilities)


def solve_6b():
    times, distances = read_file()
    time = int(''.join(str(x) for x in times))
    distance = int(''.join(str(x) for x in distances))
    game = get_winning_charge_times_for_game({"time": time, "distance": distance})

    return len(game["winning_times"])


answer1 = solve_6a()
answer2 = solve_6b()
print(answer1)
print(answer2)