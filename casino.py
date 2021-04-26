import random


class Card():
    """Simulate a single card with rank, value and suit."""

    def __init__(self, rank, value, suit):
        """Intialize card attributes"""
        self.rank = rank
        self.value = value
        self.suit = suit

    def dispaly_card(self):
        print(self.rank + " of " + self.suit)


class Deck():
    """Simulate a deck of 52 indivitual playing cards."""

    def __init__(self):
        """A list to hold all future cards in the deck"""
        self.cards = []

    def build_deck(self):
        """Build a deck constituting of 52 unique cards."""
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        ranks = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                 '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11, }

        for suit in suits:
            for rank, value in ranks.items():
                card = Card(rank, value, suit)
                self.cards.append(card)

      def shuffle_deck(self):
        """Shuffle a deck of cards"""
        random.shuffle(self.cards)

      def deal_card(self):
        """Remove a card from the deck to be dealt"""
        
        card = self.cards.pop()
        return card
