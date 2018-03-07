# -*- coding: utf-8 -*-
"""
Created on Thu Mar 01 16:58:49 2018

@author: Ben Brock
"""

from HandCommandPattern import HandCommandPattern
#from PokerHandUtility import PokerHandUtility

class RoyalFlushCommand(HandCommandPattern):

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
        
        self.__payout = float(self.get_bet_amount()) * float(self.get_payout_multiplier())
        
        return self.__payout
    
    def get_hand_list_format(self):
        return self.__hand_list_format
    
    def get_hand_string_format(self):
        return self.__hand_string_format
    
    def getTieBreaker(self):
        return self.__tie_breaker
    
    
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
        
        self.__payout = float(self.get_bet_amount()) * float(self.get_payout_multiplier())
        
        return self.__payout
    
    def get_hand_list_format(self):
        return self.__hand_list_format
    
    def get_hand_string_format(self):
        return self.__hand_string_format
    
    def getTieBreaker(self):
        return self.__tie_breaker
    
    
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
        
        self.__payout = float(self.get_bet_amount()) * float(self.get_payout_multiplier())
        
        return self.__payout
    
    def get_hand_list_format(self):
        return self.__hand_list_format
    
    def get_hand_string_format(self):
        return self.__hand_string_format
    
    def getTieBreaker(self):
        return self.__tie_breaker
    
    
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
        
        self.__payout = float(self.get_bet_amount()) * float(self.get_payout_multiplier())
        
        return self.__payout
    
    def get_hand_list_format(self):
        return self.__hand_list_format
    
    def get_hand_string_format(self):
        return self.__hand_string_format
    
    def getTieBreaker(self):
        return self.__tie_breaker
    
    
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
        
        self.__payout = float(self.get_bet_amount()) * float(self.get_payout_multiplier())
        
        return self.__payout
    
    def get_hand_list_format(self):
        return self.__hand_list_format
    
    def get_hand_string_format(self):
        return self.__hand_string_format
    
    def getTieBreaker(self):
        return self.__tie_breaker
    
    
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
        
        self.__payout = float(self.get_bet_amount()) * float(self.get_payout_multiplier())
        
        return self.__payout
    
    def get_hand_list_format(self):
        return self.__hand_list_format
    
    def get_hand_string_format(self):
        return self.__hand_string_format
    
    def getTieBreaker(self):
        return self.__tie_breaker
    
    
class ThreeOfAKindCommand(HandCommandPattern):

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
        
        self.__payout = float(self.get_bet_amount()) * float(self.get_payout_multiplier())
        
        return self.__payout
    
    def get_hand_list_format(self):
        return self.__hand_list_format
    
    def get_hand_string_format(self):
        return self.__hand_string_format
    
    def getTieBreaker(self):
        return self.__tie_breaker
    

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
        
        self.__payout = float(self.get_bet_amount()) * float(self.get_payout_multiplier())
        
        return self.__payout
    
    def get_hand_list_format(self):
        return self.__hand_list_format
    
    def get_hand_string_format(self):
        return self.__hand_string_format
    
    def getTieBreaker(self):
        return self.__tie_breaker
    
    
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
        
        self.__payout = float(self.get_bet_amount()) * float(self.get_payout_multiplier())
        
        return self.__payout
    
    def get_hand_list_format(self):
        return self.__hand_list_format
    
    def get_hand_string_format(self):
        return self.__hand_string_format
    
    def getTieBreaker(self):
        return self.__tie_breaker
    
    
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
        
        self.__payout = float(self.get_bet_amount()) * float(self.get_payout_multiplier())
        
        return self.__payout
    
    def get_hand_list_format(self):
        return self.__hand_list_format
    
    def get_hand_string_format(self):
        return self.__hand_string_format
    
    def getTieBreaker(self):
        return self.__tie_breaker
    
    
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
        
        self.__payout = float(self.get_bet_amount()) * float(self.get_payout_multiplier())
        
        return self.__payout
    
    def get_hand_list_format(self):
        return self.__hand_list_format
    
    def get_hand_string_format(self):
        return self.__hand_string_format
    
    def getTieBreaker(self):
        return self.__tie_breaker
    
def main():

    bet_amount = 5
    multiplier = PokerHandUtility.HAND_PAYOUT_MULTIPLIER['royal_flush']
    rank = PokerHandUtility.POKER_HAND_RANK['royal_flush']
    command_name = 'royal_flush'
    hand_list_format = ["10s", "js", "qs", "ks", "as"]
    hand_string_format = "10s js qs ks as"
    tie_breaker = ['a', 'k', 'q', 'j', '10']
    
    command = RoyalFlushCommand(bet_amount,
                                            multiplier,
                                            rank,
                                            command_name,
                                            hand_list_format,
                                            hand_string_format,
                                            tie_breaker)
    
    print "\nAmount of BET {}".format(command.get_bet_amount())
    print "RANK {}".format(command.get_rank())
    print "MULTIPLIER {}".format(command.get_payout_multiplier())
    print "COMMAND NAME {}".format(command.getCommandName())
    print "PAYOUT {}".format(command.calculate_payout())
    print "HAND IN LIST FORMAT {}".format(command.get_hand_list_format())
    print "HAND IN STRING FORMAT {}".format(command.get_hand_string_format())
    print "TIE BREAKER {}".format(command.getTieBreaker())
    
    bet_amount = 5
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
    
    print "\nAmount of BET {}".format(straight_command.get_bet_amount())
    print "RANK {}".format(straight_command.get_rank())
    print "MULTIPLIER {}".format(straight_command.get_payout_multiplier())
    print "COMMAND NAME {}".format(straight_command.getCommandName())
    print "PAYOUT {}".format(straight_command.calculate_payout())
    print "HAND IN LIST FORMAT {}".format(straight_command.get_hand_list_format())
    print "HAND IN STRING FORMAT {}".format(straight_command.get_hand_string_format())
    print "TIE BREAKER {}".format(straight_command.getTieBreaker())
    
    bet_amount = 5
    multiplier = PokerHandUtility.HAND_PAYOUT_MULTIPLIER['straight_flush']
    rank = PokerHandUtility.POKER_HAND_RANK['straight_flush']
    command_name = 'straight_flush'
    hand_list_format = ["4d", "5d", "6d", "7d", "8d"]
    hand_string_format = "4d 5d 6d 7d 8d"
    tie_breaker = ['8']
    
    command = StraightFlushCommand(bet_amount,
                                                  multiplier,
                                                  rank,
                                                  command_name,
                                                  hand_list_format,
                                                  hand_string_format,
                                                  tie_breaker)
    
    print "\nAmount of BET {}".format(command.get_bet_amount())
    print "RANK {}".format(command.get_rank())
    print "MULTIPLIER {}".format(command.get_payout_multiplier())
    print "COMMAND NAME {}".format(command.getCommandName())
    print "PAYOUT {}".format(command.calculate_payout())
    print "HAND IN LIST FORMAT {}".format(command.get_hand_list_format())
    print "HAND IN STRING FORMAT {}".format(command.get_hand_string_format())
    print "TIE BREAKER {}".format(command.getTieBreaker())

if __name__ == '__main__':
    main()
        
        
        
        
        
