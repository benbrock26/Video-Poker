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
    
    MAX_CARD_HAND_SIZE    = 5
    STARTING_CARD_SIZE    = 0
    
    def __init__(self):
        pass
        self.__play_game = True
        self.__player = None
        self.__discard_cards = []
        self.__game_view = []
        self.__discard_indices_list = []
        self.__discard_card_list = []
        self.__number_of_replacement_cards = 0
        
        self.__deck = Deck()
    
    def __del__(self):
        pass
    
    '''
    add_view
    Adds a "viewer" to the game

    @param: game_view: PokerGameInterface object : The interface that the player interacts with
    @return: NONE
    '''
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
    
    def get_game_view(self):
        return self.game_view
    
    
    def player_card_keep_delete_position_management(self):
        
        self.__discard_indices_list = []
        self.__discard_card_list = []
        self.__number_of_replacement_cards = 0
        
        if self.__current_hand.get_cards():
            
            for idx in range(Poker.STARTING_CARD_SIZE, Poker.MAX_CARD_HAND_SIZE):
                
                action  = self.__game_view.checker_action(idx)
                
                if action in ['k', 'd']:
                    
                    if action == 'k':
                        print "ACTION is {}\n".format(action)
                        #do nothing
                        pass
                    elif action == 'd':
                        print "ACTION is {}\n".format(action)
                        
                        # add index to discard_indices_list
                        self.__discard_indices_list.append(idx)
                        
                        # get the value to be removed from the crd list
                        temp_card = self.__player.get_hand().get_cards()[idx]
                        
                        # now add card to be removed it to the discard_card_list
                        self.__discard_card_list.append(temp_card)
                        self.__number_of_replacement_cards = self.__number_of_replacement_cards + 1
                        
            if self.__discard_indices_list:
                print "\nDISCARD INDICES  LIST is {}\n".format(self.__discard_indices_list)
            else:
               print "\nDISCARD INDICES LIST IS EMPTY\n" 
               
            if self.__discard_card_list:
                print "\nDISCARD CARD LIST is {}\n".format(self.__discard_card_list)
            else:
               print "\nDISCARD CARD LIST IS EMPTY\n" 
             
            print "Number of Replacement Cards:\t{}".format(self.__number_of_replacement_cards)            
            # add new random card or cards to the players hand
            self.add_new_card_to_hand()
            
            '''
            Based on the "n" cards that were discarded by the user, 
            Now must add the "n" card random cards back to the deck of cards to replace the cards removed.
            ==> Will not have duplicate cards in the deck.
            '''
            # add the discarded cars back to the Deck
            self.add_discarded_cards_back_to_deck()
                    
        else:
            print "CANNOT KEEP OR DISCARD MANAGEMENT OF PLAYERS' HAND ==> PLAYERS HAND IS EMPTY NO CARDS ARE IN THE HAND\n"
            
        
    def add_new_card_to_hand(self):
        pass
        
        [ self.get_player_hand().get_cards().add_card(self.__deck.draw_card()) for index in range(0, self.__number_of_replacement_cards) ]

    
    '''
    Go thru the design to make sure the cards dealt to the Player is from the Pokers' object point of view.
    '''
    def add_discarded_cards_back_to_deck(self):
        pass
    
## Unit Test of the Poker Class ####
def main():
    
    print "\nUnit Testing of the Poker Class.....\n"
    
    print "\n.... This is where most of the complex logic will be located for the Poker Game...\n"
    
    
    
            
if __name__ == '__main__':
    main()