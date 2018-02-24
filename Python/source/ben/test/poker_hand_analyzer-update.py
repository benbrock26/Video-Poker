# -*- coding: utf-8 -*-
"""

https://rosettacode.org/wiki/Poker_hand_analyser#Python

https://en.wikipedia.org/wiki/List_of_poker_hands

Created on Sat Feb 24 08:33:29 2018

@author: Ben Brock and Shazia Zaman
"""

from collections import namedtuple
import sys
 
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
 
 
def straightflush(hand):
    f,fs = ( (lowace, lowaces) if any(card.face == '2' for card in hand)
             else (face, faces) )
    ordered = sorted(hand, key=lambda card: (f.index(card.face), card.suit))
    first, rest = ordered[0], ordered[1:]
    if ( all(card.suit == first.suit for card in rest) and
         ' '.join(card.face for card in ordered) in fs ):
        return 'straight-flush', ordered[-1].face
    return False
 
def fourofakind(hand):
    allfaces = [f for f,s in hand]
    allftypes = set(allfaces)
    if len(allftypes) != 2:
        return False
    for f in allftypes:
        if allfaces.count(f) == 4:
            allftypes.remove(f)
            return 'four-of-a-kind', [f, allftypes.pop()]
    else:
        return False
 
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
 
def flush(hand):
    allstypes = {s for f, s in hand}
    if len(allstypes) == 1:
        allfaces = [f for f,s in hand]
        return 'flush', sorted(allfaces,
                               key=lambda f: face.index(f),
                               reverse=True)
    return False
 
def straight(hand):
    f,fs = ( (lowace, lowaces) if any(card.face == '2' for card in hand)
             else (face, faces) )
    ordered = sorted(hand, key=lambda card: (f.index(card.face), card.suit))
    first, rest = ordered[0], ordered[1:]
    if ' '.join(card.face for card in ordered) in fs:
        return 'straight', ordered[-1].face
    return False
 
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
 
def twopair(hand):
    allfaces = [f for f,s in hand]
    allftypes = set(allfaces)
    pairs = [f for f in allftypes if allfaces.count(f) == 2]
    if len(pairs) != 2:
        return False
    p0, p1 = pairs
    other = [(allftypes - set(pairs)).pop()]
    return 'two-pair', pairs + other if face.index(p0) > face.index(p1) else pairs[::-1] + other
 
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
 
def highcard(hand):
    allfaces = [f for f,s in hand]
    return 'high-card', sorted(allfaces,
                               key=lambda f: face.index(f),
                               reverse=True)
 
handrankorder =  (straightflush, fourofakind, fullhouse,
                  flush, straight, threeofakind,
                  twopair, onepair, highcard)
 
def rank(cards):
    hand = handy(cards)
    for ranker in handrankorder:
        rank = ranker(hand)
        if rank:
            break
    assert rank, "Invalid: Failed to rank cards: %r" % cards
    return rank
 
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
    c27 = ['Jh', 'Jc', '3c', '3s', '2h']    # two pair
    c28 = ['10c', '10h', '8s', '7h', '4c']   # one pair
    c29 = ['Kd', 'Qd', '7s', '4s', '2h']     # high card
    c30 = ['Jh', 'Jc', '3c', '3s', '2h']     # --> Two pairs!
    '''
    
    hands = ["2h 2d 2c kc qd",
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
     'ks kd 3h 3s 3c']
             
    
    print("%-18s %-15s %s" % ("HAND", "CATEGORY", "TIE-BREAKER"))
    #sys.exit(2)
    
    #print hands[0].split()
    #print len(hands[0].split())
    #sys.exit(2)
    
    for cards in hands:
        r = rank(cards)
        print("%-18r %-15s %r" % (cards, r[0], r[1]))