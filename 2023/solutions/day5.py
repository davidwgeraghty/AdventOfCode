from itertools import chain


def get_translated_ids(source_ids, translations):
    temp_source_ids = source_ids.copy()
    translated_ids = []
    for translation in translations:
        for source_id in source_ids:
            if source_id in translation["source_range"]:
                translated_ids.append(source_id + translation["translation_amount"])
                temp_source_ids.remove(source_id)

    # don't forget to keep ids with no translation applied
    return translated_ids + temp_source_ids


def find_items_for_items(source, destination, ids, elf_maps):
    if source == destination:
        return ids

    translated_ids = get_translated_ids(ids, elf_maps[source]["translations"])
    return find_items_for_items(elf_maps[source]["destination"], destination, translated_ids, elf_maps)


def solve_5a():
    # get all objects from file
    seed_ids, elf_maps = get_data_from_file()

    # calculate transversal of relationships
    location_ids = find_items_for_items("seed", "location", seed_ids, elf_maps)

    return min(location_ids)


def get_data_from_file():
    file = open("../inputs/input5.txt", "r")
    # file = open("inputs/rough_input.txt", "r")

    seed_numbers = []
    elf_maps = {}

    source = ""
    for line in file:
        # get seed ids
        if "seeds:" in line:
            seed_numbers = list(map(int, line.split("seeds: ")[1].split()))
        # process maps
        elif "-to-" in line:
            source = line.split("-to-")[0]
            destination = line.split("-to-")[1].split(" map")[0]
            elf_maps[source] = {
                "destination": destination,
                "translations": []
            }
        elif any(character.isdigit() for character in line):
            translation_numbers = list(map(int, line.split()))
            destination_range_start = translation_numbers[0]
            source_range_start = translation_numbers[1]
            range_length = translation_numbers[2]
            translation = {
                "source_range": range(source_range_start, source_range_start + range_length),
                "translation_amount": destination_range_start - source_range_start
            }
            elf_maps[source]["translations"].append(translation)

    return seed_numbers, elf_maps


def get_seed_id_ranges_from_seed_numbers(seed_numbers):
    seed_id_ranges = []

    for i in range(0, len(seed_numbers), 2):
        seed_id_ranges.append(range(seed_numbers[i], seed_numbers[i] + seed_numbers[i + 1]))

    return seed_id_ranges


def get_translated_id_ranges(source_id_ranges, translations):
    untranslated_id_ranges = []
    translated_id_ranges = []
    for source_id_range in source_id_ranges:
        translation_found = False
        for translation in translations:
            # check for intersection between given ids and id map ranges
            intersection = range(
                max(source_id_range.start, translation["source_range"].start),
                min(source_id_range.stop, translation["source_range"].stop)
            )
            if intersection:
                translation_found = True
                translated_range = range(intersection.start + translation["translation_amount"],
                                         intersection.stop + translation["translation_amount"])
                translated_id_ranges.append(translated_range)

                # create ranges for leftover untranslated ids
                untranslated_ranges = [
                    range(source_id_range.start, intersection.start),
                    range(intersection.stop, source_id_range.stop)
                    ]
                for untranslated_range in untranslated_ranges:
                    if untranslated_range:
                        untranslated_id_ranges.append(untranslated_range)

        # keep untranslated ids
        if not translation_found:
            untranslated_id_ranges.append(source_id_range)

    # merge ranges for tidiness
    return chain(translated_id_ranges + untranslated_id_ranges)


def find_item_ranges_for_item_ranges(source, destination, id_ranges, elf_maps):
    if source == destination:
        return id_ranges

    translated_id_ranges = get_translated_id_ranges(id_ranges, elf_maps[source]["translations"])
    return find_item_ranges_for_item_ranges(elf_maps[source]["destination"], destination, translated_id_ranges, elf_maps)


def find_minimum_id(id_ranges):
    min_id = None
    for id_range in id_ranges:
        if not min_id:
            min_id = id_range.start
        elif id_range.start < min_id:
            min_id = id_range.start

    return min_id


def solve_5b():
    # get all objects from file
    seed_numbers, elf_maps = get_data_from_file()
    seed_id_ranges = get_seed_id_ranges_from_seed_numbers(seed_numbers)

    # calculate transversal of relationships
    id_ranges = find_item_ranges_for_item_ranges("seed", "location", seed_id_ranges, elf_maps)
    minimum_id = find_minimum_id(id_ranges)

    return minimum_id


if __name__ == "__main__":
    # answer1 = solve_5a()
    answer2 = solve_5b()
    # print(answer1)
    print(answer2)


# TODO write unit tests to find the problem
