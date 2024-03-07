from enum import Enum
from functools import cmp_to_key


class Hand(Enum):
    HIGHCARD = 1
    ONEPAIR = 2
    TWOPAIR = 3
    THREEOFAKIND = 4
    FULLHOUSE = 5
    FOUROFAKIND = 6
    FIVEOFAKIND = 7


joker_map = {
    Hand.HIGHCARD: Hand.ONEPAIR,
    Hand.ONEPAIR: Hand.THREEOFAKIND,
    Hand.TWOPAIR: Hand.FULLHOUSE,
    Hand.THREEOFAKIND: Hand.FOUROFAKIND,
    Hand.FULLHOUSE: Hand.FOUROFAKIND,
    Hand.FOUROFAKIND: Hand.FIVEOFAKIND,
    Hand.FIVEOFAKIND: Hand.FIVEOFAKIND
}


def read_hands_from_file(card_strengths):
    file = open("../inputs/input7.txt", "r")
    # file = open("inputs/rough_input.txt", "r")

    hands = []
    for line in file:
        card_strs = line.strip().split(" ")[0]
        card_int_values = list(map(lambda x: card_strengths.index(x), card_strs))
        hand = {
            "cards": card_strs,
            "card_int_values": card_int_values,
            "bet": int(line.strip().split(" ")[1]),
            "type": None
        }
        hands.append(hand)

    return hands


def get_type_for_hand(hand, card_strengths, wildcard_active):
    match_count = {
        Hand.ONEPAIR: 0,
        Hand.THREEOFAKIND: 0
    }
    for card in card_strengths:
        if wildcard_active and card == "J":
            continue
        matches = hand["cards"].count(card)
        if matches < 2:
            continue
        elif matches == 5:
            return Hand.FIVEOFAKIND
        elif matches == 4:
            return Hand.FOUROFAKIND
        elif matches == 3:
            match_count[Hand.THREEOFAKIND] += 1
        elif matches == 2:
            match_count[Hand.ONEPAIR] += 1

    if match_count[Hand.THREEOFAKIND]:
        if match_count[Hand.ONEPAIR]:
            return Hand.FULLHOUSE
        return Hand.THREEOFAKIND

    if match_count[Hand.ONEPAIR] == 2:
        return Hand.TWOPAIR

    if match_count[Hand.ONEPAIR]:
        return Hand.ONEPAIR

    return Hand.HIGHCARD


def get_types_for_hands(hands, card_strengths):
    for hand in hands:
        hand["type"] = get_type_for_hand(hand, card_strengths, False)
    return hands


def get_types_for_hands_2(hands, card_strengths):
    for hand in hands:
        type = get_type_for_hand(hand, card_strengths, True)
        for i in range(hand["cards"].count("J")):
            type = joker_map[type]
        hand["type"] = type
    return hands


def compare_cards(hand1, hand2):
    if hand2["type"].value > hand1["type"].value:
        return 1
    elif hand2["type"].value < hand1["type"].value:
        return -1
    for int_value1, int_value2 in zip(hand1["card_int_values"], hand2["card_int_values"]):
        if int_value2 > int_value1:
            return 1
        elif int_value2 < int_value1:
            return -1
    return 0


def get_result(ranked_hands):
    winnings = 0
    for i in range(len(ranked_hands)):
        winnings += ranked_hands[i]["bet"] * (len(ranked_hands) - i)
    return winnings


def solve_7a(card_strengths):
    hands = read_hands_from_file(card_strengths)
    hands_with_types = get_types_for_hands(hands, card_strengths)
    ranked_hands = sorted(hands_with_types, key=cmp_to_key(compare_cards))
    return get_result(ranked_hands)


def solve_7b(card_strengths):
    hands = read_hands_from_file(card_strengths)
    hands_with_types = get_types_for_hands_2(hands, card_strengths)
    ranked_hands = sorted(hands_with_types, key=cmp_to_key(compare_cards))
    return get_result(ranked_hands)


card_strengths_part_1 = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
card_strengths_part_2 = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

answer1 = solve_7a(card_strengths_part_1)
answer2 = solve_7b(card_strengths_part_2)
print(answer1)
print(answer2)