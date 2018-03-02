# -*- coding: utf-8 -*-
"""
Created on Thu Mar 01 16:58:49 2018

@author: Ben Brock
"""

from HandCommandPattern import HandCommandPattern
from PokerHandUtility import PokerHandUtility

class TwoPairCommand(HandCommandPattern):

    def __init__ (self, 
                  bet_amount,
                  multiplier,
                  rank,
                  command_name,
                  hand_list_format,
                  hand_string_format,
                  tie_breaker):

        HandCommandPattern.__init__(self,
                                    bet_amount,
                                    multiplier,
                                    rank,
                                    command_name) 
        
        self.__hand_list_format = hand_list_format
        self.__hand_string_format = hand_string_format
        self.__tie_breaker = tie_breaker
        self.__payout = None
        
        
    def calculate_payout(self):
        
        self.__payout = self.get_bet_amount() * self.get_payout_multiplier()
        
        return self.__payout
    
    def get_hand_list_format(self):
        return self.__hand_list_format
    
    def get_hand_string_format(self):
        return self.__hand_string_format
    
    
def main():

    bet_amount = 1
    multiplier = PokerHandUtility.HAND_PAYOUT_MULTIPLIER['two_pair']
    rank = PokerHandUtility.POKER_HAND_RANK['two_pair']
    command_name = 'two_pair'
    hand_list_format = ["jh", "jc", "3c", "3s", "2h"]
    hand_string_format = "jh jc 3c 3s 2h"
    tie_breaker = ['j', '3', '2']
    
    two_pair_command = TwoPairCommand(bet_amount,
                                      multiplier,
                                      rank,
                                      command_name,
                                      hand_list_format,
                                      hand_string_format,
                                      tie_breaker)
    
    print two_pair_command.get_bet_amount()
    print two_pair_command.get_rank()
    print two_pair_command.get_payout_multiplier()
    print two_pair_command.getCommandName()
    print two_pair_command.calculate_payout()
    print two_pair_command.get_hand_list_format()
    print two_pair_command.get_hand_string_format()

if __name__ == '__main__':
    main()
        
        
        
        
        
