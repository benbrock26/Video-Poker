# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 16:20:36 2018

@author: Ben Brock and Shazia Zaman
"""

from Card import Card
from Hand import Hand
from Deck import Deck

class Player(object):

     '''
     Player Constructor
     Set the players name, initializes the players hand, initializes list of hands,
     initializes players' bank roll and bet amount.
     
     @param: name
     @return: NONE
     '''
     def __init__(self, name):
         self.__name = name
         self.__current_hand = Hand()
         self.__list_of_hands = []
         self.__bank_roll = 0
         self.__bet_amount = 0
         
     
     '''
     Players Destructor
     clears the list of hands LIST
     @param: self
     @return: NONE
     '''
     def __del__(self):
        del self.__list_of_hands[:]
    
     '''
     add_card
     Add input new card object to the Players' hand
     @param:  new_card  - input Card object
     @return: NONE
     '''
     def add_card(self, new_card):
        self.__current_hand.add_card(new_card)
    
     '''
     add_funds
     Adds the specified amount to the player's funds
     @param: new_funds: The amount to be added to the player's funds
     @return: NONE
     '''
     def add_funds(self, new_funds):
        self.__bank_roll += new_funds
    
     '''
     remove_funds
     Removes the specified amount from the player's funds
     @param: amount_of_funds: The amount to be removed from the player's funds
     @return: NONE
     '''
     def remove_funds(self, amount_of_funds):
        self.__bank_roll -= amount_of_funds
    
     '''
     get_funds
     Retrieves the player's funds
     @param: self
     @return: int: The integer amount of funds the player has
     '''
     def get_funds(self):
        return self.__bank_roll
    
     '''
     get_bet_amount
     Retrieves the bet amount
     @param: self
     @return: int: The amount of money the player bet
     '''
     def get_bet_amount(self):
        return self.__bet_amount
    
     '''
     set_bet_amount
     Sets the bet amount
     @param: bet_amount : The amount of money the player is betting
     @return: NONE
     '''
     def set_bet_amount(self, bet_amount):
        self.__bet_amount = bet_amount
    
     '''
     get_name
     Retrieves the player's name
     @param: self
     @return string: The player's name
     '''
     def get_name(self):
        return self.__name
    
     '''
     five_card_stud_hand
     get_hand
     Retrieves the player's current hand
     @param: self
     @return: LIST :  The player's hand
     '''
     def get_hand(self):
        return self.__current_hand
    
     def get_current_hand_size(self):
         return len(self.__current_hand.get_cards())
    
     
     def show_hand(self):
         for card in self.__current_hand.get_cards():
             card.print_card()
             
     def draw(self, deck):
         self.__current_hand.add_card(deck.draw_card())
         return self
             
     '''
     reset
     Resets the player's bet and hand
     @param: self
     @return: NONE
     '''
     def reset(self):
        # reset the bet amount
        self.__bet_amount = 0
        
        # clear the players' current hand
        self.__current_hand.clear()
        
     '''
     get_list_of_players_hands
     Retrieves the players' history of list of hands
     @param: self
     @return: LIST : the list of players previous hands while playing poker
     '''
     def get_list_of_players_hands(self):
        return self.__list_of_hands
    
     '''
     This was done to make the Card class iterable
     '''
     def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    
## Unit Test of the Player Class ####
def main():
    print "...Start of Player Class Unit Testing...\n"
    
    from Player import Player
    bob = Player("bob")
    print "Players name:\t{}\n".format(bob.get_name())
    
    deck = Deck()
    deck.shuffle()
    
    print "Number of cards in the deck:\t{}\n" .format(deck.get_deck_size())
    
    
    bob.draw(deck).draw(deck).draw(deck).draw(deck).draw(deck)
    
    print "Players' current hand size:\t{}\n".format(bob.get_current_hand_size())
    
    bob.show_hand()
    
    
    print "\nUpdated Number of cards in the deck:\t{}\n".format(deck.get_deck_size())
    
    
    
            
if __name__ == '__main__':
    main()
    
        
    
    