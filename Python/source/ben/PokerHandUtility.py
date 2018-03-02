# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 07:51:44 2018

@author: Ben Brock and Shazia Zaman
"""


#from Hand import Hand

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

class PokerHandUtility(object):
    
    CARD_SUIT = dict(
           Spades   = "s",
           Clubs    = "c",
           Diamonds = "d",
           Hearts   = "h")
    
    ORDERED_RANK = {
            "Ace":"a", 
            "2":2,
            "3":3,
            "4":4,
            "5":5,
            "6":6,
            "7":7,
            "8":8,
            "9":9,
            "10":10,
            "Jack":"j",
            "Queen":"q",
            "King" :"k"}
    
    HAND_PAYOUT_MULTIPLIER = dict(
            royal_flush     = 250,
            straight_flush  = 50,
            four_of_a_kind  = 25,
            full_house      = 9,
            flush           = 6,
            straight        = 4,
            three_of_a_kind = 3,
            two_pair        = 2,
            one_pair        = 1,
            jacks_or_better = 0.75,
            high_card       = 0.50)
    
    POKER_HAND_RANK = dict(
            royal_flush     = 1,
            straight_flush  = 2,
            four_of_a_kind  = 3,
            full_house      = 4,
            flush           = 5,
            straight        = 6,
            three_of_a_kind = 7,
            two_pair        = 8,
            one_pair        = 9,
            jacks_or_better = 10,
            high_card       = 11)
    
    
    def __init__(self):
        self.__hand = None
        self.__converted_current_hand_list = None
        self.__converted_current_hand_string = ""
        
    def get_hand(self):
        return self.__hand
    
    def get_converted_current_hand_list(self):
        return self.__converted_current_hand_list
    
    def get_converted_current_hand_string(self):
        return self.__converted_current_hand_string
    
    def set_poker_hand(self, hand):
        
        #print "ENTER SET POKER HAND"
        self.__hand = hand
        #print "PokerHandUtility::set poker_hand() POKER HAND IS {}".format(self.__hand)
        #print "EXIT SET POKER HAND"
        
        self.convert_hand_to_list()
        self.convert_hand_to_string()
        
    def convert_hand_to_list(self):
        
        if self.__hand:
            
            current_hand_list = []
            for card in self.__hand.get_cards():
                #card.print_card()
                ##print"{}{}".format(PokerHandUtility.ORDERED_RANK[card.get_rank()], 
                ##               PokerHandUtility.CARD_SUIT[card.get_suit()])
                dealt_card = '{}{}'.format(PokerHandUtility.ORDERED_RANK[card.get_rank()], 
                                 PokerHandUtility.CARD_SUIT[card.get_suit()])
                current_hand_list.append(dealt_card)
            
            self.__converted_current_hand_list = current_hand_list
    
    
    def convert_hand_to_string(self):
        
        if self.__hand:
            
            # 1st convert the hand to a list of cards
            self.convert_hand_to_list()
            
            # build a list of strings, separated by a space, then join them
            # Here we used List Compression
            self.__converted_current_hand_string = ' '.join([str for str in self.__converted_current_hand_list])
    
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
    def royal_flush(self, hand):
        
        all_ranks = [f for f,s in hand]
        all_rank_types = set(all_ranks)
    
        all_suits = [s for f, s in hand]
        all_suit_types = len(set(all_suits))
        
        #print "ROYAL FLUSH: HAND:\t{}".format(hand)
        values, suit = self.set_cards_rank_value_to_max_rank_ordinal_value(hand)
        
        if all_suit_types == 1 and len(all_rank_types) == 5 and sum(values) == 60:
            
            return 'royal_flush',  sorted(all_ranks,
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
    def straight_flush(self, hand):
        f,fs = ( (LOW_ACE, LOW_ACES) if any(card.face == '2' for card in hand)
                 else (FACE, FACES) )
        ordered = sorted(hand, key=lambda card: (f.index(card.face), card.suit))
        first, rest = ordered[0], ordered[1:]
        
        if ( all(card.suit == first.suit for card in rest) and
             ' '.join(card.face for card in ordered) in fs ):
            return 'straight_flush', ordered[-1].face
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
    def four_of_a_kind(self, hand):
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
                return 'four_of_a_kind', [f, all_rank_types.pop()]
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
    def full_house(self, hand):
        all_ranks = [f for f,s in hand]
        all_rank_types = set(all_ranks)
        if len(all_rank_types) != 2:
            return False
        for f in all_rank_types:
            if all_ranks.count(f) == 3:
                all_rank_types.remove(f)
                return 'full_house', [f, all_rank_types.pop()]
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
    def flush(self, hand):
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
    def straight(self, hand):
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
    def three_of_a_kind(self, hand):
        all_ranks = [f for f,s in hand]
        all_rank_types = set(all_ranks)
        if len(all_rank_types) <= 2:
            return False
        for f in all_rank_types:
            if all_ranks.count(f) == 3:
                all_rank_types.remove(f)
                return ('three_of_a_kind', [f] +
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
    def two_pair(self, hand):
        
        all_ranks = [f for f,s in hand]
        all_rank_types = set(all_ranks)
        pairs = [f for f in all_rank_types if all_ranks.count(f) == 2]
        if len(pairs) != 2:
            return False
        p0, p1 = pairs
        other = [(all_rank_types - set(pairs)).pop()]
        return 'two_pair', pairs + other if FACE.index(p0) > FACE.index(p1) else pairs[::-1] + other


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
    def one_pair(self, hand):
        
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
        return 'one_pair', pairs + sorted(all_rank_types,
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
    def high_card(self, hand):
        all_ranks = [f for f,s in hand]
        return 'high_card', sorted(all_ranks,
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
    def jacks_or_better(self, hand):
    
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
        return 'jacks_or_better', pairs + sorted(all_rank_types,
                                          key=lambda f: FACE.index(f),
                                          reverse=True)


    '''
    set_cards_rank_value_to_max_rank_ordinal_value
    
    set_cards_rank_value_to_max_rank_ordinal_value is a helper function which
    will convert the high card face value's ('J', 'Q', 'K', 'A', '10') into
    the cardinal values.
    
    @param: hand  --> Players hand
    @return: sorted values, suits 
    '''
    def set_cards_rank_value_to_max_rank_ordinal_value(self, hand):
        
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
        
        #print "set_cards_rank_value_to_max_rank_ordinal_value: SUITS:\t{}".format(suits)
        #print "set_cards_rank_value_to_max_rank_ordinal_value: VALUES:\t{}".format(values)
        return sorted(values),suits  #values need to be sorted
    
    
    '''
    List of functional objects used for the poker hand evalution.  The function 
    objects are listed in Poker hand priority order, i.e., from highest to lowest.
    '''
    def hand_rank_order_fnc_obs(self):
        
        hand_rank_order =  (self.royal_flush,
                            self.straight_flush,
                            self.four_of_a_kind,
                            self.full_house,
                            self.flush,
                            self.straight,
                            self.three_of_a_kind,
                            self.two_pair,
                            self.one_pair,
                            self.jacks_or_better,
                            self.high_card)
        
        return hand_rank_order
        
    '''
    rank
    rank function will iterate through the list of poker hand functions listed in
    the hand_rank_order list to determine the poker hand.
    
    Note:
    cards are in two digits
    1st digit - encoded card value  or encoded rank 
    2nd digit - suit
    ''' 
    def rank(self, cards):
        hand = self.handy(cards)
        for ranker in self.hand_rank_order_fnc_obs():
            
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
    def handy(self, cards='2h 2d 2c kc qd'):
        hand = []
        for card in cards.split():
            f, s = card[:-1], card[-1]
            assert f in FACE, "Invalid: Don't understand card face %r" % f
            assert s in SUIT, "Invalid: Don't understand card suit %r" % s
            hand.append(Card(f, s))
        assert len(hand) == 5, "Invalid: Must be 5 cards in a hand, not %i" % len(hand)
        assert len(set(hand)) == 5, "Invalid: All cards in the hand must be unique %r" % cards
        return hand
            
    
def main():
    pass

    poker_hand_utility = PokerHandUtility()
    
    print "START of UNIT TESTING OF POKER HAND UTILITY CLASS\n"
    #hands = ["10s js qs ks as"]
    
    #'''
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
     'as   2c 4h 5d ks',
     'jh   jc 2s 3c 4h',
     'qh   qc 2s 3c 4h',
     'kh   kc 2s 3c 4h',
     'ah   ac 2s 3c 4h',
     '10s  8h 7d 7s 8d',
     '9s  10s js qs ks',
     '10s  js qs ks as'
      ]
    #'''
    
    print("%-18s %-15s %s\t\t\t\t\t\t\t%-30s" % ("HAND", "CATEGORY", "TIE-BREAKER", "PAY-OUT"))
    
    for cards in hands:
        #print cards.capitalize()
        #print cards
        #print len(cards.split())
        #print cards.count()
        #sys.exit(2)
        r = poker_hand_utility.rank(cards)
        print("%-18r %-15s %r" % (cards, r[0], r[1]))
        
        
    print poker_hand_utility.HAND_PAYOUT_MULTIPLIER.keys()
    
    print poker_hand_utility.POKER_HAND_RANK.keys()
        
if __name__ == '__main__':
    main()
    