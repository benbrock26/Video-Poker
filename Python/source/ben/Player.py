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
         self.__current_hand_size = 0
         
     
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
        self.__current_hand_size = self.__current_hand_size + 1
     '''
     add_funds
     Adds the specified amount to the player's funds
     @param: new_funds: The amount to be added to the player's funds
     @return: NONE
     '''
     def add_funds(self, new_funds):
        self.__bank_roll = self.__bank_roll + int(new_funds)
        
    
     '''
     remove_funds
     Removes the specified amount from the player's funds
     @param: amount_of_funds: The amount to be removed from the player's funds
     @return: NONE
     '''
     def remove_funds(self, amount_of_funds):
        self.__bank_roll = self.__bank_roll - int(amount_of_funds)
    
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
        return self.__current_hand.get_cards()
    
     def get_current_hand_size(self):
         return len(self.__current_hand.get_cards())
    
     
     def show_hand(self):
         for card in self.__current_hand.get_cards():
             card.print_card()
             
     def show_hand_by_index(self):
         
         '''
         The pythonic way to do it is from the PEP 8 style guide:
         https://stackoverflow.com/questions/53513/how-do-i-check-if-a-list-is-empty
         '''
         if self.__current_hand.get_cards():
             index = 0
             for card in self.__current_hand.get_cards():
                 card.print_card_by_index(index)
                 index = index + 1
         else:
            print "PLAYERS HAND IS EMPTY NO CARDS ARE IN THE HAND\n"
             
     def show_hand_ver1(self):
         idx = 0
         for card in self.__current_hand.get_cards():
             self.__current_hand.get_cards()[idx].print_card()
             idx = idx + 1
             
     def get_card_at_index(self, position):
         return self.__current_hand[position]
     
     def show_hand_single_card_format(self):
         for card in self.__current_hand.get_cards():
             card.print_single_card()
             
             
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
     add_hand_to_list_of_players_hands
     Add the latest current hand to the list of players hands
     This can be used to study the players hands later
     @param: self
     @param: list : five_stud_hand
     @return: NONE
     '''
     def add_hand_to_list_of_players_hands(self, five_stud_hand):
         self.__list_of_hands.append(five_stud_hand)
    
     def get_list_of_players_hands_size(self):
         return len(self.__list_of_hands)
     '''
     This was done to make the Card class iterable
     '''
     def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
     '''
     toString method
     @return - String respresentation in a customized card hand order
     '''
    
     def toString(self):
        return "Hand: \t\t{} Test\t| {} | {} | {} | {}".format(self.__current_hand.get_cards()[0].print_card(),
                                                    self.__current_hand.get_cards()[1].print_card(),
                                                    self.__current_hand.get_cards()[2].print_card(),
                                                    self.__current_hand.get_cards()[3].print_card(),
                                                    self.__current_hand.get_cards()[4].print_card())
    
    
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
    
    print "\n...Printing Bob's hand via the show_hand() method.....\n"
    bob.show_hand()
    
    print "\n...Printing Bob's hand via the get_hand() method.....\n"
    for card in bob.get_hand():
        card.print_card()
        
    print "\nUpdated Number of cards in the deck:\t{}\n".format(deck.get_deck_size())
    
    
    print "\nONLY ADD 5 STUD CARD HANDS TO LIST OF HISTORY OF HAND COMMANDS\n"
    
    bob.add_hand_to_list_of_players_hands(bob.get_hand())
    
    print "Number of hands listed in the HISTORY of Commands:\t{}\n".format(bob.get_list_of_players_hands_size())
    
    print "CARD:\t{}".format(bob.get_hand()[0].print_card())
    position = 2
    #print "CARD POSITION:\t{} is {}".format(position,   bob.get_card_at_index(position))
    
    bob.show_hand_ver1()
    
    
    
            
if __name__ == '__main__':
    main()
    
        
    
    