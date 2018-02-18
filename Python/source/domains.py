# -*- coding: utf-8 -*-

# Define Classes related to Poker game here

from colour import Color

card_suites = ['Spade','Diamond','Heart','Club']
card_values = [2,3,4,5,6,7,8,9,10,'Joker','Queen','King','Ace']
card_colors = [Color('red'),Color('black')]

class Card:
    def __init__(self, suite, color, value, priority):
        self.suite = suite
        self.color = color
        self.value = value
        self.priority = priority
    
    def __str__(self):
        return 'Suite: ' + str(self.suite) + ' | color: ' + str(self.color) + ' | value: ' + str(self.value) + ' | priority: ' + str(self.priority)

class Deck:
    def __init__(self):
        self.deck = []
        for color in card_colors:
            for suite in card_suites:
                priority = 0
                for value in card_values:
                    card = Card(suite, color, value, priority)
                    priority += 1
                    self.deck.append(card)
    
    def show(self):
        for card in self.deck:
            print (str(card))
            
    def shuffle(self):
        print ('Shuffle functionality is not implemented yet')
    
            
