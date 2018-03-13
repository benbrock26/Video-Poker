# -*- coding: utf-8 -*-
"""

NOTE:
    Will follow the Google Python Style Guide for the coding standards.
    
    https://google.github.io/styleguide/pyguide.html
    
Created on Wed Feb 28 07:51:44 2018

@author: Ben Brock and Shazia Zaman
"""


#from Hand import Hand
from HandCommandPattern import HandCommandPattern
from PokerCommands import RoyalFlushCommand
from PokerCommands import StraightFlushCommand
from PokerCommands import FourOfAKindCommand
from PokerCommands import FullHouseCommand
from PokerCommands import FlushCommand
from PokerCommands import StraightCommand
from PokerCommands import ThreeOfAKindCommand
from PokerCommands import TwoPairCommand
from PokerCommands import OnePairCommand
from PokerCommands import HighCardCommand
from PokerCommands import JacksOrBetterCommand

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

ORDERED_HAND_RANKS = 'royal_flush straight_flush four_of_a_kind full_house flush straight three_of_a_kind two_pair one_pair jacks_or_better high_card'

# faces as lists
FACE    = FACES.split()
LOW_ACE = LOW_ACES.split()
ORDERED_HAND_RANK = ORDERED_HAND_RANKS.split()

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
    
    
    POKER_HAND_COMMAND_NAME = dict(
            royal_flush     = "royal_flush",
            straight_flush  = "straight_flush",
            four_of_a_kind  = "four_of_a_kind",
            full_house      = "full_house",
            flush           = "flush",
            straight        = "straight",
            three_of_a_kind = "three_of_a_kind",
            two_pair        = "two_pair",
            one_pair        = "one_pair",
            jacks_or_better = "jacks_or_better",
            high_card       = "high_card")
    
    POKER_HAND_RANK_DIC = dict(
        royal_flush     = "RoyalFlushCommand",
        straight_flush  = "StraightFlushCommand",
        four_of_a_kind  = "FourOfAKindCommand",
        full_house      = "FullHouseCommand",
        flush           = "FlushCommand",
        straight        = "StraightCommand",
        three_of_a_kind = "ThreeOfAKindCommand",
        two_pair        = "TwoPairCommand",
        one_pair        = "OnePairCommand",
        jacks_or_better = "JacksOrBetterCommand",
        high_card       = "HighCardCommand")
    
    def __init__(self):
        self.__hand = None
        self.__converted_current_hand_list = None
        self.__converted_current_hand_string = ""
        self.__bet_amount = None
        
    def get_hand(self):
        return self.__hand
    
    def get_converted_current_hand_list(self):
        return self.__converted_current_hand_list
    
    def get_converted_current_hand_string(self):
        return self.__converted_current_hand_string
    
    def set_poker_hand(self, hand):
        
        #print "ENTER SET POKER HAND"
        self.__hand = hand
        #print "PokerHandUtility::set poker_hand() POKER HAND IS<<<{}>>>".format(self.__hand)
        #print "EXIT SET POKER HAND"
        
        self.convert_hand_to_list()
        self.convert_hand_to_string()
        

        
        
    def set_poker_hand_on_fly(self, hand):
        
        self.__hand = hand
        
        self.convert_hand_on_fly_to_list()
        
        #print "SET POKER HAND ON FLY is {}".format(self.__converted_current_hand_list)
        
        '''
        This code was cheesy to do but I wanted to get this function done quickly.
        I tried to do this code in a one liner but I kept getting syntax errors.
        I fixed the bug for now and I will revisit this problem later.
        '''
        element_string = ""
        for elem in self.__converted_current_hand_list:
            #print elem
            element_string = str(elem) + " " + str(element_string)
            
        element_string = element_string.rstrip()  
        #print "FINAL <<<{}>>>".format(element_string.rstrip())
        #self.__converted_current_hand_string = ' '.join([elem for elem in self.__hand])
        
        self.__converted_current_hand_string = element_string
        
    def convert_hand_to_list(self):
        
        if self.__hand:
            
            current_hand_list = []
            for card in self.__hand:
                #card.print card
                ##print"{}{}".format(PokerHandUtility.ORDERED_RANK[card.get_rank()], 
                ##               PokerHandUtility.CARD_SUIT[card.get_suit()])
                dealt_card = '{}{}'.format(PokerHandUtility.ORDERED_RANK[card.get_rank()], 
                                 PokerHandUtility.CARD_SUIT[card.get_suit()])
                current_hand_list.append(dealt_card)
                
            self.__converted_current_hand_list = current_hand_list
    
    
    def convert_hand_on_fly_to_list(self):
        
        if self.__hand:
            
           self.__converted_current_hand_list = self.__hand
        
    
    def convert_hand_to_string(self):
        
        if self.__hand:
            
            # 1st convert the hand to a list of cards
            self.convert_hand_to_list()
            
            # build a list of strings, separated by a space, then join them
            # Here we used List Compression
            self.__converted_current_hand_string = ' '.join([x for x in self.__converted_current_hand_list])
    
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
        #print "ROYAL FLUSH HAND POKER HAND CARD VALUE LIST:\t{}".format(values)
        #print "ROYAL FLUSH HAND TOTAL POKER HAND CARD VALUE:\t{}".format(sum(values))
        
        if all_suit_types == 1 and len(all_rank_types) == 5 and sum(values) == 60:
            
            royal_flush_command = RoyalFlushCommand(self.__bet_amount, 
                                     PokerHandUtility.HAND_PAYOUT_MULTIPLIER['royal_flush'],
                                     PokerHandUtility.POKER_HAND_RANK['royal_flush'],
                                     'royal_flush',
                                     self.__converted_current_hand_list,
                                     self.__converted_current_hand_string,
                                     sorted(all_ranks,
                                            key=lambda f: FACE.index(f),
                                            reverse=True))
            
            # save the total poker hand card value
            royal_flush_command.setTotalPokerHandCardValue(sum(values))
            
            return royal_flush_command
                                          
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
        
        values, suit = self.set_cards_rank_value_to_max_rank_ordinal_value(hand)
        
        f,fs = ( (LOW_ACE, LOW_ACES) if any(card.face == '2' for card in hand)
                 else (FACE, FACES) )
        ordered = sorted(hand, key=lambda card: (f.index(card.face), card.suit))
        first, rest = ordered[0], ordered[1:]
        
        if ( all(card.suit == first.suit for card in rest) and
             ' '.join(card.face for card in ordered) in fs ):
            
            straight_flush_command = StraightFlushCommand(self.__bet_amount, 
                                                          PokerHandUtility.HAND_PAYOUT_MULTIPLIER['straight_flush'],
                                                          PokerHandUtility.POKER_HAND_RANK['straight_flush'],
                                                          'straight_flush',
                                                          self.__converted_current_hand_list,
                                                          self.__converted_current_hand_string,
                                                          ordered[-1].face)
            
            straight_flush_command.setTotalPokerHandCardValue(sum(values))
            
            return straight_flush_command

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
        
        values, suit = self.set_cards_rank_value_to_max_rank_ordinal_value(hand)
        
        # Only support 2 face types or two ranks of with respect to the card face
        # values
        #  "qs qd qc qh 3c"  ==> face types == 2
        if len(all_rank_types) != 2:
            return False
        for f in all_rank_types:
            if all_ranks.count(f) == 4:
                all_rank_types.remove(f)
                
                four_of_a_kind_cmd = FourOfAKindCommand(self.__bet_amount, 
                                       PokerHandUtility.HAND_PAYOUT_MULTIPLIER['four_of_a_kind'],
                                       PokerHandUtility.POKER_HAND_RANK['four_of_a_kind'],
                                      'four_of_a_kind',
                                      self.__converted_current_hand_list,
                                      self.__converted_current_hand_string,
                                      [f, all_rank_types.pop()])
                
                four_of_a_kind_cmd.setTotalPokerHandCardValue(sum(values))
                
                return four_of_a_kind_cmd

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
        
        values, suit = self.set_cards_rank_value_to_max_rank_ordinal_value(hand)
        
        if len(all_rank_types) != 2:
            return False
        for f in all_rank_types:
            if all_ranks.count(f) == 3:
                all_rank_types.remove(f)
                
                full_house_command = FullHouseCommand(self.__bet_amount, 
                                       PokerHandUtility.HAND_PAYOUT_MULTIPLIER['full_house'],
                                       PokerHandUtility.POKER_HAND_RANK['full_house'],
                                      'full_house',
                                      self.__converted_current_hand_list,
                                      self.__converted_current_hand_string,
                                      [f, all_rank_types.pop()])
                
                full_house_command.setTotalPokerHandCardValue(sum(values))
                
                return full_house_command
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
        
        values, suit = self.set_cards_rank_value_to_max_rank_ordinal_value(hand)
        
        all_suit_types = {s for f, s in hand}
        if len(all_suit_types) == 1:
            all_ranks = [f for f,s in hand]
            
            flush_command = FlushCommand(self.__bet_amount, 
                                       PokerHandUtility.HAND_PAYOUT_MULTIPLIER['flush'],
                                       PokerHandUtility.POKER_HAND_RANK['flush'],
                                      'flush',
                                      self.__converted_current_hand_list,
                                      self.__converted_current_hand_string,
                                      sorted(all_ranks,
                                             key=lambda f: FACE.index(f),
                                             reverse=True))
            
            flush_command.setTotalPokerHandCardValue(sum(values))
            
            return flush_command
        
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
        
        values, suit = self.set_cards_rank_value_to_max_rank_ordinal_value(hand)
        
        f,fs = ( (LOW_ACE, LOW_ACES) if any(card.face == '2' for card in hand)
                 else (FACE, FACES) )
        ordered = sorted(hand, key=lambda card: (f.index(card.face), card.suit))
        first, rest = ordered[0], ordered[1:]
        if ' '.join(card.face for card in ordered) in fs:
            
            straight_command = StraightCommand(self.__bet_amount, 
                                       PokerHandUtility.HAND_PAYOUT_MULTIPLIER['straight'],
                                       PokerHandUtility.POKER_HAND_RANK['straight'],
                                      'straight',
                                      self.__converted_current_hand_list,
                                      self.__converted_current_hand_string,
                                      ordered[-1].face)
            
            straight_command.setTotalPokerHandCardValue(sum(values))
            
            return straight_command
        
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
        
        values, suit = self.set_cards_rank_value_to_max_rank_ordinal_value(hand)
        
        if len(all_rank_types) <= 2:
            return False
        for f in all_rank_types:
            if all_ranks.count(f) == 3:
                all_rank_types.remove(f)
                
                three_of_a_kind_command = ThreeOfAKindCommand(self.__bet_amount, 
                                             PokerHandUtility.HAND_PAYOUT_MULTIPLIER['three_of_a_kind'],
                                             PokerHandUtility.POKER_HAND_RANK['three_of_a_kind'],
                                             'three_of_a_kind',
                                             self.__converted_current_hand_list,
                                             self.__converted_current_hand_string,
                                             [f] + sorted(all_rank_types,
                                                   key=lambda f: FACE.index(f),
                                                   reverse=True))
                
                three_of_a_kind_command.setTotalPokerHandCardValue(sum(values))
            
                return three_of_a_kind_command
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
        
        values, suit = self.set_cards_rank_value_to_max_rank_ordinal_value(hand)
        
        pairs = [f for f in all_rank_types if all_ranks.count(f) == 2]
        if len(pairs) != 2:
            return False
        p0, p1 = pairs
        other = [(all_rank_types - set(pairs)).pop()]
        
        two_pair_command = TwoPairCommand(self.__bet_amount, 
                                     PokerHandUtility.HAND_PAYOUT_MULTIPLIER['two_pair'],
                                     PokerHandUtility.POKER_HAND_RANK['two_pair'],
                                     'two_pair',
                                     self.__converted_current_hand_list,
                                     self.__converted_current_hand_string,
                                     pairs + other if FACE.index(p0) > FACE.index(p1) else pairs[::-1] + other)
        
        two_pair_command.setTotalPokerHandCardValue(sum(values))
                
        return two_pair_command


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
        
        values, suit = self.set_cards_rank_value_to_max_rank_ordinal_value(hand)
        
        pairs = [f for f in all_rank_types if all_ranks.count(f) == 2]
        if len(pairs) != 1:
            return False
      
        '''
        Test and make sure the card pair IS NOT a 'J', 'Q', 'K', or 'A'
        '''
        if pairs[0].isalpha() and str(pairs[0]) in ['j', 'q', 'k', 'a']:
            return False
        
        all_rank_types.remove(pairs[0])
        
        one_pair_command = OnePairCommand(self.__bet_amount, 
                                     PokerHandUtility.HAND_PAYOUT_MULTIPLIER['one_pair'],
                                     PokerHandUtility.POKER_HAND_RANK['one_pair'],
                                     'one_pair',
                                     self.__converted_current_hand_list,
                                     self.__converted_current_hand_string,
                                     pairs + sorted(all_rank_types,
                                                    key=lambda f: FACE.index(f),
                                                    reverse=True))
        
        one_pair_command.setTotalPokerHandCardValue(sum(values))
       
        return one_pair_command
    
    
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
        
        values, suit = self.set_cards_rank_value_to_max_rank_ordinal_value(hand)
        
        high_card_command = HighCardCommand(self.__bet_amount, 
                                     PokerHandUtility.HAND_PAYOUT_MULTIPLIER['high_card'],
                                     PokerHandUtility.POKER_HAND_RANK['high_card'],
                                     'high_card',
                                     self.__converted_current_hand_list,
                                     self.__converted_current_hand_string,
                                     sorted(all_ranks,
                                            key=lambda f: FACE.index(f),
                                            reverse=True))
        
        high_card_command.setTotalPokerHandCardValue(sum(values))
        
        return high_card_command

    '''
    jacks or better
    Exactly one pair of Jacks, Queens, Kings, or Aces, and nothing else of interest.
    
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
        
        values, suit = self.set_cards_rank_value_to_max_rank_ordinal_value(hand)
        
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
        
        jacks_or_better_command = JacksOrBetterCommand(self.__bet_amount, 
                                        PokerHandUtility.HAND_PAYOUT_MULTIPLIER['jacks_or_better'],
                                        PokerHandUtility.POKER_HAND_RANK['jacks_or_better'],
                                        'jacks_or_better',
                                        self.__converted_current_hand_list,
                                        self.__converted_current_hand_string,
                                        pairs + sorted(all_rank_types,
                                                    key=lambda f: FACE.index(f),
                                                    reverse=True))
        
        jacks_or_better_command.setTotalPokerHandCardValue(sum(values))
        
        return jacks_or_better_command


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
    List of function objects used for the poker hand evalution.  The function 
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
    def rank(self, cards, bet_amount):
        
        hand = self.handy(cards)
        
        self.__bet_amount = bet_amount
        
        self.set_poker_hand_on_fly(hand)
        
        #print "RANK HAND is <<<{}>>>>".format(hand)
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
    
    
    
    def determine_number_of_winning_poker_hands(self, 
                                                winning_poker_hand, 
                                                ordered_list_of_player_poker_hand_commands):
        
        if debug == 1:
            print "\n>>>>>> ENTER PokerHandUtility::determine_number_of_winning_poker_hands()  <<<<<<<\n"
        
        number_of_times_winning_hand_found = 0
        winning_poker_hands = []
        for item in ordered_list_of_player_poker_hand_commands:
            #print item
            
            if winning_poker_hand in str(item):
                number_of_times_winning_hand_found = number_of_times_winning_hand_found + 1
                winning_poker_hands.append(item)
                
        if debug == 1:  
            print "\n >>>>>> determine_number_of_winning_poker_hands::  WINNING POKER HANDS <<<<<<< \n{}".format(winning_poker_hands)
            print "\n >>>>>> determine_number_of_winning_poker_hands::  NUMBER OF WINNERS is {} <<<<<<".format(number_of_times_winning_hand_found)
            print "\n>>>>>> EXIT PokerHandUtility::determine_number_of_winning_poker_hands()  <<<<<<<\n"
                
        return number_of_times_winning_hand_found, winning_poker_hands


    def determine_the_winning_poker_royal_flush_hand(self, ordered_list_of_player_poker_hand_commands):
        
        if debug == 1:
            print "\n>>>>>> ENTER PokerHandUtility::determine_the_winning_poker_royal_flush_hand()  <<<<<<<\n"
                
        winning_hand_type = PokerHandUtility.POKER_HAND_RANK_DIC['royal_flush']
        
        num_of_winning_royal_flush_hands, winning_royal_flush_poker_hands = self.determine_number_of_winning_poker_hands(winning_hand_type, 
                                                                                                        ordered_list_of_player_poker_hand_commands)
        
        if debug == 1:
            print "\nNumber of winning Royal Flush Hands is {}".format(num_of_winning_royal_flush_hands)
            print "\n>>>>>> EXIT PokerHandUtility::determine_the_winning_poker_royal_flush_hand()  <<<<<<<\n"
        
    
        return winning_hand_type, winning_royal_flush_poker_hands



    def determine_the_winning_poker_hand(self, ordered_list_of_player_poker_hand_commands):
        
        if debug == 1:
            print "\n>>>>>> ENTER PokerHandUtility::determine_the_winning_poker_hand()  <<<<<<<\n"
        
        first_command = ordered_list_of_player_poker_hand_commands[0]
        
        if debug == 1:
            print "determine_the_winning_poker_hand() WINNING POKER HAND TYPE IS {}".format(first_command.getCommandName())
            print "determine_the_winning_poker_hand() WINNING POKER HAND COMMAND PATTERN IS {}".format(PokerHandUtility.POKER_HAND_RANK_DIC[first_command.getCommandName()])
    
        winning_hand_type = PokerHandUtility.POKER_HAND_RANK_DIC[first_command.getCommandName()]
        
        num_of_winning_hands, winning_poker_hand_types = self.determine_number_of_winning_poker_hands(winning_hand_type, \
                                                                                                 ordered_list_of_player_poker_hand_commands)
        
        if debug == 1:
            print "\nNumber of winning POKER Hands is {} with Poker Hand Command Type is a '{}'".format(num_of_winning_hands, winning_hand_type)
            print "\n>>>>>> EXIT PokerHandUtility::determine_the_winning_poker_hand()  <<<<<<<\n"
        
        return first_command.getCommandName(), winning_poker_hand_types

    def determine_the_winning_poker_non_royal_flush_hand(self, command, poker_hands_command_with_same_command_type):
        
        if debug == 1:
            print "\n>>>>>> ENTER PokerHandUtility::determine_the_winning_poker_non_royal_flush_hand()  <<<<<<<\n"
          
        if debug == 1:    
            # To return a new list, use the sorted() built-in function...
            print "\nSORTED LIST BASED ON STYLE 1 OF USING SORTED COMMAND with total poker hand of cards values sorted in descending order\n"
        
        sort_ordered_hands_by_hand_card_value = sorted(poker_hands_command_with_same_command_type, 
                                                       key=lambda command: command.getTotalPokerHandCardValue(), 
                                                       reverse=True)
        
        if debug == 1:
            for cmd in sort_ordered_hands_by_hand_card_value:
                print "COMMAND TYPE is {} with total card hand value of {}".format(cmd.getCommandName(), cmd.getTotalPokerHandCardValue())
                
        winner = sort_ordered_hands_by_hand_card_value[0]
        
        if debug == 1:
            print "\nTHE WINNING POKER HAND is a {} with a TOTAL HAND Card Values of {}".format(winner.getCommandName(), winner.getTotalPokerHandCardValue())
            
            print "\n>>>>>> EXIT PokerHandUtility::determine_the_winning_poker_non_royal_flush_hand()  <<<<<<<\n"
        
        return winner      

  
    
def main():
    pass

    poker_hand_utility = PokerHandUtility()
    bet_amount = 4
    
    print "START of UNIT TESTING OF POKER HAND UTILITY CLASS\n"
    
    hands = ["2h 5h 7d 8c 9h",
             "2h 7h 2d 3c 3d",
             '10s  qd 7s qc 7h',
             'qh   qc kc ks 2h',
             '9d  10d jd qd kd', 
             '9c  10c jc qc kc', 
             '9h  10h jh qh kh', 
             'qc  jc 10c 9c 8c',
             'jc  10c 9c 8c 7c',
             '10c  9c 8c 7c 6c']
    
    
    '''
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
     'as   2c 4h 5d ks',
     'jh   jc 2s 3c 4h',
     'qh   qc 2s 3c 4h',
     'kh   kc 2s 3c 4h',
     'ah   ac 2s 3c 4h',
     '10s  8h 7d 7s 8d',
     '9s  10s js qs ks',
     '10s  js qs ks as'
      ]
    '''
    
    print("%-18s %-15s %s" % ("HAND", "CATEGORY", "TIE-BREAKER"))
    
    for cards in hands:
        #print cards.capitalize()
        #print cards
        #print len(cards.split())
        #print cards.count()
        #sys.exit(2)
        cmd = poker_hand_utility.rank(cards, bet_amount)
        #hand_command_pattern = r[2]
        #print("%-18r %-15s %r" % (cards, r[0], r[1]))
        print("%-18r %-15s %r" % (cards, cmd.getCommandName(), cmd.getTieBreaker()))
        #print("%-18r %-15s %r" % (cards, 
        #                          hand_command_pattern.getCommandName(), 
        #                          hand_command_pattern.getTieBreaker()))
        
    #print hand_command_pattern.getCommandName()
    #print hand_command_pattern.calculate_payout()
        
    #print poker_hand_utility.HAND_PAYOUT_MULTIPLIER.keys()
    
    #print poker_hand_utility.POKER_HAND_RANK.keys()
        
if __name__ == '__main__':
    main()
    