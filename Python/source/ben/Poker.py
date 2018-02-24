# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 21:58:28 2018

@author: Ben Brock and Shazia Zaman
"""

from Deck import Deck
from Player import Player
import sys

debug = 0

'''
Starting Boilerplate for the Poker class.

This is where the most complex code will reside for the Poker game.

'''
class Poker(object):
    
    MAX_CARD_HAND_SIZE    = 5
    STARTING_CARD_SIZE    = 0
    
    def __init__(self):
        
        self.__play_game = True
        self.__discard_cards = []
        self.__discard_indices_list = []
        self.__discard_card_list = []
        self.__number_of_replacement_cards = 0
        
        # instantiate the objects controlled by the Poker object
        self.__deck = Deck()        ## 1 deck of cards
        self.__player = None        ## 1 to many player's
        self.__game_view = None     ## 1 PokerGameInterface
    
    def __del__(self):
        pass
    
    '''
    add_view
    Adds a "viewer" to the game

    @param: game_view: PokerGameInterface object : The interface that the player interacts with
    @return: NONE
    '''
    def add_view(self, game_view):
        self.__game_view = game_view
    
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
        
        if self.__player.get_hand():
            
            for idx in range(Poker.STARTING_CARD_SIZE, Poker.MAX_CARD_HAND_SIZE):
                
                action  = self.__game_view.get_action(idx)
                
                if action in ['k', 'd']:
                    
                    if action == 'k':
                        
                        if debug == 1:
                            print "ACTION is {}\n".format(action)
                        #do nothing
                        pass
                    elif action == 'd':
                        
                        if debug == 1:
                            print "ACTION is {}\n".format(action)
                        
                        # add index to discard_indices_list
                        self.__discard_indices_list.append(idx)
                        
                        # get the value to be removed from the crd list
                        temp_card = self.__player.get_hand().get_cards()[idx]
                        
                        # now add card to be removed it to the discard_card_list
                        self.__discard_card_list.append(temp_card)
                        self.__number_of_replacement_cards = self.__number_of_replacement_cards + 1
              
            if debug == 1:
                if self.__discard_indices_list:
                    print "\nDISCARD INDICES  LIST is {}\n".format(self.__discard_indices_list)
                else:
                    print "\nDISCARD INDICES LIST IS EMPTY\n" 
                if self.__discard_card_list:
                    print "\nDISCARD CARD LIST is {}\n".format(self.__discard_card_list)
                    [card.print_card()  for card in self.__discard_card_list]
                else:
                    print "\nDISCARD CARD LIST IS EMPTY\n" 
             
                print "\n\nNumber of Replacement Cards:\t{}".format(self.__number_of_replacement_cards)            
            
            
            self.remove_cards_from_hand()
            
            if self.__number_of_replacement_cards > 0:
                # add new random card or cards to the players hand
                self.add_new_cards_to_hand()
                
                self.__game_view.display_players_five_card_stud_hand_table_summary()
            
            
            '''
            Based on the "n" cards that were discarded by the user, 
            Now must add the "n" card random cards back to the deck of cards to replace the cards removed.
            ==> Will not have duplicate cards in the deck.
            '''
            
            # add the discarded cars back to the Deck
            self.add_discarded_cards_back_to_deck()
                    
        else:
            print "CANNOT KEEP OR DISCARD MANAGEMENT OF PLAYERS' HAND ==> PLAYERS HAND IS EMPTY NO CARDS ARE IN THE HAND\n"
            
        
    def add_new_cards_to_hand(self):
        
        #[ self.get_player_hand().get_cards().add_card(self.__deck.draw_card()) for index in range(0, self.__number_of_replacement_cards) ]
        
        if debug == 1:
            print
            for index in range(0, self.__number_of_replacement_cards):
                print "MUST ADD NEW CARD: CALL NUMBER: {}".format(index)
            
        for i in range(0, self.__number_of_replacement_cards):
            self.__player.get_hand().add_card(self.__deck.draw_card())

    
    '''
    Go thru the design to make sure the cards dealt to the Player is from the Pokers' object point of view.
    '''
    def add_discarded_cards_back_to_deck(self):
    
        if debug == 1:
            print "\nADD THE FOLLOWING CARDS FROM THE PLAYER's HAND BACK TO THE DECK OF CARDS\n"
        
            [ card.print_card()  for card in self.__discard_card_list ]
        
            print "\n\nDECK OF CARDS -- BFORE --\n\n"
            print "\n\nBEFORE -- NUMBER OF CARDS IN THE DECK:\t{}".format(self.__deck.get_deck_size())
        
        [ self.__deck.get_cards().append(card)  for card in self.__discard_card_list ]
        
        # reshuffle the deck after putting the cards back in the deck.
        self.__deck.shuffle()
        
        if debug == 1:
            print "\n\nAFTER -- NUMBER OF CARDS IN THE DECK:\t{}".format(self.__deck.get_deck_size())
    
    def get_deck(self):
        return self.__deck
    
    def remove_cards_from_hand(self):
        
        if debug == 1:
            print "\nREMOVE THE FOLLOWING CARDS FROM THE PLAYER's HAND\n"
            
            [ card.print_card()  for card in self.__discard_card_list ]
    
        
            print "\n\nPLAYERS CURRENT HAND -- BFORE --\n\n"
            self.__player.show_hand()
        
            print self.__player.get_hand().get_cards()
        
            print "\n..... DELETE CARDS FROM HAND BASED ON USER's REQUEST ....."
        
        [ self.__player.get_hand().get_cards().remove(card) for card in self.__discard_card_list ]
    
        if debug == 1:
            print "\n\nPLAYERS CURRENT HAND -- AFTER --\n\n"
            self.__player.show_hand()
        
## Unit Test of the Poker Class ####
def main():
    
    print "\nUnit Testing of the Poker Class.....\n"
    
    print "\n.... This is where most of the complex logic will be located for the Poker Game...\n"
    
    
    
            
if __name__ == '__main__':
    main()