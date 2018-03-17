# -*- coding: utf-8 -*-
"""
Created on Thu Mar 01 16:58:49 2018

@author: Ben Brock
"""

from operator import attrgetter

from HandCommandPattern import HandCommandPattern
#from PokerHandUtility import PokerHandUtility

ORDERED_HAND_RANKS = 'royal_flush straight_flush four_of_a_kind full_house flush straight three_of_a_kind two_pair one_pair jacks_or_better high_card'

# faces as lists
ORDERED_HAND_RANK = ORDERED_HAND_RANKS.split()


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
        self.__total_poker_hand_card_value = 0
        
    def calculate_payout(self):
        
        self.__payout = float(self.get_bet_amount()) * float(self.get_payout_multiplier())
        
        return self.__payout
    
    def get_hand_list_format(self):
        return self.__hand_list_format
    
    def get_hand_string_format(self):
        return self.__hand_string_format
    
    def getTieBreaker(self):
        return self.__tie_breaker
    
    def getTotalPokerHandCardValue(self):
        return self.__total_poker_hand_card_value
    
    def setTotalPokerHandCardValue(self, value):
        self.__total_poker_hand_card_value = value
    
    def get_payout(self):
        return self.__payout
    
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
        self.__total_poker_hand_card_value = 0
        
        
    def calculate_payout(self):
        
        self.__payout = float(self.get_bet_amount()) * float(self.get_payout_multiplier())
        
        return self.__payout
    
    def get_hand_list_format(self):
        return self.__hand_list_format
    
    def get_hand_string_format(self):
        return self.__hand_string_format
    
    def getTieBreaker(self):
        return self.__tie_breaker
    
    def getTotalPokerHandCardValue(self):
        return self.__total_poker_hand_card_value
    
    def setTotalPokerHandCardValue(self, value):
        self.__total_poker_hand_card_value = value
        
    def get_payout(self):
        return self.__payout
    
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
        self.__total_poker_hand_card_value = 0
        
        
    def calculate_payout(self):
        
        self.__payout = float(self.get_bet_amount()) * float(self.get_payout_multiplier())
        
        return self.__payout
    
    def get_hand_list_format(self):
        return self.__hand_list_format
    
    def get_hand_string_format(self):
        return self.__hand_string_format
    
    def getTieBreaker(self):
        return self.__tie_breaker
    
    def getTotalPokerHandCardValue(self):
        return self.__total_poker_hand_card_value
    
    def setTotalPokerHandCardValue(self, value):
        self.__total_poker_hand_card_value = value
        
    def get_payout(self):
        return self.__payout
    
    
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
        self.__total_poker_hand_card_value = 0
        
        
    def calculate_payout(self):
        
        self.__payout = float(self.get_bet_amount()) * float(self.get_payout_multiplier())
        
        return self.__payout
    
    def get_hand_list_format(self):
        return self.__hand_list_format
    
    def get_hand_string_format(self):
        return self.__hand_string_format
    
    def getTieBreaker(self):
        return self.__tie_breaker
    
    def getTotalPokerHandCardValue(self):
        return self.__total_poker_hand_card_value
    
    def setTotalPokerHandCardValue(self, value):
        self.__total_poker_hand_card_value = value
        
    def get_payout(self):
        return self.__payout
    
    
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
        self.__total_poker_hand_card_value = 0
        
        
    def calculate_payout(self):
        
        self.__payout = float(self.get_bet_amount()) * float(self.get_payout_multiplier())
        
        return self.__payout
    
    def get_hand_list_format(self):
        return self.__hand_list_format
    
    def get_hand_string_format(self):
        return self.__hand_string_format
    
    def getTieBreaker(self):
        return self.__tie_breaker
    
    def getTotalPokerHandCardValue(self):
        return self.__total_poker_hand_card_value
    
    def setTotalPokerHandCardValue(self, value):
        self.__total_poker_hand_card_value = value
    
    def get_payout(self):
        return self.__payout
    
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
        self.__total_poker_hand_card_value = 0
        
        
    def calculate_payout(self):
        
        self.__payout = float(self.get_bet_amount()) * float(self.get_payout_multiplier())
        
        return self.__payout
    
    def get_hand_list_format(self):
        return self.__hand_list_format
    
    def get_hand_string_format(self):
        return self.__hand_string_format
    
    def getTieBreaker(self):
        return self.__tie_breaker
    
    def getTotalPokerHandCardValue(self):
        return self.__total_poker_hand_card_value
    
    def setTotalPokerHandCardValue(self, value):
        self.__total_poker_hand_card_value = value
    
    def get_payout(self):
        return self.__payout
    
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
        self.__total_poker_hand_card_value = 0
        
        
    def calculate_payout(self):
        
        self.__payout = float(self.get_bet_amount()) * float(self.get_payout_multiplier())
        
        return self.__payout
    
    def get_hand_list_format(self):
        return self.__hand_list_format
    
    def get_hand_string_format(self):
        return self.__hand_string_format
    
    def getTieBreaker(self):
        return self.__tie_breaker
    
    def getTotalPokerHandCardValue(self):
        return self.__total_poker_hand_card_value
    
    def setTotalPokerHandCardValue(self, value):
        self.__total_poker_hand_card_value = value
    
    def get_payout(self):
        return self.__payout
    
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
        self.__total_poker_hand_card_value = 0
        
        
    def calculate_payout(self):
        
        self.__payout = float(self.get_bet_amount()) * float(self.get_payout_multiplier())
        
        return self.__payout
    
    def get_hand_list_format(self):
        return self.__hand_list_format
    
    def get_hand_string_format(self):
        return self.__hand_string_format
    
    def getTieBreaker(self):
        return self.__tie_breaker
    
    def getTotalPokerHandCardValue(self):
        return self.__total_poker_hand_card_value
    
    def setTotalPokerHandCardValue(self, value):
        self.__total_poker_hand_card_value = value
        
    def get_payout(self):
        return self.__payout
    
    
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
        self.__total_poker_hand_card_value = 0
        
        
    def calculate_payout(self):
        
        self.__payout = float(self.get_bet_amount()) * float(self.get_payout_multiplier())
        
        return self.__payout
    
    def get_hand_list_format(self):
        return self.__hand_list_format
    
    def get_hand_string_format(self):
        return self.__hand_string_format
    
    def getTieBreaker(self):
        return self.__tie_breaker
    
    def getTotalPokerHandCardValue(self):
        return self.__total_poker_hand_card_value
    
    def setTotalPokerHandCardValue(self, value):
        self.__total_poker_hand_card_value = value
        
    def get_payout(self):
        return self.__payout
    
    
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
        self.__total_poker_hand_card_value = 0
        
        
    def calculate_payout(self):
        
        self.__payout = float(self.get_bet_amount()) * float(self.get_payout_multiplier())
        
        return self.__payout
    
    def get_hand_list_format(self):
        return self.__hand_list_format
    
    def get_hand_string_format(self):
        return self.__hand_string_format
    
    def getTieBreaker(self):
        return self.__tie_breaker
    
    def getTotalPokerHandCardValue(self):
        return self.__total_poker_hand_card_value
    
    def setTotalPokerHandCardValue(self, value):
        self.__total_poker_hand_card_value = value
    
    def get_payout(self):
        return self.__payout
    
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
        self.__total_poker_hand_card_value = 0
        
        
    def calculate_payout(self):
        
        self.__payout = float(self.get_bet_amount()) * float(self.get_payout_multiplier())
        
        return self.__payout
    
    def get_hand_list_format(self):
        return self.__hand_list_format
    
    def get_hand_string_format(self):
        return self.__hand_string_format
    
    def getTieBreaker(self):
        return self.__tie_breaker
    
    def getTotalPokerHandCardValue(self):
        return self.__total_poker_hand_card_value
    
    def setTotalPokerHandCardValue(self, value):
        self.__total_poker_hand_card_value = value
    
    def get_payout(self):
        return self.__payout
    
def main():

    from PokerHandUtility import PokerHandUtility
    
    bet_amount = 5
    multiplier = PokerHandUtility.HAND_PAYOUT_MULTIPLIER['royal_flush']
    rank = PokerHandUtility.POKER_HAND_RANK['royal_flush']
    command_name = 'royal_flush'
    hand_list_format = ["10s", "js", "qs", "ks", "as"]
    hand_string_format = "10s js qs ks as"
    tie_breaker = ['a', 'k', 'q', 'j', '10']
    values = [10, 11, 12, 13, 14]
    
    royal_flush_command = RoyalFlushCommand(bet_amount,
                                            multiplier,
                                            rank,
                                            command_name,
                                            hand_list_format,
                                            hand_string_format,
                                            tie_breaker)
    
    royal_flush_command.setTotalPokerHandCardValue(sum(values))

    print "\nAmount of BET {}".format(royal_flush_command.get_bet_amount())
    print "RANK {}".format(royal_flush_command.get_rank())
    print "MULTIPLIER {}".format(royal_flush_command.get_payout_multiplier())
    print "COMMAND NAME {}".format(royal_flush_command.getCommandName())
    print "PAYOUT {}".format(royal_flush_command.calculate_payout())
    print "PAYOUT {}".format(royal_flush_command.get_payout())
    print "HAND IN LIST FORMAT {}".format(royal_flush_command.get_hand_list_format())
    print "HAND IN STRING FORMAT {}".format(royal_flush_command.get_hand_string_format())
    print "TIE BREAKER {}".format(royal_flush_command.getTieBreaker())
    print "TOTAL POKER HAND SUM OF CARD VALUE is {}".format(royal_flush_command.getTotalPokerHandCardValue())
    
    ## 2nd Royal FLush Command
    
    royal_flush_command_1 = RoyalFlushCommand(bet_amount,
                                            multiplier,
                                            rank,
                                            command_name,
                                            hand_list_format,
                                            hand_string_format,
                                            tie_breaker)
    
    royal_flush_command_1.setTotalPokerHandCardValue(sum(values))
    
    bet_amount = 4
    multiplier = PokerHandUtility.HAND_PAYOUT_MULTIPLIER['straight']
    rank = PokerHandUtility.POKER_HAND_RANK['straight']
    command_name = 'straight'
    hand_list_format = ["10d", "9s", "8h", "7d", "6c"]
    hand_string_format = "10d 9s 8h 7d 6c"
    tie_breaker = ['10']
    values = [10, 9, 8, 7, 6]
    
    straight_command = StraightCommand(bet_amount,
                                 multiplier,
                                 rank,
                                 command_name,
                                 hand_list_format,
                                 hand_string_format,
                                 tie_breaker)
    
    straight_command.setTotalPokerHandCardValue(sum(values))
    
    print "\nAmount of BET {}".format(straight_command.get_bet_amount())
    print "RANK {}".format(straight_command.get_rank())
    print "MULTIPLIER {}".format(straight_command.get_payout_multiplier())
    print "COMMAND NAME {}".format(straight_command.getCommandName())
    print "PAYOUT {}".format(straight_command.calculate_payout())
    print "HAND IN LIST FORMAT {}".format(straight_command.get_hand_list_format())
    print "HAND IN STRING FORMAT {}".format(straight_command.get_hand_string_format())
    print "TIE BREAKER {}".format(straight_command.getTieBreaker())
    print "TOTAL POKER HAND SUM OF CARD VALUE is {}".format(straight_command.getTotalPokerHandCardValue())
    
    bet_amount = 5
    multiplier = PokerHandUtility.HAND_PAYOUT_MULTIPLIER['straight_flush']
    rank = PokerHandUtility.POKER_HAND_RANK['straight_flush']
    command_name = 'straight_flush'
    hand_list_format = ["4d", "5d", "6d", "7d", "8d"]
    hand_string_format = "4d 5d 6d 7d 8d"
    tie_breaker = ['8']
    values = [4, 5, 6, 7, 8]
    
    straight_flush_command = StraightFlushCommand(bet_amount,
                                                  multiplier,
                                                  rank,
                                                  command_name,
                                                  hand_list_format,
                                                  hand_string_format,
                                                  tie_breaker)
    straight_flush_command.setTotalPokerHandCardValue(sum(values))
    
    print "\nAmount of BET {}".format(straight_flush_command.get_bet_amount())
    print "RANK {}".format(straight_flush_command.get_rank())
    print "MULTIPLIER {}".format(straight_flush_command.get_payout_multiplier())
    print "COMMAND NAME {}".format(straight_flush_command.getCommandName())
    print "PAYOUT {}".format(straight_flush_command.calculate_payout())
    print "HAND IN LIST FORMAT {}".format(straight_flush_command.get_hand_list_format())
    print "HAND IN STRING FORMAT {}".format(straight_flush_command.get_hand_string_format())
    print "TIE BREAKER {}".format(straight_flush_command.getTieBreaker())
    print "TOTAL POKER HAND SUM OF CARD VALUE is {}".format(straight_flush_command.getTotalPokerHandCardValue())
    
    
    bet_amount = 5
    multiplier = PokerHandUtility.HAND_PAYOUT_MULTIPLIER['straight_flush']
    rank = PokerHandUtility.POKER_HAND_RANK['straight_flush']
    command_name = 'straight_flush'
    hand_list_format = ["9d", "10d", "jd", "qd", "kd"]
    hand_string_format = "9d  10d jd qd kd"
    tie_breaker = ['k']
    values = [9, 10, 11, 12, 13]
    
    straight_flush_command1 = StraightFlushCommand(bet_amount,
                                                  multiplier,
                                                  rank,
                                                  command_name,
                                                  hand_list_format,
                                                  hand_string_format,
                                                  tie_breaker)
    straight_flush_command1.setTotalPokerHandCardValue(sum(values))
    
    # Build Two Pair
    bet_amount = 5
    multiplier = PokerHandUtility.HAND_PAYOUT_MULTIPLIER['two_pair']
    rank = PokerHandUtility.POKER_HAND_RANK['two_pair']
    command_name = 'two_pair'
    hand_list_format = ["2h", "7h", "2d", "3c", "3d"]
    hand_string_format = "2h 7h 2d 3c 3d"
    tie_breaker = ['3', '2', '7']
    values = [2, 7, 2, 3, 3]
    
    two_pair_command_1 = TwoPairCommand(bet_amount,
                                                  multiplier,
                                                  rank,
                                                  command_name,
                                                  hand_list_format,
                                                  hand_string_format,
                                                  tie_breaker)
    two_pair_command_1.setTotalPokerHandCardValue(sum(values))
    
    
    bet_amount = 5
    multiplier = PokerHandUtility.HAND_PAYOUT_MULTIPLIER['two_pair']
    rank = PokerHandUtility.POKER_HAND_RANK['two_pair']
    command_name = 'two_pair'
    hand_list_format = ["10s", "qd", "7s", "qc", "7h"]
    hand_string_format = "10s  qd 7s qc 7h"
    tie_breaker = ['q', '7', '10']
    values = [10, 11, 7, 11, 7]
    
    two_pair_command_2 = TwoPairCommand(bet_amount,
                                                  multiplier,
                                                  rank,
                                                  command_name,
                                                  hand_list_format,
                                                  hand_string_format,
                                                  tie_breaker)
    two_pair_command_2.setTotalPokerHandCardValue(sum(values))
    
    
    bet_amount = 5
    multiplier = PokerHandUtility.HAND_PAYOUT_MULTIPLIER['two_pair']
    rank = PokerHandUtility.POKER_HAND_RANK['two_pair']
    command_name = 'two_pair'
    hand_list_format = ["qh", "qc", "kc", "ks", "2h"]
    hand_string_format = "qh qc kc ks 2h"
    tie_breaker = ['k', 'q', '2']
    values = [10, 11, 7, 11, 7]
    
    two_pair_command_3 = TwoPairCommand(bet_amount,
                                                  multiplier,
                                                  rank,
                                                  command_name,
                                                  hand_list_format,
                                                  hand_string_format,
                                                  tie_breaker)
    two_pair_command_3.setTotalPokerHandCardValue(sum(values))
    
    # High Card
    bet_amount = 5
    multiplier = PokerHandUtility.HAND_PAYOUT_MULTIPLIER['high_card']
    rank = PokerHandUtility.POKER_HAND_RANK['high_card']
    command_name = 'high_card'
    hand_list_format = ["2h", "5h", "7d", "8c", "9h"]
    hand_string_format = "2h 5h 7d 8c 9h"
    tie_breaker = ['9', '8', '7', '5', '2']
    values = [9, 8, 7, 5, 2]
    
    high_card_command = HighCardCommand(bet_amount,
                                                  multiplier,
                                                  rank,
                                                  command_name,
                                                  hand_list_format,
                                                  hand_string_format,
                                                  tie_breaker)
    high_card_command.setTotalPokerHandCardValue(sum(values))
    
    
    # Four of a Kind
    bet_amount = 5
    multiplier = PokerHandUtility.HAND_PAYOUT_MULTIPLIER['four_of_a_kind']
    rank = PokerHandUtility.POKER_HAND_RANK['four_of_a_kind']
    command_name = 'four_of_a_kind'
    hand_list_format = ["qs", "qd", "qc", "qh", "10s"]
    hand_string_format = "qs qd qc qh 10s"
    tie_breaker = ['q', '10']
    values = [12, 12, 12, 12, 10]
    
    four_of_a_kind_command = FourOfAKindCommand(bet_amount,
                                                  multiplier,
                                                  rank,
                                                  command_name,
                                                  hand_list_format,
                                                  hand_string_format,
                                                  tie_breaker)
    four_of_a_kind_command.setTotalPokerHandCardValue(sum(values))
    
    # Full House Command
    bet_amount = 5
    multiplier = PokerHandUtility.HAND_PAYOUT_MULTIPLIER['full_house']
    rank = PokerHandUtility.POKER_HAND_RANK['full_house']
    command_name = 'full_house'
    hand_list_format = ["ks", "kh", "kd", "ac", "qh"]
    hand_string_format = "ks kh kd qc qh"
    tie_breaker = ['k', 'q']
    values = [13, 13, 13, 12, 12]
    
    full_house_command = FullHouseCommand(bet_amount,
                                                  multiplier,
                                                  rank,
                                                  command_name,
                                                  hand_list_format,
                                                  hand_string_format,
                                                  tie_breaker)
    full_house_command.setTotalPokerHandCardValue(sum(values))
    
    # Flush Command
    bet_amount = 5
    multiplier = PokerHandUtility.HAND_PAYOUT_MULTIPLIER['flush']
    rank = PokerHandUtility.POKER_HAND_RANK['flush']
    command_name = 'flush'
    hand_list_format = ["ad", "kd", "qd", "jd", "9d"]
    hand_string_format = "ad kd qd jd 9d"
    tie_breaker = ['a', 'k', 'q', 'j', '9']
    values = [14, 13, 12, 11, 9]
    
    flush_command = FlushCommand(bet_amount,
                                                  multiplier,
                                                  rank,
                                                  command_name,
                                                  hand_list_format,
                                                  hand_string_format,
                                                  tie_breaker)
    flush_command.setTotalPokerHandCardValue(sum(values))
    
    
    # Three of a Kind Command
    bet_amount = 5
    multiplier = PokerHandUtility.HAND_PAYOUT_MULTIPLIER['three_of_a_kind']
    rank = PokerHandUtility.POKER_HAND_RANK['three_of_a_kind']
    command_name = 'three_of_a_kind'
    hand_list_format = ["ac", "as", "ah", "kh", "qs"]
    hand_string_format = "ac as ah kh qs"
    tie_breaker = ['a', 'k', 'q']
    values = [14, 14, 14, 13, 12]
    
    three_of_a_kind_command = ThreeOfAKindCommand(bet_amount,
                                                  multiplier,
                                                  rank,
                                                  command_name,
                                                  hand_list_format,
                                                  hand_string_format,
                                                  tie_breaker)
    three_of_a_kind_command.setTotalPokerHandCardValue(sum(values))
    
    # One Pair Command
    bet_amount = 5
    multiplier = PokerHandUtility.HAND_PAYOUT_MULTIPLIER['one_pair']
    rank = PokerHandUtility.POKER_HAND_RANK['one_pair']
    command_name = 'one_pair'
    hand_list_format = ["10c", "10h", "8s", "7h", "4c"]
    hand_string_format = "10c 10h 8s 7h 4c"
    tie_breaker = ['10', '8', '7', '4']
    values = [10, 10, 8, 7, 4]
    
    one_pair_command = OnePairCommand(bet_amount,
                                                  multiplier,
                                                  rank,
                                                  command_name,
                                                  hand_list_format,
                                                  hand_string_format,
                                                  tie_breaker)
    one_pair_command.setTotalPokerHandCardValue(sum(values))
    
    # Jacks or Better Command
    bet_amount = 5
    multiplier = PokerHandUtility.HAND_PAYOUT_MULTIPLIER['jacks_or_better']
    rank = PokerHandUtility.POKER_HAND_RANK['jacks_or_better']
    command_name = 'jacks_or_better'
    hand_list_format = ["ah", "ac", "ks", "qc", "jh"]
    hand_string_format = "ah ac ks qc jh"
    tie_breaker = ['a', 'k', 'q', 'j']
    values = [14, 14, 13, 12, 11]
    
    jacks_or_better_command = JacksOrBetterCommand(bet_amount,
                                                  multiplier,
                                                  rank,
                                                  command_name,
                                                  hand_list_format,
                                                  hand_string_format,
                                                  tie_breaker)
    jacks_or_better_command.setTotalPokerHandCardValue(sum(values))
    
    players_current_round_of_poker_hands = []
    players_current_round_of_poker_hands.append(royal_flush_command)
    players_current_round_of_poker_hands.append(royal_flush_command_1)
    players_current_round_of_poker_hands.append(straight_command)
    players_current_round_of_poker_hands.append(straight_flush_command)
    players_current_round_of_poker_hands.append(straight_flush_command1)
    players_current_round_of_poker_hands.append(two_pair_command_1)
    players_current_round_of_poker_hands.append(two_pair_command_2)
    players_current_round_of_poker_hands.append(two_pair_command_3)
    players_current_round_of_poker_hands.append(high_card_command)
    players_current_round_of_poker_hands.append(four_of_a_kind_command)
    players_current_round_of_poker_hands.append(full_house_command)
    players_current_round_of_poker_hands.append(flush_command)
    players_current_round_of_poker_hands.append(three_of_a_kind_command)
    players_current_round_of_poker_hands.append(one_pair_command)
    players_current_round_of_poker_hands.append(jacks_or_better_command)
    
    print "\n\nNUMBER OF POKER HANDS IN ROUND 1:\t{}".format(len(players_current_round_of_poker_hands)) 
    
    #ordered = sorted(players_current_round_of_poker_hands, key=lambda command: (f.index(command.get_rank()), command.getTotalPokerHandCardValue()))
    
    # To return a new list, use the sorted() built-in function...
    print "\nSORTED LIST BASED ON STYLE 1 OF USING SORTED COMMAND\n"
    sort_ordered_hands_by_poker_hand_rank = sorted(players_current_round_of_poker_hands, 
                     key=lambda command: command.get_rank(), 
                     reverse=False)
    
    print "\n\nHERE IS THE SORTED COMMAND LIST --> STYLE 1 <---\n\n{}".format(sort_ordered_hands_by_poker_hand_rank)
    print "\n\n****>>>> NUMBER OF ITEMS IN SORTED LIST {} <<<<<*****".format(len(sort_ordered_hands_by_poker_hand_rank))
    
    for item in sort_ordered_hands_by_poker_hand_rank:
        print item
  
    
    first, second = sort_ordered_hands_by_poker_hand_rank[0], sort_ordered_hands_by_poker_hand_rank[1:]
    
    #print "FIRST ITEM is {}:".format(first.getCommandName())
    
    #print "TEST: {}".format(ordered.count(first.getCommandName()))
    
    #print "NUMBER OF ITEMS LEFT IN LIST: {}".format(len(second))
    
    print "\nSORTED LIST BASED ON STYLE 2 OF USING SORTED COMMAND\n"
    test = sorted(players_current_round_of_poker_hands, key = attrgetter('getCommandName'), reverse=False)
    
    print "\n\nHERE IS THE SORTED COMMAND LIST  --> STYLE 2 <---\n\n{}".format(test)
    
    print "\nNUMBER OF ITEMS IN SORTED LIST: {}".format(len(test))
    
    for item in test:
        print item
    
    POKER_HAND_RANK_DIC = dict(
        royal_flush     = "RoyalFlushCommand",
        straight_flush  = "StraightFlushCommand",
        four_of_a_kind  = "FourOfAKindCommand",
        full_house      = "FullHouseCommand",
        flush           = "FlushCommand",
        straight        = "StraightCommand",
        three_of_a_kind = "ThreeOfAKindCommand",
        two_pair        = "TwoPairCommand",
        one_pair        = "OnePairCommand",
        jacks_or_better = "JacksOrBetterCommand",
        high_card       = "HighCardCommand")
        
    
    print "WINNING HAND IS:\t{}".format(POKER_HAND_RANK_DIC[first.getCommandName()])
    
    ## POKER STRING COMPARISON
    print "\nPOKER HAND COMPARISON\n\n"
    
    import re
    winning_hand = POKER_HAND_RANK_DIC[first.getCommandName()]
    number_of_times = 0
    for item in sort_ordered_hands_by_poker_hand_rank:
        #print item
        #print winning_hand
        
        '''
        if re.search("RoyalFlushCommand" , str(item)):
            print "FOUND IT"
            number_of_times = number_of_times + 1
        '''
            
        if "RoyalFlushCommand" in str(item):
            number_of_times = number_of_times + 1
            
    print "\nTOTAL WINNING POKERS WITH {} is {}\n\n".format(winning_hand, number_of_times)
        
    # result, winning_hands = determine_number_of_winning_poker_hands(winning_hand, test)
    
#    print "WINNING HAND OCCURS {} TIMES in the ORDERED COMMAND LIST".format(result)
    
    
    print "RESULT IS: {}".format(float(100/25))
    
    
    print "\n\nSTYLE 1 SEARCH BASED ON SEARCH FOR EXACT ROYAL_FLUSH_HAND\n"
    
    winner_command_type, winning_poker_hand = determine_the_winning_poker_royal_flush_hand(sort_ordered_hands_by_poker_hand_rank)
    
    if winner_command_type == None:
        
        print "\n\n<<<<<< Determine the winning poker hand is not implemented YET!! >>>>>>"
        print "\n ******** Stay tuned, it will be completed SOON!!! ******* \n\n"
        
    else:
        print "\n\nLet's Get Ready to Rumble!!!\n\n"
        print "WINNING POKER HAND IS {}".format(winner_command_type)
        print "NUMBER OF WINNING is {}".format(len(winning_poker_hand))
        
        for command in winning_poker_hand:
            print command
          
            
    print "\n\nSTYLE 1 SEARCH BASED ON ORDERING OF THE HIGHEST RANKED DATA IN THE LIST\n"
    
    winner_command_type, winning_poker_hands = determine_the_winning_poker_hand(sort_ordered_hands_by_poker_hand_rank)
    
    print "###### ROYAL FLUSH COMMAND NAME is {} ######".format(PokerHandUtility.POKER_HAND_COMMAND_NAME["royal_flush"])
    
    if winner_command_type == PokerHandUtility.POKER_HAND_COMMAND_NAME["royal_flush"]:
        
        if len(winning_poker_hands) == 1:
            print "\n\n **** WINNING COMMAND POKER HAND TYPE IS {} ****".format(winner_command_type)
            print " **** THE NUMBER OF {} WINNERS is {}".format(winner_command_type, len(winning_poker_hands))
            
        elif len(winning_poker_hands) > 1:
            print "\n\n **** WINNING COMMAND POKER HAND TYPE IS {} ****".format(winner_command_type)
            print " **** THE NUMBER OF {} WINNERS is {}".format(winner_command_type, len(winning_poker_hands))
            print " **** MUST SPLIT THE WINNING POT BETWEEN ALL OF THE POKER PLAYERS WITH THE ROYAL FLUSH POKER HAND"
            
            for command in winning_poker_hands:
                print command
        
    elif winner_command_type != PokerHandUtility.POKER_HAND_COMMAND_NAME["royal_flush"]:
        print "\n\nLet's Get Ready to Rumble!!!\n\n"
        print "WINNING POKER HAND IS {}".format(winner_command_type)
        print "NUMBER OF WINNING is {}".format(len(winning_poker_hands))
        
        for command in winning_poker_hands:
            print command
        
        print "\n\nLet investigate the list of poker hands named {}".format(winner_command_type) 
        
        winner = determine_the_winning_poker_non_royal_flush_hand(winner_command_type, winning_poker_hands)
        
        
        print "\n\n ***** Let's see who won!!!  *********"
        print "****  The winner player has a poker hand of a {} with a total poker hand of cards with a value of {}".format(winner.getCommandName(),
                                                                                                                            winner.getTotalPokerHandCardValue())
        
    ###  SCENARIO ATTACK ROYAL FLUSH PROBLEM
    ##    
    ## Case 1a)  One player with Royal Flush
    
    ## Case 2a)  One or more players with Royal Flush Hands
    
    '''
    For both cases above, call the determine_number_of_winning_poker_hands function 
    with the following input variables set
    @input parameters
    - winning_poker_hand :   POKER_HAND_RANK_DIC[royal_flush]  --> RoyalFlushCommand
    - ordered_list_of_player_poker_hand_commands   specific round of all poker players' hand commands
    
    @return number of Royal Flush Poker Hands winnings hands
    returns either 0
    - 0   --> indicates that no-one or winner with with a Royal Flush winning hand 
    
    - 1   --> indicates only one Poker player with a Royal Flush winning hand 
              a) the winning pot is distributed only to the player with the Royal Flush hand
                 - winning pot calculation:
                     - current RoyalFlushCommand.calculate_payout() + \
                              players 1:N "PokerHandCommand.calculate_payout()
                          
                # update the players bank_roll who won with the Royal Flush Command
                # WE KNOW HandCommand == RoyalFlushCommand
                temp_bank_roll = 0
                temp_bank_roll = winning_player.bank_roll + HandCommand.calculate_payout
                winning_player.set_bankroll(temp_bank_roll)
                
                or 
                
                winning_player.add_funds(HandCommand.calculate_payout())
              
                if winning_player == "WINNING PLAYER":
                    
                    temp_bank_roll_wrt_losers_hand = 0
                    # update the winning players bank roll based on the players who lost
                    for player in players_list:
                        
                        if player.Command.getName() != POKER_HAND_RANK_DIC[royal_flush]:
                              temp_bank_roll_wrt_losers_hand = temp_bank_roll_wrt_losers_hand + HandCommand.calculate_payout()
                              
                    winning_player.add_funds(temp_bank_roll_wrt_losers_hand)
                              
              b) players in the round must their current bank roll deducted by the 
                 players current Poker Hand Command.calculate_payout() 
                 
                 # LOSING PLAYERS ONLY!!
                 # NOT THE WINNING PLAYER with the Royal Flush Command
                 for player in players_list: 
                     
                     # update the players bank_roll who lost
                     if Command.getName() != POKER_HAND_RANK_DIC[royal_flush]:
                        player.bank_roll = player.bank_roll - HandCommand.calculate_payout()
                        # ------ or ------
                        # but not both.
                        # these commands are doing the same thing!!!
                        #
                        player.remove_funds(HandCommand.calculate_payout())
                     
    - >1  --> indicates multiple Poker players with a Royal Flush winning hand
              a) the winning pot must be split evenly between all of the Royal Flush winners
        
              Total winning pot
              
            if winning_player == "WINNING PLAYER":
                    
                    temp_winning_bank_roll = 0
                    # update the winning players bank roll based on the players who lost
                    for player in players_list:
                        
                        if player.Command.getName() == POKER_HAND_RANK_DIC[royal_flush]:
                              temp_winning_bank_roll = temp_winning_bank_roll + HandCommand.calculate_payout()
                              
                   ==> Not yet..... winning_player.add_funds(temp_bank_roll)
                   
                   keep the partial calculation
                    
              b) players in the round must their current bank roll deducted by the 
                 players current Poker Hand Command.calculate_payout() 
                 
                 Same as above
                 
                 
               winning_pot = (temp_winning_bank_roll + temp_bank_roll_wrt_losers_hand)/len(winning_players_list) 
               
               
               
            Now, lets add the winning pot evenly to each winning player with the RoyalFlushCommand
            
         if winning_player == "WINNING PLAYER":
                    
             
                    # update the winning players bank roll evenly distributed equally
                    for player in players_list:
                        
                        if player.Command.getName() == POKER_HAND_RANK_DIC[royal_flush]:
                              player.set_bankroll(winning_pot)
                 
        
    '''
    
    
    #print test[0].__class__
    
    #print test.count(test[0].__class__)
    
    #print test[0].__dict__
    
    #from collections import Counter
    #print "\n{}".format(Counter(test).most_common())
    
    #print "INTEROGATE THE LIST COUNT: {}".format(test.count(ordered[0].__class__.__name__))
    
    #result = test.__contains__(test[0].__metaclass__)
    #print result
    
    #print test.count(test[0])
    #print test[0].__class__
    
#    new_list = sorted(players_current_round_of_poker_hands, 
#                     key=lambda command: (ORDERED_HAND_RANK.index(command.get_rank()), command.getTotalPokerHandCardValue()), 
#                     reverse=False)
#    
#    first, second = new_list[0], new_list[1:]
#    
#    print "FIRST ITEM is {}:".format(first.getCommandName())


def determine_number_of_winning_poker_hands(winning_poker_hand, ordered_list_of_player_poker_hand_commands):
    
    print "\n>>>>>> ENTER determine_number_of_winning_poker_hands()  <<<<<<<\n"
    
    number_of_times_winning_hand_found = 0
    winning_poker_hands = []
    for item in ordered_list_of_player_poker_hand_commands:
        #print item
        
        if winning_poker_hand in str(item):
            number_of_times_winning_hand_found = number_of_times_winning_hand_found + 1
            winning_poker_hands.append(item)
            
            
    print "\n >>>>>> determine_number_of_winning_poker_hands::  WINNING POKER HANDS <<<<<<< \n{}".format(winning_poker_hands)
    print "\n >>>>>> determine_number_of_winning_poker_hands::  NUMBER OF WINNERS is {} <<<<<<".format(number_of_times_winning_hand_found)
        
    print "\n>>>>>> EXIT determine_number_of_winning_poker_hands()  <<<<<<<\n"
            
    return number_of_times_winning_hand_found, winning_poker_hands



'''
determine_the_winning_poker_royal_flush_hand

Find the number of royal flush poker hands in the input ordered list of player poker hands.
This is ok but not as flexible for any generic command

'''
def determine_the_winning_poker_royal_flush_hand(ordered_list_of_player_poker_hand_commands):
    
    print "\n>>>>>> ENTER determine_the_winning_poker_royal_flush_hand()  <<<<<<<\n"
    
    from PokerHandUtility import PokerHandUtility
    
    winning_hand_type = PokerHandUtility.POKER_HAND_RANK_DIC['royal_flush']
    
    num_of_winning_royal_flush_hands, winning_royal_flush_poker_hands = determine_number_of_winning_poker_hands(winning_hand_type, 
                                                                                                    ordered_list_of_player_poker_hand_commands)
    
    print "\nNumber of winning Royal Flush Hands is {}".format(num_of_winning_royal_flush_hands)
    
    
    print "\n>>>>>> EXIT determine_the_winning_poker_royal_flush_hand()  <<<<<<<\n"
    

    #return "\nNumber of winning Royal Flush Hands is {}".format(num_of_winning_royal_flush_hands), winning_royal_flush_poker_hands
    return winning_hand_type, winning_royal_flush_poker_hands



def determine_the_winning_poker_hand(ordered_list_of_player_poker_hand_commands):
    
    print "\n>>>>>> ENTER determine_the_winning_poker_hand()  <<<<<<<\n"
    
    from PokerHandUtility import PokerHandUtility
    first_command = ordered_list_of_player_poker_hand_commands[0]
    print "determine_the_winning_poker_hand() WINNING POKER HAND TYPE IS {}".format(first_command.getCommandName())
    print "determine_the_winning_poker_hand() WINNING POKER HAND COMMAND PATTERN IS {}".format(PokerHandUtility.POKER_HAND_RANK_DIC[first_command.getCommandName()])

    winning_hand_type = PokerHandUtility.POKER_HAND_RANK_DIC[first_command.getCommandName()]
    
    num_of_winning_hands, winning_poker_hand_types = determine_number_of_winning_poker_hands(winning_hand_type, \
                                                                                             ordered_list_of_player_poker_hand_commands)
    
    print "\nNumber of winning POKER Hands is {} with Poker Hand Command Type is a '{}'".format(num_of_winning_hands, winning_hand_type)
    
    
    print "\n>>>>>> EXIT determine_the_winning_poker_hand()  <<<<<<<\n"
    

    #return "\nNumber of winning Royal Flush Hands is {}".format(num_of_winning_royal_flush_hands), winning_royal_flush_poker_hands
    return first_command.getCommandName(), winning_poker_hand_types


def determine_the_winning_poker_non_royal_flush_hand(command, poker_hands_command_with_same_command_type):
    
    print "\n>>>>>> ENTER determine_the_winning_poker_non_royal_flush_hand()  <<<<<<<\n"
      
      # To return a new list, use the sorted() built-in function...
    print "\nSORTED LIST BASED ON STYLE 1 OF USING SORTED COMMAND with total poker hand of cards values sorted in descending order\n"
    sort_ordered_hands_by_hand_card_value = sorted(poker_hands_command_with_same_command_type, 
                                        key=lambda command: command.getTotalPokerHandCardValue(), 
                                        reverse=True)
    
    for cmd in sort_ordered_hands_by_hand_card_value:
        print "COMMAND TYPE is {} with total card hand value of {}".format(cmd.getCommandName(), cmd.getTotalPokerHandCardValue())
        
    
    winner = sort_ordered_hands_by_hand_card_value[0]
    
    print "\nTHE WINNING POKER HAND is a {} with a TOTAL HAND Card Values of {}".format(winner.getCommandName(), winner.getTotalPokerHandCardValue())
    
    print "\n>>>>>> EXIT determine_the_winning_poker_non_royal_flush_hand()  <<<<<<<\n"
    
    return winner


if __name__ == '__main__':
    main()
        
        
        
        
        
