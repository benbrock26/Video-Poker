# -*- coding: utf-8 -*-
"""

https://rosettacode.org/wiki/Poker_hand_analyser#Python

https://en.wikipedia.org/wiki/List_of_poker_hands

https://en.wikipedia.org/wiki/List_of_poker_hands


https://briancaffey.github.io/2018/01/02/checking-poker-hands-with-python.html

https://www.pokerstars.com/poker/games/rules/hand-rankings/?no_redirect=1


NOTE:
    Will follow the Google Python Style Guide for the coding standards.
    
    https://google.github.io/styleguide/pyguide.html
    
Created on Sat Feb 24 08:33:29 2018

@author: Ben Brock and Shazia Zaman
"""

from collections import namedtuple
import sys

debug = 0
 
class Card(namedtuple('Card', 'face, suit')):
    def __repr__(self):
        return ''.join(self)
 
 
SUIT = 'h d c s'.split()

# ordered strings of faces
FACES    = '2 3 4 5 6 7 8 9 10 j q k a'
LOW_ACES = 'a 2 3 4 5 6 7 8 9 10 j q k'

# faces as lists
FACE    = FACES.split()
LOW_ACE = LOW_ACES.split()
 

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

Here after converting the card value or rank value to actual ordinal number 
in the list for this particular hand.

  [ 'a', 'k', 'q', 'j', 10]      ==> Royal flush via card value or rank value
  [ 14,   13,  12,  11, 10 ]     ==> Royal flush via converted max ordinal value
  
  With respect to the Royal flush in terms of the converted max ordinal value,
  the sum of all in values in the list is 60
  
  total_sum = 14 + 13 + 12 + 11 + 10 = 60

Design implementation implemented using Python 'set' data structure
  This made it very simplistic to verify if the hand is a royal flush based
  on the rules.
  
  - All cards MUST be of the SAME SUIT
  - 5 unique cards in the hand 
  - total sum of the converted ordinal values is 60; which is equivalent to
    [ 14,   13,  12,  11, 10 ] 

Note:
cards are in two digits
1st digit - encoded card value  or encoded rank
2nd digit - suit
'''
def royal_flush(hand):

    #print "ENTER ROYAL FLUSH: HAND:\t{}".format(hand)
    
    all_ranks = [f for f,s in hand]
    all_rank_types = set(all_ranks)
    
    all_suits = [s for f, s in hand]
    all_suit_types = len(set(all_suits))
        
    #print "ROYAL FLUSH: HAND:\t{}".format(hand)
    values, suit = set_cards_rank_value_to_max_rank_ordinal_value(hand)

    if all_suit_types == 1 and len(all_rank_types) == 5 and sum(values) == 60:
        #print "\nROYAL FLUSH: ALL FACES:\t{}".format(all_ranks)
        #print "ROYAL FLUSH: ALL FTYPES:\t{}".format(all_rank_types)
        #print "ROYAL FLUSH: NUMBER OF FTYPE's:\t{}".format(len(set(all_ranks)))
        #print "\nROYAL FLUSH: ALL SUITS:\t{}".format(all_suits)
        #print "ROYAL FLUSH: ALL SUIT TYPES:\t{}".format(all_suit_types)
        #print "ROYAL FLUSH SUM is:\t{}".format(sum(values))
        
        #sys.exit(2)
        
        return 'royal-flush',  sorted(all_ranks,
                               key=lambda f: FACE.index(f),
                               reverse=True)
    else:
        return False
 

'''
Straight Flush
Any five card sequence in the same suit.

A straight flush is a poker hand containing five cards of sequential rank, 
all of the same suit, such as Q♥ J♥ 10♥ 9♥ 8♥ (a "queen-high straight flush").

POKER HAND RANKINGS:  2

Example: 4d, 5d, 6d, 7d, 8d

Nice feature of Python:  any command
--> https://www.dotnetperls.com/any-python
--> https://www.programiz.com/python-programming/methods/built-in/any
--> The any() method returns True if any element of an iterable is true. 
    If not, this method returns False.

all() command
--> https://www.programiz.com/python-programming/methods/built-in/all
--> The all() method returns True when all elements in the given iterable 
    are true. If not, it returns False.
    
sorted command
--> https://medium.com/@johngrant/python-list-sorting-keys-lambdas-1903b2a4c949
--> https://www.pythoncentral.io/how-to-sort-a-list-tuple-or-object-with-sorted-in-python/
--> https://www.pythoncentral.io/how-to-sort-python-dictionaries-by-key-or-value/

Design implementation implemented using Python 'set' data structure
  This made it very simplistic to verify if the hand is a straight flush based
  on the rules.
  - All cards MUST be of the SAME SUIT
  - 5 unique cards in the hand 
  - len(all_rank_types) == 5
  - len(all_suit_types) == 1
  - sorted card list
  - hand will support LOW_ACES and FACES
  - display --> ['8', '7', '6', '4', '5']
    
Note:
cards are in two digits
1st digit - encoded card value  or encoded rank
2nd digit - suit
'''
def straight_flush(hand):
    f,fs = ( (LOW_ACE, LOW_ACES) if any(card.face == '2' for card in hand)
             else (FACE, FACES) )
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

Design implementation implemented using Python 'set' data structure
  This made it very simplistic to verify if the hand is a four of a kind based
  on the rules.
  - 5 unique cards in the hand 
  - length of all rank types is 2
  - all_ranks.count('Q') == 4
  - all_rank_types == 2 --> { '3', 'q'}
  - will display the set of all_rank_types 

Note:
cards are in two digits
1st digit - encoded card value  or encoded rank 
2nd digit - suit
'''
def four_of_a_kind(hand):
    all_ranks = [f for f,s in hand]
    all_rank_types = set(all_ranks)
    
    all_suits = [s for f, s in hand]
    all_suit_types = set(all_suits)
    
    # Only support 2 face types or two ranks of with respect to the card face
    # values
    #  "qs qd qc qh 3c"  ==> face types == 2
    if len(all_rank_types) != 2:
        return False
    for f in all_rank_types:
        if all_ranks.count(f) == 4:
            all_rank_types.remove(f)
            return 'four-of-a-kind', [f, all_rank_types.pop()]
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

Design implementation implemented using Python 'set' data structure
  This made it very simplistic to verify if the hand is a full house based
  on the rules.
  - 5 unique cards in the hand 
  - length of all rank types is 2
  - all_ranks.count == 3
  - function will list the highest rank
  
Note:
cards are in two digits
1st digit - encoded card value  or encoded rank 
2nd digit - suit
'''
def full_house(hand):
    all_ranks = [f for f,s in hand]
    all_rank_types = set(all_ranks)
    if len(all_rank_types) != 2:
        return False
    for f in all_rank_types:
        if all_ranks.count(f) == 3:
            all_rank_types.remove(f)
            return 'full-house', [f, all_rank_types.pop()]
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

Design implementation implemented using Python 'set' data structure
  This made it very simplistic to verify if the hand is a flush based
  on the rules.
  - 5 unique cards in the hand 
  - length of all suits types is 1
  - len(all_rank_types) == 5
  - all_rank_types = {'a', 'q', 'j', '6', '2'}
  - all_suit_types = {'d'}
  - len(all_suit_types) == 1
  - all_ranks in ordered sort order
  - function will list the sorted(all_ranks) --> ['a', 'q', 'j', '6', '2']
 
Note:
cards are in two digits
1st digit - encoded card value  or encoded rank 
2nd digit - suit
'''
def flush(hand):
    all_suit_types = {s for f, s in hand}
    if len(all_suit_types) == 1:
        all_ranks = [f for f,s in hand]
        return 'flush', sorted(all_ranks,
                               key=lambda f: FACE.index(f),
                               reverse=True)
    return False
 
'''
Straight
Five cards in sequence, but not in the same suit.

A straight is a poker hand containing five cards of sequential rank, not all 
of the same suit, such as 7♣ 6♠ 5♠ 4♥ 3♥ (a "seven-high straight")

POKER HAND RANKINGS:  6

Example:  Ks, Qd, Jc, 10h, 9s

- Similar to straight flush but without the constraint of having all cards  
  having the same suit.
  
Design implementation implemented using Python 'set' data structure
  This made it very simplistic to verify if the hand is a straight based
  on the rules.
  - 5 unique cards in the hand 
  - 4 of the cards do not belong to the same suit
  - all_ranks in ordered sort order
  - will display the highest order 
  
Note:
cards are in two digits
1st digit - encoded card value  or encoded rank 
2nd digit - suit
'''
def straight(hand):
    f,fs = ( (LOW_ACE, LOW_ACES) if any(card.face == '2' for card in hand)
             else (FACE, FACES) )
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

Design implementation implemented using Python 'set' data structure
  This made it very simplistic to verify if the hand is a three of a kind based
  on the rules.
  - 5 unique cards in the hand 
  - all_rank_types == 3 --> { '5', '8', 'J'}
  - all_ranks.count('8') == 3
  - will display the set of all_rank_types --> { '5', '8', 'J'}
  
Note:
cards are in two digits
1st digit - encoded card value  or encoded rank 
2nd digit - suit
'''
def three_of_a_kind(hand):
    all_ranks = [f for f,s in hand]
    all_rank_types = set(all_ranks)
    if len(all_rank_types) <= 2:
        return False
    for f in all_rank_types:
        if all_ranks.count(f) == 3:
            all_rank_types.remove(f)
            return ('three-of-a-kind', [f] +
                     sorted(all_rank_types,
                            key=lambda f: FACE.index(f),
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

Design implementation implemented using Python 'set' data structure
  This made it very simplistic to verify if the hand is a two pair based
  on the rules.
  - 5 unique cards in the hand 
  - all_rank_types == 3 --> { '10', '7', 'Q'}
  - all_ranks.count('Q') == 2 and all_ranks.count('7') == 2
  - len(all_rank_types) == 3
  - pairs = ['Q', '7']
  - len(pairs) == 2
  - will display the set of all_rank_types -->  { '10', '7', 'Q'}

Note:
cards are in two digits
1st digit - encoded card value  or encoded rank 
2nd digit - suit
'''
def two_pair(hand):
    
    all_ranks = [f for f,s in hand]
    all_rank_types = set(all_ranks)
    pairs = [f for f in all_rank_types if all_ranks.count(f) == 2]
    if len(pairs) != 2:
        return False
    p0, p1 = pairs
    other = [(all_rank_types - set(pairs)).pop()]
    return 'two-pair', pairs + other if FACE.index(p0) > FACE.index(p1) else pairs[::-1] + other
 
'''
One Pair
Two cars of the same rank.

One pair, or simply a pair, is a poker hand containing two cards of the same 
rank and three cards of three other ranks (the kickers), 

such as 4♥ 4♠ K♠ 10♦ 5♠ 

("one pair, fours" or a "pair of fours").

POKER HAND RANKINGS:  9

Example:  10s, Jd, 7s, 6h, 6c

Design implementation implemented using Python 'set' data structure
  This made it very simplistic to verify if the hand is a one pair based
  on the rules.
  - 5 unique cards in the hand 
  - all_rank_types == 4 --> {'10', '4', '5', 'k'}
  - all_ranks.count('4') == 2
  - len(all_rank_types) == 4
  - pairs = ['4']
  - len(pairs) == 1
  - will display the set of all_rank_types -->  {'10', '4', '5', 'k'}

Note:
cards are in two digits
1st digit - encoded card value  or encoded rank 
2nd digit - suit
'''
def one_pair(hand):
    
    #print "\nEnter\nONE_PAIR: HAND is {}".format(hand)
    all_ranks = [f for f,s in hand]
    all_rank_types = set(all_ranks)
    
    pairs = [f for f in all_rank_types if all_ranks.count(f) == 2]
    if len(pairs) != 1:
        return False
  
    '''
    Test and make sure the card pair IS NOT a 'J', 'Q', 'K', or 'A'
    '''
    if pairs[0].isalpha() and str(pairs[0]) in ['j', 'q', 'k', 'a']:
        return False
    
    all_rank_types.remove(pairs[0])
    return 'one-pair', pairs + sorted(all_rank_types,
                                      key=lambda f: FACE.index(f),
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

Design implementation implemented using Python 'set' data structure
  This made it very simplistic to verify if the hand is a one pair based
  on the rules.
  - 5 unique cards in the hand 
  - all_rank_types == 5 --> {'2', '3', '4', '6', '7'}
  - len(all_rank_types) == 5
  - will display the set of all_rank_types -->  {'7', '6', '4', '3', '2'}

Note:
cards are in two digits
1st digit - encoded card value  or encoded rank 
2nd digit - suit
'''
def high_card(hand):
    all_ranks = [f for f,s in hand]
    
    print "\nHIGH-CARD: HAND:\t{}".format(hand)    
    print "\nHIGH-CARD: ALL FACES:\t{}".format(all_ranks)
    print "HIGH-CARD: f\t{}".format(f)
    print "FACE:\t{}".format(FACE)
    
    return 'high-card', sorted(all_ranks,
                               key=lambda f: FACE.index(f),
                               reverse=True)
'''
jacks or better
Exactly on pair of Jacks, Queens, Kings, or Aces, and nothing else of interest.

Here after converting the card value or rank value to actual ordinal number 
in the list for this particular hand.

  [ 'a', 'a', '2', '2', 3]  ==> Jacks or Better via card value or rank value
  [ 14,   14,  2,  2,   3 ] ==> Jacks or Better via converted max ordinal value
  
  With respect to the Jacks or Better in terms of the converted max ordinal 
  value,the sum of all in values in the list is 35
  
  total_sum = 14 + 14 + 2 + 2 + 3 = 35

Design implementation implemented using Python 'set' data structure
  This made it very simplistic to verify if the hand is a jacks or better based
  on the rules.
  
  - All cards can be of any suit
  - at least 1 pair of either of the following: J, K, Q, A
  - 5 unique cards in the hand 
  - total sum of the converted ordinal values is 35; which is equivalent to
    [ 14,   14,  2,  2,   3] 
    
Example:  JH, JC, 2s, 2c, 3h

Payout 1:1

One quick thing about this hand is that is can be easily mis-classified as a
one-pair or two-pair.   Must interrogate the hand and check to make sure either
one of the high pairs ('J', 'Q', 'K', and 'A') are the ONLY valid pairs.

Based on the definition of this hand, the one-pair can 
not contain any of the high pairs of cards listed in the hand as listed above.

Note:
cards are in two digits
1st digit - encoded card value  or encoded rank 
2nd digit - suit
'''  
def jacks_or_better(hand):

    all_ranks = [f for f,s in hand]
    all_rank_types = set(all_ranks)
    
    pairs = [f for f in all_rank_types if all_ranks.count(f) == 2]
    if len(pairs) != 1:
        return False
    
    '''
    result = [ pair in [ 'j', 'q', 'k', 'a']  for pair in pairs ]
    if not result:
        return False
    '''
    '''
    Test and make sure the card pair IS a 'J', 'Q', 'K', or 'A'.  
    The logic here is to test if the pair is the following list:
    '2', '3', '4', '5', '6', '7', '8', '9', or '10'
    '''
    if not (pairs[0].isalpha() and str(pairs[0]) in ['j', 'q', 'k', 'a']):
        return False
    
    all_rank_types.remove(pairs[0])
    return 'jacks or better', pairs + sorted(all_rank_types,
                                      key=lambda f: FACE.index(f),
                                      reverse=True)
    

# extract values and suits information from cards
'''
set_cards_rank_value_to_max_rank_ordinal_value

set_cards_rank_value_to_max_rank_ordinal_value is a helper function which
will convert the high card face value's ('J', 'Q', 'K', 'A', '10') into
the cardinal values.

@param: hand  --> Players hand
@return: sorted values, suits 
'''
def set_cards_rank_value_to_max_rank_ordinal_value(hand):
    #print "ENTER set_cards_rank_value_to_max_rank_ordinal_value HAND:\t{}".format(hand)
    values=[]
    suits=[]
    for card in hand:
        #print card
        suits.append(card[-1])
        if  card[0] == 'j' or card[0] == 'J':
            values.append(11)
        elif  card[0] == 'q' or card[0] == 'Q':
            values.append(12)
        elif  card[0] == 'k' or card[0] == 'K':
            values.append(13)
        elif  card[0] == 'a' or card[0] == 'A':
            values.append(14)
        elif card[0] == '10':
            values.append(10)
        elif card[0] == '9':
            values.append(9)
        elif card[0] == '8':
            values.append(8)
        elif card[0] == '7':
            values.append(7)
        elif card[0] == '6':
            values.append(6)
        elif card[0] == '5':
            values.append(5)
        elif card[0] == '4':
            values.append(4)
        elif card[0] == '3':
            values.append(3)
        elif card[0] == '2':
            values.append(2)
    
    #print "\nOriginal player's 5 card poker hand:\t\t\t{}".format(hand)    
    #print "set_cards_rank_value_to_max_rank_ordinal_value: SUITS:\t{}".format(suits)
    #print "set_cards_rank_value_to_max_rank_ordinal_value: VALUES:\t{}".format(values)
    #print "ordinal value of player's 5 card poker hand:\t\t{}\n".format(sum(values))
    
    return sorted(values),suits  #values need to be sorted
 
    
'''
List of functional objects used for the poker hand evalution.  The function 
objects are listed in Poker hand priority order, i.e., from highest to lowest.
'''
hand_rank_order =  (royal_flush, 
                    straight_flush, 
                    four_of_a_kind, 
                    full_house,
                    flush, 
                    straight, 
                    three_of_a_kind,
                    two_pair, 
                    one_pair, 
                    jacks_or_better,
                    high_card)

'''
rank
rank function will iterate through the list of poker hand functions listed in
the hand_rank_order list to determine the poker hand.

Note:
cards are in two digits
1st digit - encoded card value  or encoded rank 
2nd digit - suit
''' 
def rank(cards):
    hand = handy(cards)
    for ranker in hand_rank_order:
        
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

This is where you instantiate or create a Card object based on the face value
and suit.  The Card face rank value and the suit value is created from the 
two digit encoded value (ie., '2h 2d 2c kc qd').  

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
        assert f in FACE, "Invalid: Don't understand card face %r" % f
        assert s in SUIT, "Invalid: Don't understand card suit %r" % s
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
    
    '''
    hands = ["2h 5h 7d 8c 9h",
             "2h 7h 2d 3c 3d",
             '10s  qd 7s qc 7h',
             'qh   qc kc ks 2h']
    '''
             
             
    #'''
    hands = [
     "10s js qs ks as", # royal flush
     "10h jh qh kh ah",
     '10c  jc qc kc ac',
     '10d  jd qd kd ad',
     '9s  10s js qs ks',  # straight flush
     '9d  10d jd qd kd', 
     '9c  10c jc qc kc', 
     '9h  10h jh qh kh', 
     'qc  jc 10c 9c 8c',
     'jc  10c 9c 8c 7c',
     '10c  9c 8c 7c 6c',
     '4d  5d 6d 7d 8d'] + [
     "2h 7h 7d 7c 7s",  # four-of-a-kind
     'qs qd qc qh 10s',
     'as   ac ah ad 2c',
     'as   ac ah ad kc',
     '5c   5d 5h 5s 2d',  
     'ks kd 3h 3s 3c', # full-house
     "2h 3h 2d 3c 3d",
     '6s 6h 6d kc kh',
     'ks kh kd qc qh',
     'as ah ad kc kh'] + [
     "qc 10c 7c 6c 4c", # flush
     'ad qd 6d jd 2d', 
     'jd   9d 8d 4d 3d',
     'ad   kd qd jd 9d',
     'ks qd jc 10h 9s', # straight
     "ah 2d 3c 4c 5d",
     '10d  9s 8h 7d 6c'] + \
     [ "2h 2d 2c kc qd", # three-of-a-kind
     '5d js 8h 8s 8d',
     'qc qs qh 9h 2s',
     'kc ks kh 9h 2s',
     'ac as ah 9h 2s',
     'ac as ah kh qs',
     "2h 7h 2d 3c 3d", # two pair
     '10s  qd 7s qc 7h',
     'jh   jc 3c 3s 2h',
     '10s  8h 7d 7s 8d',
     'jh   jc 3c 3s 2h',
     'qh   qc kc ks 2h',
     'kh   kc ac as 2h',
     'kh   kc ac as qh'] + [
     "4h 4c ks 5d 10s", # one-pair
     '10c 10h 8s 7h 4c',
     '9c 9h 8s 7h 4c',
     '10s  jd 7s 6h 6s',
     '10s  ad ks qh 10d'] + \
    ['jh   jc 2s 3c 4h', # jacks or better
     'qh   qc 2s 3c 4h',
     'kh   kc 2s 3c 4h',
     'ah   ac 2s 3c 4h',
     'ah   ac ks qc jh'] + \
    ["2h 5h 7d 8c 9h", # high-card
     '7c 6d 4s 3h 2c',
     'kd   qd 7s 4s 2h',
     'as   9c 10h jd ks']
    #'''
             
    
    print("%-18s %-15s %s\t\t\t\t\t\t\t%-30s" % ("HAND", "CATEGORY", "TIE-BREAKER", "PAY-OUT"))
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