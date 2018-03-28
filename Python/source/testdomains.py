# -*- coding: utf-8 -*-

# test domain classes here

from domains import Deck
from PIL import Image
from PIL import ImageDraw

import os

workingDir = os.getcwd()
cardImageDir = workingDir + os.sep + "Images"
if not os.path.exists(cardImageDir):
    os.makedirs(cardImageDir)

selectedCardCanvas = Image.new("RGBA",[1100,800],(153,153,153,0))
selectCardDraw = ImageDraw.Draw(selectedCardCanvas)

def showCards(cardList):
    x=20
    y=20
    for i, card in enumerate(cardList,1):
        width,height = card.canvas.size
        selectedCardCanvas.paste(card.canvas,(x,y))
        x=x+width+20
        if i%10 is 0:
            x=20
            y=y+height+20
    selectedCardCanvas.save(cardImageDir + os.sep + "selectedCards.jpeg",format="JPEG")
       
print '************** Create Deck of Cards ****************'
deck = Deck()
print '************** Deck of Cards after shuffle *****************'
deck.shuffle()
print '************** Draw few cards *****************'
cardsList = [];
for i in range(0,5):
    cardsList.append(deck.deck.pop())
    
print '************** Cards drawn from deck *****************'
print 'Total cards drawn from deck: ', len(cardsList), 
print 'Check image file for selected cards'

showCards(cardsList)







            


