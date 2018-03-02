# -*- coding: utf-8 -*-
"""
Created on Thu Mar 01 16:58:49 2018

@author: Ben Brock
"""

from HandCommandPattern import HandCommandPattern
from PokerHandUtility import PokerHandUtility

class StraightFlushCommand(HandCommandPattern):

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
    multiplier = PokerHandUtility.HAND_PAYOUT_MULTIPLIER['straight_flush']
    rank = PokerHandUtility.POKER_HAND_RANK['straight_flush']
    command_name = 'straight_flush'
    hand_list_format = ["4d", "5d", "6d", "7d", "8d"]
    hand_string_format = "4d 5d 6d 7d 8d"
    tie_breaker = ['8']
    
    straight_flush_command = StraightFlushCommand(bet_amount,
                                                  multiplier,
                                                  rank,
                                                  command_name,
                                                  hand_list_format,
                                                  hand_string_format,
                                                  tie_breaker)
    
    print straight_flush_command.get_bet_amount()
    print straight_flush_command.get_rank()
    print straight_flush_command.get_payout_multiplier()
    print straight_flush_command.getCommandName()
    print straight_flush_command.calculate_payout()
    print straight_flush_command.get_hand_list_format()
    print straight_flush_command.get_hand_string_format()

if __name__ == '__main__':
    main()
        
        
        
        
        
