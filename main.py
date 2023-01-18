
# Write a Program DeckOfCards.java, to initialize deck of cards having suit ("Clubs", "Diamonds", "Hearts", "Spades")
# & Rank ("2", "3", "4", "5", "6", "7", "8","9", "10", "J", "Q", "K", "A"). Shuffle the cards using Random
# method and then distribute 9 Cards to 4 Players and Print the Cards received by the 4 Players.


import itertools
import random

class DeckofCards:

	def __init__(self):
		self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
		self.values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

	def distributeCards(self,no_players,cards_distribute):

		# Creating deck of 52 cards
		deck_cards = list(itertools.product(self.values, self.suits))
		print("Before Shuffle : \n", deck_cards)

		# Shuffling the deck of 52 cards.
		random.shuffle(deck_cards)
		print("After Shuffle : \n", deck_cards)

		for i in range(no_players):
			print("\nPlayer No.: ", i+1)
			for j in range(cards_distribute):
				print (deck_cards[j][0], "of", deck_cards[j][1], ",", end=" "),
				deck_cards.pop(j)

# Constructor to initialize the suits and values .
deck = DeckofCards()

# Input the values from user the numbers of players and cards have to distribute.
no_players =int(input("Enter the numbers of Player : "))
cards_distribute = int(input("Enter the numbers cards want to distributes : "))

# Calling the distributeCards() method from the Deck class for distribution of cards.
deck.distributeCards(no_players, cards_distribute)


