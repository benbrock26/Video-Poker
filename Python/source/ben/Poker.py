# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 21:58:28 2018

@author: Ben Brock and Shazia Zaman
"""

from Deck import Deck
from Player import Player


'''
Starting Boilerplate for the Poker class.

This is where the most complex code will reside for the Poker game.

'''
class Poker(object):
    
    def __init__(self):
        pass
        self.__play_game = True
        self.__player = None
        self.__discard_cards = []
    
    def __del__(self):
        pass
    
    def add_view(self, game_view):
        self.game_view = game_view
    
    def add_player(self, player):
        self.__player = player
    
    def play(self):
        pass
    
    def get_player_funds(self):
        return self.__player.get_funds()
    
    def get_player_hand(self):
        return self.__player.get_hand()
        
    def is_bet_valid(self, amount):
        pass
    
    def evaluate_hand(self):
        pass
    
    def get_straight_type(self, values):
        pass
    
    def get_kind(self, values):
        pass
    
    def reset_table(self):
        pass
    
    def get_play_game(self):
        return self.__play_game
    
    def get_player(self):
        return self.__player
    
## Unit Test of the Poker Class ####
def main():
    
    print "\nUnit Testing of the Poker Class.....\n"
    
    print "\n.... This is where most of the complex logic will be located for the Poker Game...\n"
    
    
    
            
if __name__ == '__main__':
    main()