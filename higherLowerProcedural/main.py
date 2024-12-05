# Higher or Lower
# a card game about predicting if a face down card is higher or lower than another card
# this game is a learning exercise found in the book Object-Oriented Python by Irv Kalb


import random

SUITS = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANKS = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

ROUNDS = 8


# pass in a deck and the function returns a random card from the deck
def getCard(deckIn):
    card = deckIn.pop()
    return card


# pass in a deck and the function returns a shuffled copy of the deck
def shuffle(deck):
    shuffledDeck = deck.copy()
    random.shuffle(shuffledDeck)
    return shuffledDeck


print("Welcome to Higher or Lower")
print("You have to choose whether the next card will be higher or lower than the shown card.")
print("Get it right awards 20 points; get it wrong and lose 15 points.")
print("You start with 50 points.")
print()

# build deck
newDeck = []
for suit in SUITS:
    for value, rank in enumerate(RANKS):
        cardDict = {'rank': rank, 'suit': suit, 'value': value + 1}
        newDeck.append(cardDict)

score = 50

while True: # the game loop
    print()
    gameDeck = shuffle(newDeck)
    currentCard = getCard(gameDeck)
    cardRank = currentCard['rank']
    cardValue = currentCard['value']
    cardSuit = currentCard['suit']
    print("Starting card is:", cardRank, 'of', cardSuit)
    print()

    for c in range(0, ROUNDS):      # how many cards per game
        answer = ""
        while answer != 'h' and answer != 'l':       # some input validation
            answer = input("Will the next card be higher, or lower than the " +
                           cardRank + ' of ' + cardSuit + " ? please enter 'h' or 'l': ")
            answer = answer.casefold()  # change input to lowercase

        nextCard = getCard(gameDeck)
        nextRank = nextCard['rank']
        nextSuit = nextCard['suit']
        nextValue = nextCard['value']

        print("The next card is:", nextRank + " of " + nextSuit)

        if answer == 'h':       # player chose higher
            if nextValue > cardValue:
                print("Correct! The next card was higher!")
                score += 20
            else:
                print("The next card was NOT higher. Better luck next time...")
                score -= 15

        elif answer == 'l':     # player chose lower
            if nextValue < cardValue:
                print("Correct! The next card was lower!")
                score += 20
            else:
                print("The next card was NOT lower. Better luck next time...")
                score -= 15

        print("Your score is:", score)
        print()

        cardRank = nextRank
        cardSuit = nextSuit
        cardValue = nextValue