# -*- coding: utf-8 -*-
"""
Created on Thu Mar 01 16:58:49 2018

@author: Ben Brock
"""

from HandCommandPattern import HandCommandPattern
from PokerHandUtility import PokerHandUtility

class FullHouseCommand(HandCommandPattern):

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
    multiplier = PokerHandUtility.HAND_PAYOUT_MULTIPLIER['full_house']
    rank = PokerHandUtility.POKER_HAND_RANK['full_house']
    command_name = 'full_house'
    hand_list_format = ["2h", "3h", "2d", "3c", "13d"]
    hand_string_format = "2h 3h 2d 3c 3d"
    tie_breaker = ['3', '2']
    
    full_house_command = FullHouseCommand(bet_amount,
                                          multiplier,
                                          rank,
                                          command_name,
                                          hand_list_format,
                                          hand_string_format,
                                          tie_breaker)
    
    print full_house_command.get_bet_amount()
    print full_house_command.get_rank()
    print full_house_command.get_payout_multiplier()
    print full_house_command.getCommandName()
    print full_house_command.calculate_payout()
    print full_house_command.get_hand_list_format()
    print full_house_command.get_hand_string_format()

if __name__ == '__main__':
    main()
        
        
        
        
        
