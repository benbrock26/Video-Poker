# -*- coding: utf-8 -*-
"""
Created on Thu Mar 01 16:58:49 2018

@author: Ben Brock
"""

from HandCommandPattern import HandCommandPattern
from PokerHandUtility import PokerHandUtility

class JacksOrBetterCommand(HandCommandPattern):

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
    multiplier = PokerHandUtility.HAND_PAYOUT_MULTIPLIER['jacks_or_better']
    rank = PokerHandUtility.POKER_HAND_RANK['jacks_or_better']
    command_name = 'jacks_or_better'
    hand_list_format = ["jh", "jc", "2s", "3c", "4h"]
    hand_string_format = "jh   jc 2s 3c 4h"
    tie_breaker = ['j', '4', '3', '2']
    
    jacks_or_better_command = JacksOrBetterCommand(bet_amount,
                                                   multiplier,
                                                   rank,
                                                   command_name,
                                                   hand_list_format,
                                                   hand_string_format,
                                                   tie_breaker)
    
    print jacks_or_better_command.get_bet_amount()
    print jacks_or_better_command.get_rank()
    print jacks_or_better_command.get_payout_multiplier()
    print jacks_or_better_command.getCommandName()
    print jacks_or_better_command.calculate_payout()
    print jacks_or_better_command.get_hand_list_format()
    print jacks_or_better_command.get_hand_string_format()

if __name__ == '__main__':
    main()
        
        
        
        
        
