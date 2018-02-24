# -*- coding: utf-8 -*-
"""

https://codehiker.wordpress.com/2012/03/12/poker-hand-evaluation/


Created on Sat Feb 24 09:24:11 2018

https://codehiker.wordpress.com/2012/03/12/poker-hand-evaluation/

@author: Ben Brock and Shazia Zaman
"""

class Hand(object):
    def __init__(self,lst):
        self.cards=lst
        self.values, self.suits= self.setCards(lst)

    # extract values and suits information from cards
    def setCards(self, l):
        values=[]
        suits=[]
        for x in l:
            #print x
            suits.append(x[-1])
            if x[0]=='J':
                values.append(11)
            elif x[0]=='Q':
                values.append(12)
            elif x[0]=='K':
                values.append(13)
            elif x[0]=='A':
                values.append(14)
            else:
                values.append(int(x[:len(x)-1]))#in case of two digits line '10'
        return sorted(values),suits  #values need to be sorted

    def hasRoyalFlush(self): #1st
        hand=self.values
        return self.hasFlush() and self.hasStraight() and hand[0]==10
    def hasStraightFlush(self): #2nd
        hand=self.values
        return self.hasFlush() and self.hasStraight()
    def hasFourOfAKind(self):#3rd
        hand=self.values
        return ((hand[0]==hand[1] and hand[1]==hand[2] and hand[2]==hand[3] and hand[3]!=hand[4]) or
(hand[0]!=hand[1] and hand[1]==hand[2] and hand[2]==hand[3] and hand[3]==hand[4]))

    def hasFullHouse(self):#4th
        hand=self.values
        return ((hand[0]==hand[1] and hand[1]==hand[2] and hand[2]!=hand[3] and hand[3]==hand[4]) or
(hand[0]==hand[1] and hand[1]!=hand[2] and hand[2]==hand[3] and hand[3]==hand[4]))

    def hasFlush(self):#5th
        s=self.suits
        return s[0]==s[1] and s[1]==s[2] and s[2]==s[3] and s[3]==s[4]

    def hasStraight(self): #6nd
        for i in range(0,len(self.values)-2):
            if self.values[i]+1!=self.values[i+1]: return False
        return True

    def hasThreeOfAKind(self):#7th
        hand=self.values
        return ((hand[0]==hand[1] and hand[1]==hand[2] and hand[2]!=hand[3] and hand[3]!=hand[4])
or (hand[0]!=hand[1] and hand[1]==hand[2] and hand[2]==hand[3] and hand[3]!=hand[4]) or
(hand[0]!=hand[1] and hand[1]!=hand[2] and hand[2]==hand[3] and hand[3]==hand[4]))

    def hasTwoPairs(self):#8th
        hand=self.values
        return ((hand[0]==hand[1] and hand[1]!=hand[2] and hand[2]==hand[3] and hand[3]!=hand[4])
or (hand[0]==hand[1] and hand[1]!=hand[2] and hand[2]!=hand[3] and hand[3]==hand[4]) or
(hand[0]!=hand[1] and hand[1]==hand[2] and hand[2]!=hand[3] and hand[3]==hand[4]))

    def hasPair(self):#9th
        hand=self.values
        return ((hand[0]==hand[1] and hand[1]!=hand[2] and hand[2]!=hand[3] and hand[3]!=hand[4]) or
(hand[0]!=hand[1] and hand[1]==hand[2] and hand[2]!=hand[3] and hand[3]!=hand[4]) or
(hand[0]!=hand[1] and hand[1]!=hand[2] and hand[2]==hand[3] and hand[3]!=hand[4]) or
(hand[0]!=hand[1] and hand[1]!=hand[2] and hand[2]!=hand[3] and hand[3]==hand[4]))

    # in the getRank function, lower ranks will be masked by higher ranks
    def getRank(self):
        final='High Card' #10 the default
        if self.hasPair(): final='Pair!'
        if self.hasTwoPairs(): final='Two pairs!'
        if self.hasThreeOfAKind(): final='Three of a kind!'
        if self.hasStraight(): final='Straight'
        if self.hasFlush(): final='Flush'
        if self.hasFullHouse(): final='Full house!'
        if self.hasFourOfAKind(): final='Four of a kind!'
        if self.hasStraightFlush(): final="Straight Flush!"
        if self.hasRoyalFlush(): final="Royal Flush!"
        return final

# I created some tests according to your PDF file
c1= ['10s','Js','Qs','Ks','As']
c2=['4d','5d','6d','7d','8d']
c3=['Qs','Qd','Qc','Qh','10s']
c4=['Ks','Kd','3h','3s','3c']
c5=['Ad','Qd','6d','Jd','2d']
c6=['Ks','Qd','Jc','10h','9s']
c7=['5d','Js','8h','8s','8d']
c8=['10s','Qd','7s','Qc','7h']
c9=['10s','Jd','7s','6h','6s']
c10=['7c','6d','4s','3h','2c']
tests=[c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]
for x in tests:
    h=Hand(x)
    print h.cards,'-->', h.getRank()