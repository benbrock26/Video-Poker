# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 14:32:10 2018

@author: Ben Brock
"""




class PokerGameInterface (object):
    
    '''
    Command values
    '''
    SHOW_COMMANDS                                   = 0
    WELCOME_MESSAGE                                 = 1
    START_NEW_GAME_MESSAGE                          = 2
    INSERT_COINS                                    = 3
    DISPLAY_BANKROLL                                = 4
    PLACE_PLAYERS_BET                               = 5
    DISPLAY_PLAYERS_FIVE_CARD_STUD                  = 6
    DEAL                                            = 7
    CASH_OUT                                        = 8
    COINS_REMAINING                                 = 9
    DISPLAY_SUMMARY_OF_INTERPRETATION_OF_POKER_HAND = 10
    QUERY_CARD_0_KEEP_DISCARD                       = 11
    QUERY_CARD_1_KEEP_DISCARD                       = 12
    QUERY_CARD_2_KEEP_DISCARD                       = 13
    QUERY_CARD_3_KEEP_DISCARD                       = 14 
    QUERY_CARD_4_KEEP_DISCARD                       = 15   
    OTHER                                           = 99
    EXIT                                            = -1


    def __init__(self, game):
        self.game = game
        
    def display_welcome(self):
        print ("Welcome to the Poker Game")
        
    def display_new_game(self):
        print ("Display new game message")
        
    def display_players_five_card_stud_hand(self):
        print ("Display players 5 card stud hand")
        
    def display_winnings(self, amount):
        print ("You won:\t{} coins!".format(amount))
        
        
    