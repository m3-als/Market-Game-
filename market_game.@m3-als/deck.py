# deck.py
import random
from typing import List
from card import create_card, Card


class Deck:
    suits = ['♥', '♦', '♣', '♠']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self):
        self.cards = [create_card(rank, suit)  for suit in self.suits for rank in self.ranks]

    def shuffle(self):
        for _ in range(3):
            random.shuffle(self.cards)

    def draw(self) -> Card:
        return self.cards.pop() if self.cards else None
