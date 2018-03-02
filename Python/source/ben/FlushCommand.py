# -*- coding: utf-8 -*-
"""
Created on Thu Mar 01 16:58:49 2018

@author: Ben Brock
"""

from HandCommandPattern import HandCommandPattern
from PokerHandUtility import PokerHandUtility

class FlushCommand(HandCommandPattern):

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
    multiplier = PokerHandUtility.HAND_PAYOUT_MULTIPLIER['flush']
    rank = PokerHandUtility.POKER_HAND_RANK['flush']
    command_name = 'flush'
    hand_list_format = ["jd", "9d", "8d", "4d", "3d"]
    hand_string_format = "jd 9d 8d 4d 3d"
    tie_breaker = ['j', '9', '8', '4', '3']
    
    flush_command = FlushCommand(bet_amount,
                                 multiplier,
                                 rank,
                                 command_name,
                                 hand_list_format,
                                 hand_string_format,
                                 tie_breaker)
    
    print flush_command.get_bet_amount()
    print flush_command.get_rank()
    print flush_command.get_payout_multiplier()
    print flush_command.getCommandName()
    print flush_command.calculate_payout()
    print flush_command.get_hand_list_format()
    print flush_command.get_hand_string_format()

if __name__ == '__main__':
    main()
        
        
        
        
        
