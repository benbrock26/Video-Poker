# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 14:39:06 2018

@author: Ben Brock and Shazia Zaman
"""

from Card import Card

class Hand(object):
    
    '''
    Hand constructor
    The initial poker hand.   The hand will only contain card objects
    
    '''
    def __init__(self):
        self.__hand = []
    
    
    '''
    Hand destructor
    
    '''
    def __del__(self):
        self.clear() # delete all card objects in the hand list
        pass
    
    '''
    add_card
    Add card object to the hand
    
    @param new_card
           Add new card to the hand list
    @return - NONE
    '''
    def add_card(self, new_card):
        self.__hand.append(new_card)
    
    
    '''
    remove card
    remove card in the list based on the position.  The hand list will be 
    reduced by one item.  Additionally, method will return the card based on
    position.
    
    @param: position   position in hand list to remove card item.
    @return:   return card object based on the position
    '''
    def remove_card(self, position):
        
        card = self.__hand[position]
        self.__hand.remove(card)
    
        return card
    
    
    '''
    get_cards
    Return the entire hand or list of cards in the hand list
    @param: self
    @return:  self.__hand list
    '''
    def get_cards(self):
        return self.__hand
    
    '''
    clear
    clear, remove, or empty all items in the hand list
    '''
    def clear(self):
        del self.__hand[:]
      
    '''
    get_number_of_cards
    @param: self
    @return: int length of the number of items in the Hand list
    '''
    def get_number_of_cards(self):
        return len(self.__hand)
        
    '''
    This will be the abstract calculate_payout function to determine the 
    specific hand payout based on the bet and hand type.
    The payout could positive or negative.....
    
    TO DO:
    I WILL MAKE THIS A VIRTUAL LATER!!  NOW I AM JUST PUTTING IN THE BOILERPLATE
    '''
    def calculate_payout(bet):
        pass
    
    '''
    This was done to make the Card class iterable
    '''
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
        
## Unit Test of the Hand Class ####
def main():
    
    from Hand import Hand
    
    a = [1,2,3,1,2,3,4]
    print "Length of LIST A is:\t{}".format(len(a))
    print "Item at position 0:\t{}\n".format(a[0])
    
    b = a[0]
    
    a.remove(b)
    
    print "Updated Length of LIST A is:\t{}".format(len(a))
    print "Print the new list:\t{}\n".format(a)
    
    card1 = Card("Clubs", "6")
    card2 = Card("Diamonds", "6")
    card3 = Card("Hearts", "6")
    card4 = Card("Spades", "6")
    card5 = Card("Clubs", "10")
    
    hand = Hand()
    hand.add_card(card1)
    hand.add_card(card2)
    hand.add_card(card3)
    hand.add_card(card4)
    hand.add_card(card5)
    
    print "Number of cards in the Hand LIST:\t{}\n".format(hand.get_number_of_cards())
    
    card = hand.remove_card(2)
    card.print_card()
    
    print "Updated Number of cards in the Hand LIST:\t{}\n".format(hand.get_number_of_cards())
    
    hand.clear()
    print "Updated Number of cards in the Hand LIST:\t{}\n".format(hand.get_number_of_cards())
    
            
if __name__ == '__main__':
    main()