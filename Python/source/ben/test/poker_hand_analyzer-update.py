# -*- coding: utf-8 -*-
"""

https://rosettacode.org/wiki/Poker_hand_analyser#Python

https://en.wikipedia.org/wiki/List_of_poker_hands

https://en.wikipedia.org/wiki/List_of_poker_hands

Created on Sat Feb 24 08:33:29 2018

@author: Ben Brock and Shazia Zaman
"""

from collections import namedtuple
import sys

debug = 0
 
class Card(namedtuple('Card', 'face, suit')):
    def __repr__(self):
        return ''.join(self)
 
 
suit = 'h d c s'.split()
# ordered strings of faces
faces   = '2 3 4 5 6 7 8 9 10 j q k a'
lowaces = 'a 2 3 4 5 6 7 8 9 10 j q k'
# faces as lists
face   = faces.split()
lowace = lowaces.split()
 

'''
Royal Flush
A, K, Q, J, 10 all of the same suit.

An ace-high straight flush, such as A♦ K♦ Q♦ J♦ 10♦, is commonly known as a 
royal flush or royal straight flush and is the best possible hand in high 
games when not using wild cards.

POKER HAND RANKINGS:  1

Tie breaker rules
https://www.adda52.com/poker/poker-rules/cash-game-rules/tie-breaker-rules

Example:  As, Ks, Qs, Js, 10s

DOES NOT SUPPORT ROYAL FLUSH

Note:
cards are in two digits
1st digit - encoded card value  or encoded rank
2nd digit - suit
'''
def royal_flush(hand):
    allfaces = [f for f,s in hand]
    allftypes = set(allfaces)
    
    all_suits = [s for f, s in hand]
    all_stypes = len(set(all_suits))
    
    #print "ROYAL FLUSH: HAND:\t{}".format(hand)
    values, suit = set_Cards(hand)

    if all_stypes == 1 and sum(values) == 60:
        #print "\nROYAL FLUSH: ALL FACES:\t{}".format(allfaces)
        #print "ROYAL FLUSH: ALL FTYPES:\t{}".format(allftypes)
        #print "\nROYAL FLUSH: ALL SUITS:\t{}".format(all_suits)
        #print "ROYAL FLUSH: ALL SUIT TYPES:\t{}".format(all_stypes)
        #print "ROYAL FLUSH SUM is:\t{}".format(sum(values))
        return 'royal-flush', "No Tie breaker, if 2 players have RF split the pot"
    else:
        return False
 

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
def straightflush(hand):
    f,fs = ( (lowace, lowaces) if any(card.face == '2' for card in hand)
             else (face, faces) )
    ordered = sorted(hand, key=lambda card: (f.index(card.face), card.suit))
    first, rest = ordered[0], ordered[1:]
    if ( all(card.suit == first.suit for card in rest) and
         ' '.join(card.face for card in ordered) in fs ):
        return 'straight-flush', ordered[-1].face
    return False
 
    
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
def fourofakind(hand):
    allfaces = [f for f,s in hand]
    allftypes = set(allfaces)
    
    all_suits = [s for f, s in hand]
    all_stypes = set(all_suits)
    
    if len(allftypes) != 2:
        return False
    for f in allftypes:
        if allfaces.count(f) == 4:
            allftypes.remove(f)
            return 'four-of-a-kind', [f, allftypes.pop()]
    else:
        return False
 
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
def fullhouse(hand):
    allfaces = [f for f,s in hand]
    allftypes = set(allfaces)
    if len(allftypes) != 2:
        return False
    for f in allftypes:
        if allfaces.count(f) == 3:
            allftypes.remove(f)
            return 'full-house', [f, allftypes.pop()]
    else:
        return False
 
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
def flush(hand):
    allstypes = {s for f, s in hand}
    if len(allstypes) == 1:
        allfaces = [f for f,s in hand]
        return 'flush', sorted(allfaces,
                               key=lambda f: face.index(f),
                               reverse=True)
    return False
 
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
def straight(hand):
    f,fs = ( (lowace, lowaces) if any(card.face == '2' for card in hand)
             else (face, faces) )
    ordered = sorted(hand, key=lambda card: (f.index(card.face), card.suit))
    first, rest = ordered[0], ordered[1:]
    if ' '.join(card.face for card in ordered) in fs:
        return 'straight', ordered[-1].face
    return False
 
    
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
def threeofakind(hand):
    allfaces = [f for f,s in hand]
    allftypes = set(allfaces)
    if len(allftypes) <= 2:
        return False
    for f in allftypes:
        if allfaces.count(f) == 3:
            allftypes.remove(f)
            return ('three-of-a-kind', [f] +
                     sorted(allftypes,
                            key=lambda f: face.index(f),
                            reverse=True))
    else:
        return False
 
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
def twopair(hand):
    allfaces = [f for f,s in hand]
    allftypes = set(allfaces)
    pairs = [f for f in allftypes if allfaces.count(f) == 2]
    if len(pairs) != 2:
        return False
    p0, p1 = pairs
    other = [(allftypes - set(pairs)).pop()]
    return 'two-pair', pairs + other if face.index(p0) > face.index(p1) else pairs[::-1] + other
 
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
def onepair(hand):
    allfaces = [f for f,s in hand]
    allftypes = set(allfaces)
    pairs = [f for f in allftypes if allfaces.count(f) == 2]
    if len(pairs) != 1:
        return False
    allftypes.remove(pairs[0])
    return 'one-pair', pairs + sorted(allftypes,
                                      key=lambda f: face.index(f),
                                      reverse=True)

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

Note:
cards are in two digits
1st digit - encoded card value  or encoded rank 
2nd digit - suit
'''
def highcard(hand):
    allfaces = [f for f,s in hand]
    return 'high-card', sorted(allfaces,
                               key=lambda f: face.index(f),
                               reverse=True)
    
# extract values and suits information from cards
def set_Cards(hand):
    #print "ENTER SET_CARDS HAND:\t{}".format(hand)
    values=[]
    suits=[]
    for card in hand:
        #print card
        suits.append(card[-1])
        if  card[0] == 'j' or card[0] == 'J':
            values.append(11)
        elif  card[0] == 'q' or card[0] == 'A':
            values.append(12)
        elif  card[0] == 'k' or card[0] == 'K':
            values.append(13)
        elif  card[0] == 'a' or card[0] == 'A':
            values.append(14)
        elif card[0] == '10':
            values.append(10)
        
    #print "SET_CARDS: SUITS:\t{}".format(suits)
    #print "SET_CARDS: VALUES:\t{}".format(values)
    return sorted(values),suits  #values need to be sorted
 
handrankorder =  (royal_flush, straightflush, fourofakind, fullhouse,
                  flush, straight, threeofakind,
                  twopair, onepair, highcard)

'''
rank
rank function will iterate through the list of poker hand functions listed in
the handrankorder list to determine the poker hand.

Note:
cards are in two digits
1st digit - encoded card value  or encoded rank 
2nd digit - suit
''' 
def rank(cards):
    hand = handy(cards)
    for ranker in handrankorder:
        
        rank = ranker(hand)
        if rank:
            if (debug == 1):
                print "RANKER:\t{}".format(ranker)
                print "RANK:\t{}".format(rank)
                print "HAND:\t{}".format(hand)
                sys.exit(2)
            break
    assert rank, "Invalid: Failed to rank cards: %r" % cards
    return rank
 
'''
handy
Handy function to manipulate the 2 digit card string.
This function will determine the hand for each string, that is,
- the card value or rank --> f
- the suit of the card   --> s

This nifty function will iterate thru the five card hand to interogate the 
card value/rank and suit.

Additionally, this function provides error protection to insure there are only
5 cards in the hand and verify all cards in the hand are unique.

Note:
cards are in two digits
1st digit - encoded card value  or encoded rank 
2nd digit - suit
'''
def handy(cards='2h 2d 2c kc qd'):
    hand = []
    for card in cards.split():
        f, s = card[:-1], card[-1]
        assert f in face, "Invalid: Don't understand card face %r" % f
        assert s in suit, "Invalid: Don't understand card suit %r" % s
        hand.append(Card(f, s))
    assert len(hand) == 5, "Invalid: Must be 5 cards in a hand, not %i" % len(hand)
    assert len(set(hand)) == 5, "Invalid: All cards in the hand must be unique %r" % cards
    return hand
 

# A lot of times you will get text from some unknown encoding. 
# UTF-8 is the most common representation.
# If you need to catch errros, you can remove errors='ignore'
def convert_unicode(text):
    if isinstance(text,str):
        return text.decode('utf-8',errors='ignore')
    else:
        return text
 
if __name__ == '__main__':
    
    #suit = 'h d c s'.lower()
    #print suit
    
    #sys.exit(1)
    #sent = '@bob said the #chicken was at the #junkyard.'
    #out_tokens = convert_unicode(sent.split())
    #print(out_tokens)
    
    '''
    c1= ['10s','Js','Qs','Ks','As']  # --> Royal Flush!
    c2=['4d','5d','6d','7d','8d']    # --> Straight Flush!
    c3=['Qs','Qd','Qc','Qh','10s']   # --> Four of a kind!
    c4=['Ks','Kd','3h','3s','3c']    # --> Full house!
    c5=['Ad','Qd','6d','Jd','2d']    # --> Flush
    c6=['Ks','Qd','Jc','10h','9s']   #  --> Straight
    c7=['5d','Js','8h','8s','8d']    # --> Three of a kind!
    c8=['10s','Qd','7s','Qc','7h']   # --> Two pairs!
    c9=['10s','Jd','7s','6h','6s']   # --> Pair!
    c10=['7c','6d','4s','3h','2c']   # --> High Card
    
    c20 = ['As', 'Ac', 'Ah', 'Ad', '2c']     # four of a kind 
    c21 = ['Jc', '10c', '9c', '8c', '7c']    # straight flush
    c22 = ['5c', '5d', '5h', '5s', '2d']     # four of a kind
    c23 = ['6s', '6h', '6d', 'Kc', 'Kh']     # full house
    c24 = ['Jd', '9d','8d', '4d', '3d']      # flush
    c25 = ['10d', '9s', '8h', '7d', '6c' ]   # straight
    c26 = ['Qc', 'Qs', 'Qh', '9h', '2s']     # three of a kind 
    c27 = ['Jh', 'Jc', '3c', '3s', '2h']     # two pair
    c28 = ['10c', '10h', '8s', '7h', '4c']   # one pair
    c29 = ['Kd', 'Qd', '7s', '4s', '2h']     # high card
    c30 = ['Jh', 'Jc', '3c', '3s', '2h']     # --> Two pairs!
    '''
    
    hands = [
     "2h 2d 2c kc qd",
     "2h 5h 7d 8c 9h",
     "ah 2d 3c 4c 5d",
     "2h 3h 2d 3c 3d",
     "2h 7h 2d 3c 3d",
     "2h 7h 7d 7c 7s",
     "10h jh qh kh ah"] + [
     "4h 4c ks 5d 10s",
     "qc 10c 7c 6c 4c"] + [
     "10s js qs ks as",
     '4d 5d 6d 7d 8d',
     'qs qd qc qh 10s',
     'ks kd 3h 3s 3c',
     'ad qd 6d jd 2d',
     'ks qd jc 10h 9s',
     '5d js 8h 8s 8d',
     '10s  qd 7s qc 7h',
     '10s  jd 7s 6h 6s' ,
     '7c   6d 4s 3h 2c'] + [
     'as   ac ah ad 2c',
     'jc  10c 9c 8c 7c',
     '5c   5d 5h 5s 2d',
     '6s   6h 6d kc kh',
     'jd   9d 8d 4d 3d',
     '10d  9s 8h 7d 6c',
     'qc   qs qh 9h 2s',
     'jh   jc 3c 3s 2h',
     '10c 10h 8s 7h 4c',
     'kd   qd 7s 4s 2h',
     'jh   jc 3c 3s 2h',
     'as  2c  4h 5d ks'
      ]
             
    
    print("%-18s %-15s %s" % ("HAND", "CATEGORY", "TIE-BREAKER"))
    #sys.exit(2)
    
    #print hands[0].split()
    #print len(hands[0].split())
    #sys.exit(2)
    
    for cards in hands:
        #print cards.capitalize()
        #print cards
        #print len(cards.split())
        #print cards.count()
        #sys.exit(2)
        r = rank(cards)
        print("%-18r %-15s %r" % (cards, r[0], r[1]))