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

    '''
    Royal Flush
    A, K, Q, J, 10 all of the same suit.
    
    An ace-high straight flush, such as A♦ K♦ Q♦ J♦ 10♦, is commonly known as a 
    royal flush or royal straight flush and is the best possible hand in high 
    games when not using wild cards.
    
    POKER HAND RANKINGS:  1
    
    Example:  As, Ks, Qs, Js, 10s
    
    Note:
    cards are in two digits
    1st digit - encoded card value  or encoded rank
    2nd digit - suit
    '''
    def hasRoyalFlush(self): #1st
        hand=self.values
        return self.hasFlush() and self.hasStraight() and hand[0]==10
    
    '''
    Straight Flush
    Any five card sequence in the same suit.
    
    A straight flush is a poker hand containing five cards of sequential rank, 
    all of the same suit, such as Q♥ J♥ 10♥ 9♥ 8♥ (a "queen-high straight flush").
    
    POKER HAND RANKINGS:  2
    
    Example: 4d, 5d, 6d, 7d, 8d
    
    Note:
    cards are in two digits
    1st digit - encoded card value  or encoded rank
    2nd digit - suit
    '''
    def hasStraightFlush(self): #2nd
        hand=self.values
        return self.hasFlush() and self.hasStraight()
    
    '''
    Four of a Kind
    All four cards of the same rank.
    
    Four of a kind, also known as quads, is a poker hand containing four cards of 
    the same rank and one card of another rank, such as:
    9c, 9s, 9d, 9h, Jh ("four of kind, nines").
    
    Rank is card value or encoded value
    POKER HAND RANKINGS:  3
    
    Example:  Qs, Qd, Qc, Qh, 3c
    
    Note:
    cards are in two digits
    1st digit - encoded card value  or encoded rank 
    2nd digit - suit
    '''
    def hasFourOfAKind(self):#3rd
        hand=self.values
        return ((hand[0]==hand[1] and hand[1]==hand[2] and hand[2]==hand[3] and hand[3]!=hand[4]) or
(hand[0]!=hand[1] and hand[1]==hand[2] and hand[2]==hand[3] and hand[3]==hand[4]))

    '''
    Full House
    Three of a kind combined with a pair.
    
    A full house, also known as a full boat or tight, is a poker hand containing 
    three cards of one rank and two cards of another rank, such as 3♣ 3♠ 3♦ 6♣ 6♥ 
    (a "full house, threes over sixes" or "threes full of sixes" or "threes full")
    
    POKER HAND RANKINGS:  4
    
    Example:  Kh, Kd, 3h, 3s, 3c
    
    Note:
    cards are in two digits
    1st digit - encoded card value  or encoded rank 
    2nd digit - suit
    '''
    def hasFullHouse(self):#4th
        hand=self.values
        return ((hand[0]==hand[1] and hand[1]==hand[2] and hand[2]!=hand[3] and hand[3]==hand[4]) or
(hand[0]==hand[1] and hand[1]!=hand[2] and hand[2]==hand[3] and hand[3]==hand[4]))

    '''
    Flush
    Any five cards of the same suit but not in the same sequence
    
    A flush is a poker hand containing five cards all of the same suit, not all of
    sequential rank, such as K♣ 10♣ 7♣ 6♣ 4♣ (a "king-high flush" or
    "king-ten-high flush").
    
    POKER HAND RANKINGS:  5
    
    Example:  Ad, Qd, 6d, Jd, 2d
    
    Note:
    cards are in two digits
    1st digit - encoded card value  or encoded rank 
    2nd digit - suit
    '''
    def hasFlush(self):#5th
        s=self.suits
        return s[0]==s[1] and s[1]==s[2] and s[2]==s[3] and s[3]==s[4]

    '''
    Straight
    Five cards in sequence, but not in the same suit.
    
    A straight is a poker hand containing five cards of sequential rank, not all 
    of the same suit, such as 7♣ 6♠ 5♠ 4♥ 3♥ (a "seven-high straight")
    
    POKER HAND RANKINGS:  6
    
    Example:  Ks, Qd, Jc, 10h, 9s
    
    Note:
    cards are in two digits
    1st digit - encoded card value  or encoded rank 
    2nd digit - suit
    '''
    def hasStraight(self): #6nd
        for i in range(0,len(self.values)-2):
            if self.values[i]+1!=self.values[i+1]: return False
        return True

    '''
    Three of a Kind
    Three cards of the same rank.
    
    Three of a kind, also known as trips or a set, is a poker hand containing 
    three cards of the same rank and two cards of two other ranks (the kickers), 
    such as 2♦ 2♠ 2♣ K♠ 6♥ ("three of a kind, twos" or "trip twos" or a 
    "set of twos").
    
    POKER HAND RANKINGS:  7
    
    Example:  5d, Js, 8h, 8s, 8d
    
    Note:
    cards are in two digits
    1st digit - encoded card value  or encoded rank 
    2nd digit - suit
    '''
    def hasThreeOfAKind(self):#7th
        hand=self.values
        return ((hand[0]==hand[1] and hand[1]==hand[2] and hand[2]!=hand[3] and hand[3]!=hand[4])
or (hand[0]!=hand[1] and hand[1]==hand[2] and hand[2]==hand[3] and hand[3]!=hand[4]) or
(hand[0]!=hand[1] and hand[1]!=hand[2] and hand[2]==hand[3] and hand[3]==hand[4]))

    '''
    Two Pair
    Two separate pairs.
    
    Two pair is a poker hand containing two cards of the same rank, two cards of 
    another rank and one card of a third rank (the kicker),
    
    such as J♥ J♣ 4♣ 4♠ 9♥ 
    
    ("two pair, jacks and fours" or "two pair, jacks over fours" or "jacks up").
    
    POKER HAND RANKINGS:  8
    
    Example:  10s, Qd, 7s, Qc, 7h
    
    Note:
    cards are in two digits
    1st digit - encoded card value  or encoded rank 
    2nd digit - suit
    '''
    def hasTwoPairs(self):#8th
        hand=self.values
        return ((hand[0]==hand[1] and hand[1]!=hand[2] and hand[2]==hand[3] and hand[3]!=hand[4])
or (hand[0]==hand[1] and hand[1]!=hand[2] and hand[2]!=hand[3] and hand[3]==hand[4]) or
(hand[0]!=hand[1] and hand[1]==hand[2] and hand[2]!=hand[3] and hand[3]==hand[4]))

    '''
    One Pair
    Two cars of the same rank.
    
    One pair, or simply a pair, is a poker hand containing two cards of the same 
    rank and three cards of three other ranks (the kickers), 
    
    such as 4♥ 4♠ K♠ 10♦ 5♠ 
    
    ("one pair, fours" or a "pair of fours").
    
    POKER HAND RANKINGS:  9
    
    Example:  10s, Jd, 7s, 6h, 6c
    
    Note:
    cards are in two digits
    1st digit - encoded card value  or encoded rank 
    2nd digit - suit
    '''
    def hasPair(self):#9th
        hand=self.values
        return ((hand[0]==hand[1] and hand[1]!=hand[2] and hand[2]!=hand[3] and hand[3]!=hand[4]) or
(hand[0]!=hand[1] and hand[1]==hand[2] and hand[2]!=hand[3] and hand[3]!=hand[4]) or
(hand[0]!=hand[1] and hand[1]!=hand[2] and hand[2]==hand[3] and hand[3]!=hand[4]) or
(hand[0]!=hand[1] and hand[1]!=hand[2] and hand[2]!=hand[3] and hand[3]==hand[4]))



    '''
    High Card
    Othewise unrelated cards ranked by the highest single card.
    
    High card, also known as no pair or simply nothing, is a poker hand containing
    five cards not all of sequential rank or of the same suit, and none of which 
    are of the same rank, 
    
    such as K♥ J♥ 8♣ 7♦ 4♠ 
    
    ("high card, king" or "king-jack-high" or "king-high").
    
    POKER HAND RANKINGS:  10
    
    Example:  7c, 6d, 4s, 3h, 2c
    
    DOES NOT SUPPORT HIGH CARD!!!!
    
    Note:
    cards are in two digits
    1st digit - encoded card value  or encoded rank 
    2nd digit - suit
    '''
    def highcard(hand):
        pass

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
c1= ['10s','Js','Qs','Ks','As']   # --> Royal Flush!
c2=['4d','5d','6d','7d','8d']     # --> Straight Flush!
c3=['Qs','Qd','Qc','Qh','10s']    # --> Four of a kind!
c4=['Ks','Kd','3h','3s','3c']     # --> Full house!
c5=['Ad','Qd','6d','Jd','2d']     # --> Flush
c6=['Ks','Qd','Jc','10h','9s']
c7=['5d','Js','8h','8s','8d']
c8=['10s','Qd','7s','Qc','7h']
c9=['10s','Jd','7s','6h','6s']
c10=['7c','6d','4s','3h','2c']
c11=['2h', '2d', '2c', 'Kc', 'Qd']      # three of a kind  beginning
c12=['2h', '5h', '7d', '8c', '9s']      # high card
c13=['Ah', '2d', '3c', '4c', '5d']      # straight
c14=['2h', '3h', '2d', '3c', '2d']      # full house
c15=['2h', '7h', '2d', '3c', '3d']      # two pair
c16 =['2h','7h', '7d', '7c', '7s']      # four of a kind
c17=['9h', '10h', 'Jh', 'Qh', 'Kh']     # straigh flush 
c18=['4h', '4s', 'Ks', '5d', '10s']     # one pair
c19=['Qc', '10c', '7c', '6c', '4c']     # flush          end
c20 = ['As', 'Ac', 'Ah', 'Ad', '2c']     # four of a kind 
c21 = ['Jc', '10c', '9c', '8c', '7c']    # straight flush
c22 = ['5c', '5d', '5h', '5s', '2d']     # four of a kind
c23 = ['6s', '6h', '6d', 'Kc', 'Kh']     # full house
c24 = ['Jd', '9d','8d', '4d', '3d']      # flush
c25 = ['10d', '9s', '8h', '7d', '6c' ]   # straight
c26 = ['Qc', 'Qs', 'Qh', '9h', '2s']     # three of a kind 
c27 = ['Jh', 'Jc', '3c', '3s', '2h']    # two pair
c28 = ['10c', '10h', '8s', '7h', '4c']   # one pair
c29 = ['Kd', 'Qd', '7s', '4s', '2h']     # high card

tests=[c1,c2,c3,c4,c5,
       c6,c7,c8,c9,c10, 
       c11, c12, c13, c14, c15, 
       c16, c17, c18, c19,
       c20, c21, c22, c23,
       c24, c25, c26, c27,
       c28, c29, c27]

for x in tests:
    h=Hand(x)
    print h.cards,'-->', h.getRank()