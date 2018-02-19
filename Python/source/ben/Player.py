# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 16:20:36 2018

@author: Ben Brock and Shazia Zaman
"""

from Card import Card
from Hand import Hand

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
     '''
     def get_bet_amount(self):
        pass
    
     def set_bet_amount(self, bet_amount):
        pass
    
     def get_name(self):
        pass
    
     '''
     five_card_stud_hand
     '''
     def get_hand(self):
        pass
    
     def reset(self):
        pass
    
    
## Unit Test of the Player Class ####
def main():
    print "...Start of Player Class Unit Testing...\n"
    
    
            
if __name__ == '__main__':
    main()
    
        
    
    