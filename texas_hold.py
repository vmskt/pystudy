""" Написать функцию, которая берёт на вход набор карт (строго говоря, 7 карт, но на самом деле, это не важно)
и возвращает старшую пятикарточную комбинацию в этом наборе.
Hand values:
    * Highcard - Simple value of the card. Lowest: 2 – Highest: Ace (King in example)
    * Pair - Two cards with the same value
    * Two pairs	- Two times two cards with the same value
    * Three of a kind - Three cards with the same value
    * Straight - Sequence of 5 cards in increasing value
    * Flush	- 5 cards of the same suit
    * Full house - Combination of three of a kind and a pair
    * Four of a kind - Four cards of the same value
    * Straight flush - Straight of the same suit
    * Royal flush - Straight flush from Ten to Ace
Suits: Diamonds - D, Hearts - H, Spades - S, Clubs - C
Ranks: Ace -A, King -K, Queen - Q, Jack - J, 10, 9, 8, 7, 6, 5, 4, 3, 2
ranks: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 = 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A """

import itertools
from collections import namedtuple
from collections import Counter
from typing import List

Card = namedtuple(typename="Card", field_names=("suit", "rank"))


# Объявляем функцию возвращающую сортированный по рангу (rank) список карт, проверяя что suit & rank допустимые
def rank_func(cards):
    for card in cards:
        if card.suit not in ("D", "H", "S", "C"):
            raise RuntimeError(f"no such suit: {card.suit}")

        if card.rank not in (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14):
            raise RuntimeError(f"no such rank: {card.rank}")

    return sorted(cards, key=lambda card: card.rank)  # ascending sort by rank


def count_ranks(hand):  # count length of unique ranks in hand
    return len(set(card.rank for card in hand))


def check_ranks_unique(hand):  # checking that all ranks in hand are unique
    return count_ranks(hand) == 5


def check_flush(hand: List[Card]):
    if len(set(card.suit for card in hand)) == 1:  # If sum of all suits in hand = 1, then all suit is equal
        return hand[-1].rank  # return the rank of highest card in hand


def check_straight(hand: List[Card]):
    if check_ranks_unique(hand):  # checking for the uniqueness of the suit
        if hand[-1].rank - hand[0].rank == 4:  # difference between high and low cards of the same suit
            return hand[-1].rank


def check_straight_flush(hand: List[Card]):
    if check_ranks_unique(hand):
        if len(set(card.suit for card in hand)) == 1 and hand[-1].rank - hand[0].rank == 4:
            return hand[-1].rank


def check_royal_flush(hand: List[Card]):
    if check_straight_flush(hand):
        if hand[-1].rank == 14:
            return hand[-1].rank


def check_pair(hand: List[Card]):
    ranks = [card.rank for card in hand]
    if count_ranks(hand) == 4 and Counter(ranks).most_common(1)[0][1] == 2:
        return Counter(ranks).most_common()[0][0]


def check_two_pair(hand: List[Card]):
    ranks = [card.rank for card in hand]
    if count_ranks(hand) == 3 and Counter(ranks).most_common(2)[1][1] == 2:
        return Counter(ranks).most_common(2)[1][0]


def check_three(hand: List[Card]):
    ranks = [card.rank for card in hand]
    if count_ranks(hand) == 3 and Counter(ranks).most_common(1)[0][1] == 3:
        return Counter(ranks).most_common()[0][0]


def check_four(hand: List[Card]):
    ranks = [card.rank for card in hand]
    if count_ranks(hand) == 2 and Counter(ranks).most_common(1)[0][1] == 4:
        return Counter(ranks).most_common()[0][0]


def check_full_house(hand: List[Card]):
    ranks = [card.rank for card in hand]
    if count_ranks(hand) == 2 and Counter(ranks).most_common(1)[0][1] == 3:
        return Counter(ranks).most_common()[0][0]


def check_highcard(hand: List[Card]):
    if count_ranks(hand) == 5 and not check_flush(hand):
        return hand[-1].rank


if __name__ == '__main__':

    card1 = Card(suit="H", rank=2)
    card2 = Card(suit="D", rank=3)
    card3 = Card(suit="S", rank=4)
    card4 = Card(suit="D", rank=7)
    card5 = Card(suit="D", rank=9)
    card6 = Card(suit="D", rank=11)
    card7 = Card(suit="C", rank=14)

    cards = [card1, card2, card3, card4, card5, card6, card7]
    all_hands = list(itertools.combinations(cards, 5))
    sorted_all_hands = list(map(rank_func, all_hands))
#
#
for hand in sorted_all_hands:
    print(hand)
ranks = [card.rank for card in hand]
    # print(ranks)
    print(Counter(ranks).most_common())
    # print('Check Flush', ', ', 'Highest card =', check_flush(hand))
    # print('Check Straight', ', ', 'Highest card =', check_straight(hand))
    # print('Check Straight flush', ', ', 'Highest card =', check_straight_flush(hand))
    # print('Check Royal flush', ', ', 'Highest card =', check_royal_flush(hand))
    # print('Check Pair', ', ', 'Highest card =', check_pair([card.rank for card in hand]))
    # print('Check Pair', ', ', 'Highest card =', check_pair(hand))
    # print('Check Two Pair', ', ', 'Highest card =', check_two_pair(hand))
    # print('Check Three of a kind', ', ', 'Highest card =', check_three(hand))
    # print('Check Full House', ', ', 'Highest card =', check_full_house(hand))
    # print('Check Four of a kind', ', ', 'Highest card =', check_four(hand))
    print('Check Highcard', ', ', 'Highest card =', check_highcard(hand))

