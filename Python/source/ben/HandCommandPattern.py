# -*- coding: utf-8 -*-
"""
Created on Thu Mar 01 16:50:06 2018

@author: Ben Brock
"""

from abc import ABCMeta
from abc import abstractmethod


'''
HandCommandPattern

The goal of this root or parent class is to basic fundamental object for any of
the following eleven (11) poker hands:
    
Royal Flush:     10, Jack, Queen, King, Ace, all of the same suit 
Straight Flush:  Five ranks (or card face values) in a sequential counting row, 
                 all of the same suit (or best sorted order)
Four of a Kind:  Four cards of the same rank (or card face values)  
Full House:      Three cards of one rank and two cards of another rank 
Flush:           Five cards of the same suit    
Straight:        Five ranks in a row        
Three of a Kind: Three cards of one rank (but not a full house or four of a 
                 kind)
Two Pair:        Set of Two card values each of two different ranks
One Pair:        Set of One card values of the same rank (but not two pair,
                 three or four of a kind)       
Jacks or Better  Exactly one pair of Jacks, Queens, Kings, or Aces, and nothing 
                 else of interest.
                 One quick thing about this hand is that it can be easily 
                 mis-classified as a one-pair or two-pair.   Must interrogate 
                 the hand and check to make sure either one of the high pairs 
                 ('J', 'Q', 'K', and 'A') are the ONLY valid pairs.
High Card:       If none of the previous categories fir, X is the value of the 
                 highest rank. For example, if the largest rank is 11, the hand
                 is "Jack High"
                 High card, also known as no pair or simply nothing, is a poker
                 hand containing five cards not all of sequential rank or of 
                 the same suit, and none of which are of the same rank.
                 
Note:
    VALID CARD SUIT: "Diamonds, "Clubs", "Hearts", "Spades"
    VALID CARD RANK: "Ace", "Two", "Three", "Four", "Five", "Six", "Seven",
                     "Eight", "Nine", "Ten", "Jack", "Queen", "King"
'''

class HandCommandPattern(object):
    
    __metaclass__ = ABCMeta
 
    def __init__ (self,
                  bet_amount,
                  payout_multiplier,
                  rank,
                  command_name=None, 
                  debug=False):
    
            self.__bet_amount         = bet_amount
            self.__payout_multiplier  = payout_multiplier
            self.__rank               = rank
            self.__command_name       = command_name
            self.__debug              = debug
            
    @abstractmethod
    def calculate_payout(self):
        pass

    def getCommandName(self):
        return self.__command_name

    def getDebugFlag (self):
        return self.__debug

    def setDebugFlag (self, flag):
        self.__debug = flag
        
    def get_bet_amount(self):
        return self.__bet_amount 
    
    def get_payout_multiplier(self):
        return self.__payout_multiplier
    
    def get_rank(self):
        return self.__rank

    