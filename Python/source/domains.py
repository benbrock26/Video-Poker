# -*- coding: utf-8 -*-

# Define Classes related to Poker game here

from colour import Color
from random import shuffle

card_suits = ['Spade','Diamond','Heart','Club']
card_values = [2,3,4,5,6,7,8,9,10,'Joker','Queen','King','Ace']
card_colors = [Color('red'),Color('black')]
card_priority = {'Ace':1,'King':2,'Queen':3,'Joker':4}

class Card:
    def __init__(self, suite, color, value, priority):
        self.suit = suite
        self.color = color
        self.value = value
        self.priority = priority
    
    def __str__(self):
        return 'Suite: ' + str(self.suit) + ' | color: ' + str(self.color) + ' | value: ' + str(self.value) + ' | priority: ' + str(self.priority)

class Deck:
    def __init__(self):
        self.deck = []
        for color in card_colors:
            for suit in card_suits:
                for value in card_values:
                    priority = card_priority.get(value)
                    if priority is None:
                        priority = 999
                    card = Card(suit, color, value, priority)
                    self.deck.append(card)
    
    def show(self):
        for card in self.deck:
            print (str(card))
            
    def shuffle(self):
        for i in range(0,5):
            shuffle(self.deck)
    
            
