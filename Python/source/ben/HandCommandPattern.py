# -*- coding: utf-8 -*-
"""
Created on Thu Mar 01 16:50:06 2018

@author: Ben Brock
"""

from abc import ABCMeta
from abc import abstractmethod

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

    