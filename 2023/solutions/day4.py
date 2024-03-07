def get_cards_from_file():
    cards = []
    file = open("../inputs/input4.txt", "r")
    # file = open("inputs/rough_input.txt", "r")
    for line in file:
        card_id = line.split("Card ")[1].split(":")[0]
        winning_numbers = list(map(int, line.split(":")[1].split("|")[0].split()))
        your_numbers = list(map(int, line.split("|")[1].split()))
        card = {
            "id": int(card_id),
            "winning_numbers": winning_numbers,
            "your_numbers": your_numbers,
            "points": None
        }
        cards.append(card)

    return cards


def calculate_matched_numbers_for_cards(cards):
    for card in cards:
        card["matched_numbers"] = [number for number in card["your_numbers"] if number in card["winning_numbers"]]
    return cards


def calculate_points_for_card(card):
    if card["matched_numbers"]:
        card["points"] = pow(2, (len(card["matched_numbers"]) - 1))
    else:
        card["points"] = 0

    return card


def advent_solve_4a():
    cards = get_cards_from_file()
    cards = calculate_matched_numbers_for_cards(cards)
    cards_with_points = list(map(calculate_points_for_card, cards))

    return sum(list(map(lambda card: card["points"], cards_with_points)))


def get_total_card_count_with_duplicates(cards):
    for card in cards:
        card["card_count"] = 1

    # go through all cards
    for i in range(0, len(cards)):
        # for each card id, go through total card count
        for j in range(0, cards[i]["card_count"]):
            # for number of matched winning numbers for that card, increase the card count for the next cards
            for k in range(0, len(cards[i]["matched_numbers"])):
                cards[i + 1 + k]["card_count"] += 1

    return cards


def sum_cards_with_duplicates(cards_with_duplicate_count):
    sum = 0
    for card in cards_with_duplicate_count:
        sum += card["card_count"]
    return sum


def advent_solve_4b():
    cards = get_cards_from_file()
    cards = calculate_matched_numbers_for_cards(cards)
    cards_with_duplicate_count = get_total_card_count_with_duplicates(cards)
    total_card_count = sum_cards_with_duplicates(cards_with_duplicate_count)

    return total_card_count


if __name__ == "__main__":
    # answer1 = advent_solve_4a()
    answer2 = advent_solve_4b()
    # print(answer1)
    print(answer2)