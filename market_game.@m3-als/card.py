# card.py
from dataclasses import dataclass


@dataclass
class Card:
    rank: str
    suit: str

    def __str__(self):
        return f"{self.rank}{self.suit}"

    @property
    def get_rank(self):
        return self.rank

def create_card(rank: str, suit: str) -> Card:
    return Card(rank, suit)
