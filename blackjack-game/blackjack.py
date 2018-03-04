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

PLAYING = True


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


class Hand:
    '''
    Represents what cards are currently in someone's hand
    '''

    def __init__(self):
        self.cards = []  # Start with an empty list
        self.value = 0
        self.aces = 0  # Attribute to kepp track of Aces

    def add_card(self, card):
        '''Add a card (from Deck.deal())'''
        self.cards.append(card)
        self.value += VALUES[card.rank]

        # Track Aces
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        '''Adjust for the Ace'''
        # If total value > 21, adjust the value
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:
    '''
    Represents player's starting chips, bets and ongoing winnings
    '''

    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        '''Player wins the bet'''
        self.total += self.bet

    def lose_bet(self):
        '''Player loses the bet'''
        self.total -= self.bet


# Helper Functions
def take_bet(chips):
    '''Ask the player to make a bet'''
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except:
            print('Sorry, please provide an integer!')
        else:
            if chips.bet > chips.total:
                print(
                    'Sorry, yoou do not have enough chips! You have {} chips'.
                    format(chips.total))
            else:
                break


def hit(deck, hand):
    '''Requesting a hit'''
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    '''Prompt the player to Hit or Stand'''
    global PLAYING

    while True:
        choice = input('Hit or Stand? Enter h or s: ')

        if choice[0].lower() == 'h':
            hit(deck, hand)
        elif choice[0].lower() == 's':
            print('Player Stands, Dealer\'s Turn')
            PLAYING = False
        else:
            print('Sorry, Didn\'t understand that, Please enter h or s only!')
            continue
        break


def player_busts(chips):
    '''Player Busts'''
    print('BUST PLAYER!')
    chips.lose_bet()


def player_wins(chips):
    '''Player Wins'''
    print('PLAYER WINS!')
    chips.win_bet()


def dealer_busts(chips):
    '''Dealer Busts'''
    print('PLAYER WINS! DEALER BUSTED!')
    chips.win_bet()


def dealer_wins(chips):
    '''Dealer Wins'''
    print('DEALER WINS!')
    chips.lose_bet()


def push():
    '''Player & Dealer Tie'''
    print('Dealer and player tie! PUSH')


def show_some(player, dealer):
    '''Each time player takes a card, dealer's first card is hidden and
    all of Player's card are vsible!'''
    print('DEALERS HAND:\nOne Card Hidden!\n{}\n\nPLAYERS HAND:'.format(
        dealer.cards[1]))
    print('\n'.join([str(card) for card in player.cards]))


def show_all(player, dealer):
    '''At the end of the hand, all cars are shown!'''
    print('DEALERS HAND:')
    print('\n'.join([str(card) for card in dealer.cards]))
    print('\nPLAYERS HAND:')
    print('\n'.join([str(card) for card in player.cards]))


# Start the game
while True:
    # Opening statement
    print('WELCOME TO BALCKJACK')

    # Create and shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Setup Player's chips
    player_chips = Chips()  # Default is 100

    # Prompt the player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while PLAYING:
        # Prompt for player to Hit or Stand
        hit_or_stand(deck, player_hand)

        # Show card (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_chips)
            break

        # If player hasn't busted, play dealer's hand unitl dealer reaches 17
        # Soft 17 Rule
        if player_hand.value <= 21:
            while dealer_hand.value < player_hand.value:
                hit(deck, dealer_hand)

        # Show all cards
        show_all(player_hand, dealer_hand)

        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_chips)
        else:
            push()

    # Inform the player of their total chips
    print('\nPlayer\'s total chips are at {}'.format(player_chips.total))

    # Ask to play again
    new_game = input('Would you like to play another hand? Y/N: ')
    if new_game.lower() == 'y':
        PLAYING = True
    else:
        print('Thank you for playing BlackJack!')
        break