import random

'''
https://www.youtube.com/watch?v=t8YkjDH86Y4
'''

class Card(object):

	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def show(self):
		print "{} of {}".format(self.value, self.suit)


class Deck(object):
    
	def __init__(self):
		self.cards = []
		self.build()

	def build(self):

		for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:
			for value in "A23456789TJQK":
				self.cards.append(Card(suit, value))

	def show(self):
		for c in self.cards:
			c.show()

	def shuffle(self):
        
		for i in range(len(self.cards)-1, 0, -1):
			r = random.randint(0, i)
			self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

	def drawCard(self):
    
		return self.cards.pop()
    
	def get_deck_size(self):
		return len(self.cards)



class Player(object):
	def __init__(self, name):
		self.name = name
		self.hand = []

	def draw(self, deck):
		self.hand.append(deck.drawCard())
		return self

	def showHand(self):
		for card in self.hand:
			card.show()

	def discard(self):
		return self.hand.pop()



#card = Card("Clubs", 6)
#card.show()

deck = Deck()
deck.shuffle()
print deck.get_deck_size()
#deck.show()

#card = deck.drawCard()
#card.show()

bob = Player("bob")
bob.draw(deck).draw(deck)
bob.showHand()


print deck.get_deck_size()