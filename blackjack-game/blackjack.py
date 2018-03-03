'''
Blackjack Game (Python 3)
'''
import random

# Global constants
SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
RANKS = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
         'Ten', 'Jack', 'Queen', 'King', 'Ace')
VALUES = {
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5,
    'Six': 6,
    'Seven': 7,
    'Eight': 8,
    'Nine': 9,
    'Ten': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10,
    'Ace': 11
}


# Class Definitions
class Card:
    '''
    Represents a single card
    '''

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '{} of {}'.format(self.rank, self.suit)


class Deck:
    '''
    Represents a deck of cards
    '''

    def __init__(self):
        self.deck = []  # Start with an empty list
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))  # Append card objects

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += card.__str__() + '\n'
        return 'The deck has: {}'.format(deck_comp)

    def shuffle(self):
        '''Shuffle the deck'''
        random.shuffle(self.deck)  # Shuffle the list in place

    def deal(self):
        '''Deal'''
        return self.deck.pop()
