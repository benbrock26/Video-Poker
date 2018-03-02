# -*- coding: utf-8 -*-
"""
Created on Thu Mar 01 16:58:49 2018

@author: Ben Brock
"""

from HandCommandPattern import HandCommandPattern
from PokerHandUtility import PokerHandUtility

class StraightCommand(HandCommandPattern):

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
    multiplier = PokerHandUtility.HAND_PAYOUT_MULTIPLIER['straight']
    rank = PokerHandUtility.POKER_HAND_RANK['straight']
    command_name = 'straight'
    hand_list_format = ["10d", "9s", "8h", "7d", "6c"]
    hand_string_format = "10d 9s 8h 7d 6c"
    tie_breaker = ['10']
    
    straight_command = StraightCommand(bet_amount,
                                 multiplier,
                                 rank,
                                 command_name,
                                 hand_list_format,
                                 hand_string_format,
                                 tie_breaker)
    
    print straight_command.get_bet_amount()
    print straight_command.get_rank()
    print straight_command.get_payout_multiplier()
    print straight_command.getCommandName()
    print straight_command.calculate_payout()
    print straight_command.get_hand_list_format()
    print straight_command.get_hand_string_format()

if __name__ == '__main__':
    main()
        
        
        
        
        
