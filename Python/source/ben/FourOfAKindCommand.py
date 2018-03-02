# -*- coding: utf-8 -*-
"""
Created on Thu Mar 01 16:58:49 2018

@author: Ben Brock
"""

from HandCommandPattern import HandCommandPattern
from PokerHandUtility import PokerHandUtility

class FourOfAKindCommand(HandCommandPattern):

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
    multiplier = PokerHandUtility.HAND_PAYOUT_MULTIPLIER['four_of_a_kind']
    rank = PokerHandUtility.POKER_HAND_RANK['four_of_a_kind']
    command_name = 'four_of_a_kind'
    hand_list_format = ["qs", "qd", "qc", "qh", "10s"]
    hand_string_format = "qs qd qc qh 10s"
    tie_breaker = ['q', '10']
    
    four_of_a_kind_command = FourOfAKindCommand(bet_amount,
                                                  multiplier,
                                                  rank,
                                                  command_name,
                                                  hand_list_format,
                                                  hand_string_format,
                                                  tie_breaker)
    
    print four_of_a_kind_command.get_bet_amount()
    print four_of_a_kind_command.get_rank()
    print four_of_a_kind_command.get_payout_multiplier()
    print four_of_a_kind_command.getCommandName()
    print four_of_a_kind_command.calculate_payout()
    print four_of_a_kind_command.get_hand_list_format()
    print four_of_a_kind_command.get_hand_string_format()

if __name__ == '__main__':
    main()
        
        
        
        
        
