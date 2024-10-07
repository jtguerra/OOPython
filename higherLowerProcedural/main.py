# Higher or Lower
# a card game about predicting if a face down card is higher or lower than another card
# this game is a learning exercise found in the book Object-Oriented Python by Irv Kalb


import random

SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

NCARDS = 8


# pass in a deck and the function returns a random card from the deck
def getCard(deckIn):
    card = deckIn.pop()
    return card


# pass in a deck and the function returns a shuffled copy of the deck
def shuffle(deck):
    shuffledDeck = deck.copy()
    random.shuffle(shuffledDeck)
    return shuffledDeck


# build deck
newDeck = []
for suit in SUIT_TUPLE:
    for value, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank':rank, 'suit':suit, 'value':value +1}
        newDeck.append(cardDict)

