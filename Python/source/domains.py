# -*- coding: utf-8 -*-

# Define Classes related to Poker game here

from random import shuffle

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

import os

workingDir = os.getcwd()
cardImageDir = workingDir + os.sep + "Images"
if not os.path.exists(cardImageDir):
    os.makedirs(cardImageDir)

card_suits = ['Spade','Diamond','Club','Heart']
card_values = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
card_colors = ["#000000","#FF0000","#000000","#FF0000"]
card_priority = {'Ace':1,'King':2,'Queen':3,'Joker':4}
card_shapes = [u'\u2666', u'\u2663', u'\u2660', u'\u2665']

#set the path correctly to get true type font file
arialFont = ImageFont.truetype("fonts/arial.ttf", 20)

canvas = Image.new("RGBA",[1100,800],(153,153,153,0))
draw = ImageDraw.Draw(canvas)

class Card:
    def __init__(self, suite, color, value, priority,shape):
        self.suit = suite
        self.color = color
        self.value = value
        self.priority = priority
        self.shape = shape
        self.textDim = arialFont.getsize(str(self.value))
        self.canvas=Image.new("RGBA",[self.textDim[0]+70,self.textDim[1]+70],(245,245,220))
        self.cardWidth, self.cardHeight = self.canvas.size
        self.drawImage = ImageDraw.Draw(self.canvas)
        self.drawImage.text((5,5),str(self.value),font=arialFont,fill=color)
        self.drawImage.text((self.cardWidth/2 -5,self.cardHeight/2 -5),self.shape,font=arialFont,fill=color)
        self.drawImage.text((self.cardWidth-25,self.cardHeight-25),str(self.value),font=arialFont,fill=color,anchor=180)
    
    def __str__(self):
        return 'Suite: ' + str(self.suit) + ' | color: ' + str(self.color) + ' | value: ' + str(self.value) + ' | priority: ' + str(self.priority)
    
class Deck:
    def __init__(self):
        self.deck = []
        for i, suit in enumerate(card_suits):
            for value in card_values:
                priority = card_priority.get(value)
                if priority is None:
                    priority = 999
                color = card_colors[i]
                card = Card(suit, color, value, priority, card_shapes[i])
                self.deck.append(card)
    
    def __str__(self):
        deckString = ""
        for card in self.deck:
            deckString += str(card) + '\n'
        return deckString
    
    def show(self):
        x=20
        y=20
        for i, card in enumerate(self.deck,1):
            width,height = card.canvas.size
            canvas.paste(card.canvas,(x,y))
            x=x+width+20
            if i%10 is 0:
                x=20
                y=y+height+20
        canvas.save(cardImageDir + os.sep + "deck.jpeg",format="JPEG")
        #having issue to load and show image that has been saved
        #im = Image.open(cardImageDir + os.sep + r"deck.jpeg")
        #im.show()
                    
    def shuffle(self):
        for i in range(0,5):
            shuffle(self.deck)
    
            
