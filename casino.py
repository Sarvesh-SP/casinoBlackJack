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

class Player():
  """A Class for the user to play Black Jack"""

  def __init__(self):
    """Initialize the player"""
    self.hand = []
    self.hand_value = 0
    self.playing_hand = True

  def draw_hand(self, deck):
    """Deal the player starting hand"""
    for x in range(2):
      card = deck.deal_card()
      self.hand.append(card)
  
  def dispaly_hand(self):
    """show the player's hand"""
    print("\nPlayer's Hand: ")
    for card in self.hand:
      card.dispaly_card()

  
  def hit(self, deck):
    """Give the player a new card"""
    card = deck.deal_card()
    self.hand.append(card)

  def get_hand_value(self):
    """Compute the value of the player hand."""
    self.hand_value = 0

    ace_in_hand = False
    for card in self.hand:
      self.hand_value += card.value

      if card.rank == 'A':
        ace_in_hand = True
      
    if self.hand_value > 21 and ace_in_hand:
      self.hand_value -= 10
    print(f"Total value: {self.hand_value}")


  def update_hand(self, deck):
    """Update the players hand by allowing them to hit"""
    if self.hand_value < 21:
      choice = input("Would you like to hit(y/n): ").lower()
      if (choice == 'y'):
        self.hit(deck)
      else:
        self.playing_hand = False
    else:
      self.playing_hand = False
    

  
  
