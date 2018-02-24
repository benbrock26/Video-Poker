# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 13:04:52 2018

@author: Ben Brock and Shazia Zaman
"""
import random
from Card import Card

class Deck(object):
    
    '''
    Constructor with complete initialization.
    Create a private variable card list that will be used within the Deck class.
    The Deck constructor will build the deck of cards based on CARD suit types 
    and the list of Card ordered rank cards available for each Card suit type.
    
    In this case, we will create the deck and then shuffle the cards to make sure
    there is some randomless in the cards being dealt.
    
    @param self
    @return: NONE
    '''
    def __init__(self):
        self.__cards = []
        self.__deck_size = 0
        self.build_deck_of_cards()
        self.shuffle()
        
        
    '''
    Destructor --> Deck Destructor.
    When the Deck class goes out of scope, we must clear all items in the list.
    Since we are using Python 2.7.X we must style listed below:
        
    del list[:]  --> Will delete the values of that list variable 
    
    Reference: https://stackoverflow.com/questions/850795/different-ways-of-clearing-lists
    
    @param self
    @return: NONE
    '''
    def __del__(self):
        del self.__cards[:]
      
    '''
    build_deck_of_cards.
    Build a deck of cards that will be used for the Poker game.  The deck of cards
    will support all four Card.SUIT_TYPE's and CARD.ORDERED_RANK values
    
    @param self
    @return: NONE
    '''        
    def build_deck_of_cards(self):
        
        for suit in Card.SUIT_TYPE:
            for value in Card.ORDERED_RANK:
                self.__cards.append(Card(suit, value))
                self.__deck_size = self.__deck_size + 1
             
    '''
    show_deck_of_cards.
    Print the complete list of deck of cards 
    
    @param self
    @return: NONE
    '''  
    def show_deck_of_cards(self):
        
        '''
        The pythonic way to do it is from the PEP 8 style guide: 
        https://stackoverflow.com/questions/53513/how-do-i-check-if-a-list-is-empty   
        '''
        if self.__cards:
            
            for c in self.__cards:
                c.print_card()
        else:
            print "CARD LIST IS EMPTY --> NO CARDS ARE IN LIST"
            
    '''
    shuffle.
    Shuffles the deck of cards 
    
    @param self
    @return: NONE
    '''  
    def shuffle(self):
        
        for i in range(len(self.__cards)-1, 0, -1):
            r = random.randint(0, i)
            self.__cards[i], self.__cards[r] = self.__cards[r], self.__cards[i]
          
    '''
    get_deck_size
    Returns the integer number of cards in the deck of cards list.
    
    @param self
    @return: int length of deck of cards listed 
    '''  
    def get_deck_size(self):
        return len(self.__cards)
    
    '''
    draw_card
    Retrieves the top card in the deck of card list.  This item will be removed
    and the list will be decreased by 1 Card item.
    
    @param self
    @return: Card --> returns the Card on the top of the deck of cards list.
    '''  
    def draw_card(self):
        self.__deck_size = self.__deck_size - 1
        return self.__cards.pop()
    
    '''
    This was done to make the Card class iterable
    '''
    def __eq__(self, other):
        return self.__dict__ == other.__dict__    
    
    def get_cards(self):
        return self.__cards
            
## Unit Test of the Deck Class ####
def main():
    
    from Deck import Deck
    
    deck = Deck()
    
    print "\nNumber of Cards in the original deck of cards:\t{}\n".format(deck.get_deck_size())
    deck.shuffle()
    deck.show_deck_of_cards()
    
    print "\nNumber of Cards in the deck of cards after shuffling the deck:\t{}\n".format(deck.get_deck_size())
    
    card = deck.draw_card()
    card.print_card()
    
    print "\nNumber of Cards in the deck of cards after drawing card from the deck:\t{}\n".format(deck.get_deck_size())
    
            
if __name__ == '__main__':
    main()