# -*- coding: utf-8 -*-
"""
Created on Thu Mar 01 16:58:49 2018

@author: Ben Brock
"""

from HandCommandPattern import HandCommandPattern
from PokerHandUtility import PokerHandUtility

class OnePairCommand(HandCommandPattern):

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
    multiplier = PokerHandUtility.HAND_PAYOUT_MULTIPLIER['one_pair']
    rank = PokerHandUtility.POKER_HAND_RANK['one_pair']
    command_name = 'one_pair'
    hand_list_format = ["10c", "10h", "8s", "7h", "4c"]
    hand_string_format = "10c 10h 8s 7h 4c"
    tie_breaker = ['10', '8', '7', '4']
    
    one_pair_command = OnePairCommand(bet_amount,
                                      multiplier,
                                      rank,
                                      command_name,
                                      hand_list_format,
                                      hand_string_format,
                                      tie_breaker)
    
    print one_pair_command.get_bet_amount()
    print one_pair_command.get_rank()
    print one_pair_command.get_payout_multiplier()
    print one_pair_command.getCommandName()
    print one_pair_command.calculate_payout()
    print one_pair_command.get_hand_list_format()
    print one_pair_command.get_hand_string_format()

if __name__ == '__main__':
    main()
        
        
        
        
        
