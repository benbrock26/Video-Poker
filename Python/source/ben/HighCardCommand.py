# -*- coding: utf-8 -*-
"""
Created on Thu Mar 01 16:58:49 2018

@author: Ben Brock
"""

from HandCommandPattern import HandCommandPattern
from PokerHandUtility import PokerHandUtility

class HighCardCommand(HandCommandPattern):

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
    multiplier = PokerHandUtility.HAND_PAYOUT_MULTIPLIER['high_card']
    rank = PokerHandUtility.POKER_HAND_RANK['high_card']
    command_name = 'high_card'
    hand_list_format = ["kd", "qd", "7s", "4s", "2h"]
    hand_string_format = "kd qd 7s 4s 2h"
    tie_breaker = ['k', 'q', '7', '4', '2']
    
    high_card_command = HighCardCommand(bet_amount,
                                        multiplier,
                                        rank,
                                        command_name,
                                        hand_list_format,
                                        hand_string_format,
                                        tie_breaker)
    
    print high_card_command.get_bet_amount()
    print high_card_command.get_rank()
    print high_card_command.get_payout_multiplier()
    print high_card_command.getCommandName()
    print high_card_command.calculate_payout()
    print high_card_command.get_hand_list_format()
    print high_card_command.get_hand_string_format()

if __name__ == '__main__':
    main()
        
        
        
        
        
