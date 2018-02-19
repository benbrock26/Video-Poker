# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 07:55:47 2018

https://google.github.io/styleguide/pyguide.html


@author: Ben Brock and Shazia Zaman
"""

'''
Class:   Card
The Card class must support the valid suit types and ordered rank of collection
values of cards in a typical deck of cards.

Suit Types:
      Spades
      Clubs
      Diamonds
      Hearts
      
Ordered Rank of Collection of Cards:
    Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King
    
TO DO:
    
    (1) Should we support error checking in the Card class?
    We do not want the user to input invalid Card suit types or ordered rank
    value types.  Maybe we should think of doing some type of error checking.
    
    (2) Right now, we do not support the Joker card listed in the deck of Cards.
    Maybe, we should think of adding the Joker into the deck. This in return,
    will add to more variability in the types of Winning Hands evaluation.  
    But this issue of Hand evaluation will be dealt in the Poker class NOT 
    the Card class.  Our goal is to keep the clean and very well Object 
    Oriented. 

'''
from colour import Color

class Card(object):
    
    
    '''
    Global constants representing the valid Card suit types in a dictitonary
    style variable
    '''
    SUIT_TYPE_POS = dict(
            spades   = 1,
            clubs    = 2,
            diamonds = 3,
            hearts   = 4)
    
    '''
    Global constants representing the valid Card suit types in a list
    style variable
    '''
    SUIT_TYPE = ["Spades", 
                 "Clubs", 
                 "Diamonds", 
                 "Hearts"]
    
    '''
    Global constants representing the valid Card ORDERED RANK values for each
    SUIT TYPE
    '''
    ORDERED_RANK = ["Ace", 
                    "2", 
                    "3", 
                    "4", 
                    "5", 
                    "6", 
                    "7", 
                    "8", 
                    "9", 
                    "10", 
                    "Jack",
                    "Queen",
                    "King"]
    
    '''
    Global constants representing the OFFSET for printing specific suit type
    '''
    OFFSET = 2
    
    '''
    Constructor with complete initialization.
    @param suit -valid suit type of the deck of cards
                 Spades, Clubs, Diamonds, Hearts
    @param value - ordered rank listed in the poker requirements:
                 Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King
    @return: NONE
    '''
    def __init__(self, 
                 suit, 
                 value, 
                 suit_key_pos = SUIT_TYPE_POS["spades"]):
        
        self.__suit_type_key_pos = suit_key_pos
        self.suit_type = suit
        self.rank = value

    '''
    print_card method for card suit_type and rank
    @param NONE
    @return: NONE
    '''
    def print_card(self):
		print "{} of {}".format(self.rank, self.suit_type)


    def print_single_card(self):
        print("┌───────┐")
        print("| {:<2}    |".format(self.rank))
        print("|       |")
        print("|   {}   |".format(chr(self.__suit_type_key_pos+Card.OFFSET)))
        print("|       |")
        print("|    {:>2} |".format(self.rank))
        print("└───────┘") 
        
    '''
    set_suit_type_position method for getting the position in the available suit type 
    @param the suit key of the suits type position 
    '''
    def set_suit_type_position(self, suit_key):
        if suit_key in Card.SUIT_TYPE_POS:
            self.__suit_type_key_pos = Card.SUIT_TYPE_POS[suit_key]
        else:
            print "Invalid key {} does not exist in SUIT_TYPE_POS dictionary".format(suit_key)
            
        
    '''
    get_suit_type_position:
    Return the key value position in the dict suit_type_pos
    '''
    def get_suit_type_position(self):
        return self.__suit_type_key_pos
    
    
    '''
    This was done to make the Card class iterable
    '''
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

## Unit Test of the Card Class ####
def main():
    from Card import Card
    
    card = Card("Clubs", "6")
    card.print_card()
    
    print card.SUIT_TYPE[0]
    
    print card.SUIT_TYPE[3]
    card.print_single_card()
    
    print card.SUIT_TYPE_POS["spades"]
    
    card.set_suit_type_position("hearts")
    
    print card.get_suit_type_position()


    print("Now print all cards in the deck:\n")
    
    for suit in Card.SUIT_TYPE:
        
        print
        for card_value in Card.ORDERED_RANK:
            card = Card(suit, card_value)
            card.print_card()
            
if __name__ == '__main__':
    main()