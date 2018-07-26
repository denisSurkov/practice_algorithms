

def get_correct_cards_set(cards: str) -> list:
    list_of_cards = cards.split()
    cards_with_suite = list(map(lambda x: (x[0:-1], x[-1]), list_of_cards))
    return cards_with_suite


def get_cards_suite(cardset):
    return [i[-1] for i in cardset]


def get_cards_values(cardset):
    return [i[0] for i in cardset]


def check_royal_flush(card_set: list) -> bool:
    these_card_need_to_be = {'A', 'K', 'Q', 'J', '10'}
    card_suite = get_cards_suite(card_set)
    first_suite = card_suite[0]

    suite_check = list(map(lambda x: x == first_suite, card_suite))

    if not all(suite_check):
        return False

    card_values = set(get_cards_values(card_set))

    if these_card_need_to_be == card_values:
        return True
    else:
        return False


def check_straight_flush(card_set: list) -> bool:
    return check_flush(card_set) and check_straight(card_set)


def check_four_of_a_kind(card_set:list) -> bool:
    cards_value = get_cards_values(card_set)

    first_two = cards_value[:2]
    counted = list(map(lambda value: cards_value.count(value), first_two))

    if max(counted) == 4:
        return True
    return False


def check_full_house(cardset: list) -> bool:
    cards_value = get_cards_values(cardset)
    first_three = cards_value[:3]
    counted = list(map(lambda v: cards_value.count(v), first_three))

    # the same value
    if max(counted) != 3:
        return False


    for _ in range(2):
        over_index_of_three = cards_value.index(first_three[counted.index(3)])
        cards_value.remove(cards_value[over_index_of_three])

    if not check_pair(cards_value):
        return False

    return True


def check_flush(cardset: list) -> bool:
    cards_suite = get_cards_suite(cardset)

    if cards_suite.count(cards_suite[0]) == 5:
        return True
    return False


def check_straight(cardset: list) -> bool:
    consecutive_values = ('2', '3', '4', '5', '6', '7', '8', '9', '10',
                          'J', 'Q', 'K', 'A')

    card_values = get_cards_values(cardset)
    card_values.sort(key=lambda x: consecutive_values.index(x))

    prev_index = consecutive_values.index(card_values[0]) - 1

    for i in card_values:
        new_index = consecutive_values.index(i)

        if card_values.index(i) == len(card_values) - 1 and i == 'A':
            continue

        if new_index - 1 != prev_index:
            return False

        prev_index = new_index
    return True


def check_three_of_a_kind(cardset: list) -> bool:
    cards_value = get_cards_values(cardset)

    first_two = cards_value[:3]
    counted = list(map(lambda value: cards_value.count(value), first_two))

    if max(counted) == 3:
        return True
    return False


def check_two_pairs(cardset: list) -> bool:
    card_values = get_cards_values(cardset)
    counted = list(map(lambda x: card_values.count(x), card_values))

    if max(counted) == 2 and counted.count(2) == 4:
        return True
    return False


def check_pair(cardset: list) -> bool:
    card_values = get_cards_values(cardset)
    counted = list(map(lambda x: card_values.count(x), card_values))

    if max(counted) == 2:
        return True

    return False


def check_high_card(*args) -> bool:
    return True


def get_combination(cards: list) -> str:
    order_to_check = ((check_royal_flush, 'Royal Flush'),
                      (check_straight_flush, 'Straight Flush'),
                      (check_four_of_a_kind, 'Four of a Kind'),
                      (check_full_house, 'Full House'),
                      (check_flush, 'Flush'),
                      (check_straight, 'Straight'),
                      (check_three_of_a_kind, 'Three of a Kind'),
                      (check_two_pairs, 'Two Pairs'),
                      (check_pair, 'Pair'),
                      (check_high_card, 'High Card'))

    for func_and_name in order_to_check:
        func = func_and_name[0]
        res = func(cards)
        if res:
            combination = func_and_name[1]
            return combination


def main():
    cards = input()
    cards = get_correct_cards_set(cards)
    combination = get_combination(cards)
    print(combination)


if __name__ == '__main__':
    # main
    with open("poker_test.txt") as fin:
        for line in fin:
            hand = line.strip().split("-")
            s = get_combination(get_correct_cards_set(hand[-1]))
            assert hand[0] == s, hand[-1] + " is " + hand[0] + ", but prog output is: " + s