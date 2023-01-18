
# Create a deck of cards class. Internally, the deck of cards should use another class, a card class. Your requirements are:
#
# The Deck class should have a deal method to deal a single card from the deck
# After a card is dealt, it is removed from the deck.
# There should be a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)



from random import shuffle

class Card:

    # Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    #  __repr__() function returns the object representation in string format.
    #  This method is called when repr() function is invoked on the object
    def __repr__(self):
        return "(%s,%s)" % (self.value, self.suit)
class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

        # creating the object of Cards class and initialized the suits and values
        self.cards = [Card(suit, value) for suit in suits for value in values]
        for i in self.cards:
            print(i)

    def __repr__(self):
        return "Cards remaining in deck: {}".format(len(self.cards))

    # shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
    def shuffle(self):
        if len(self.cards) == 52:
            shuffle(self.cards)   # importing the shuffle() from random module
            return self.cards
        else:
            return ("Only full decks can be shuffled...!")

    # Single card is dealt, it is removed from the deck using pop()
    def deal(self):
        if len(self.cards) != 0:
            return self.cards.pop()
        else:
            return ("All cards have been removed..!")


deck = Deck()
print("Deck created...!")

print("\n \nShuffling the Deck of cards..!")
x = deck.shuffle()  # Calling the shuffle()
for i in x:
    print(i)
a = int(input("\n \nEnter 1 to deal the cards : "))

while (a == 1):
    # The Deck class should have a deal method to deal a single card from the deck.
    print(deck.deal())
    print(deck)
    a = int(input("Enter 1 to deal the cards (or) any key to discontinue : "))
print(deck.shuffle())