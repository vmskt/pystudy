""" Написать функцию, которая берёт на вход набор карт (строго говоря, 7 карт, но на самом деле, это не важно)
и возвращает старшую пятикарточную комбинацию в этом наборе."""
# Hand values:
    # Highcard - Simple value of the card. Lowest: 2 – Highest: Ace (King in example)
    # Pair - Two cards with the same value
    # Two pairs	- Two times two cards with the same value
    # Three of a kind - Three cards with the same value
    # Straight - Sequence of 5 cards in increasing value (Ace can precede 2 and follow up King)
    # Flush	- 5 cards of the same suit
    # Full house - Combination of three of a kind and a pair
    # Four of a kind - Four cards of the same value
    # Straight flush - Straight of the same suit
    # Royal flush - Straight flush from Ten to Ace
# Suits: Diamonds - D, Hearts - H, Spades - S, Clubs - C
# Ranks: Ace -A, King -K, Queen - Q, Jack - J, 10, 9, 8, 7, 6, 5, 4, 3, 2
# ranks: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 = 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A

from collections import namedtuple
Card = namedtuple("Card", ("suit", "rank"))

# Объявляем функцию возвращающую сортированный по rank список карт, попутно проверяя что suit & rank допустимые
def rank_func(cards):
    for card in cards:
        if card.suit not in ("D", "H", "S", "C"):
            raise RuntimeError(f"no such suit: {card.suit}")

        if card.rank not in (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14):
            raise RuntimeError(f"no such rank: {card.rank}")

    return sorted(cards, key=lambda card: card.rank)

import itertools

l = []
list(itertools.combinations(l, 5))

if __name__ == '__main__':
    card1 = Card(suit="D", rank=2)
    card2 = Card(suit="D", rank=3)
    card3 = Card(suit="H", rank=14)
    card4 = Card(suit="D", rank=2)
    card5 = Card(suit="D", rank=10)
    card6 = Card(suit="S", rank=6)
    card7 = Card(suit="C", rank=11)

    cards = [card1, card2, card3, card4, card5, card6, card7]
#   print(rank_func(cards))
    all_hands = list(itertools.combinations(cards, 5))
    all_hands = list(map(rank_func, all_hands))

for hand in all_hands:
    print(hand)


    #
    # best_combination, best_hand = None, None
    #
    # for hand in all_hands:
    #     combination = get_combination(hand) """описать get_combination"""
    #     if get_weight(combination) > get_weight(best_combination):
    #         best_combination = combination
    #         best_hand = hand


# hand_values = {1: 'Highcard', 2: 'Pair', 3: 'Two pairs', 4: 'Three of a kind', 5: 'Straight',
#               6: 'Flush', 7: 'Full house', 8: 'Four of a kind', 9: 'Straight flush', 10: 'Royal flush'}
