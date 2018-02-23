# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 19:48:55 2018

@author: Ben Brock
"""


'''
Will not have duplicate cards in the deck.
'''
def checker_action(index):
    action = raw_input("Would you like to 'k' (keep) or 'd' (discard) the card at position\t{}   ".format(index) )
    #if action.isalpha() and str(action) in range('k', 'd'):
    if action.isalpha() and str(action) in ['k', 'd']:
        print("Valid selection. You selected action:\t{}".format(action))
        return action
    else:
        print("Invalid Action Entered! Please be more careful and re-enter a valid action.")
        return checker_action(index)
    
## Unit Test of the Player Class ####
def main():
    
    discard_indices_list = []
    discard_card_list = []
    
    card_list = [ 1, 2, 3, 4, 5]
    number_of_replacement_cards = 0

    #print card_list[0]
    
    for idx in range(0, 5):
        #print card_list[idx]
        action = checker_action(idx)
        
        if action in ['k', 'd']:
            
            if action == 'k':
                print "ACTION is {}\n".format(action)
            elif action == 'd':
                print "ACTION is {}\n".format(action)
                
                # add index to discard_indics
                discard_indices_list.append(idx)
                
                # get the value to be removed the card list
                temp = card_list[idx]
                
                discard_card_list.append(temp)
                
                number_of_replacement_cards = number_of_replacement_cards + 1
                
                # remove the value from card list
                #card_list.remove(temp)
                
 
    if discard_indices_list:
        print "\nDISCARD POSITION LIST is {}\n".format(discard_indices_list)
    else:
        print "\nDISCARD POSITION LIST IS EMPTY\n"
        
    if discard_card_list:
        print "\nDISCARD CARD LIST is {}\n".format(discard_card_list)
    else:
        print "\nDISCARD CARD LIST IS EMPTY\n"
        

    ## REMOVE ITEMS FROM CARD_LIST  ####
    if discard_card_list:
        #for idx in discard_card_list:
        #    print idx
        #    card_list.remove(idx)
            
        [card_list.remove(idx) for idx in discard_card_list]
        
    if card_list:
        print "\nUPDATED CARD LIST is {}\n".format(card_list)
    else:
        print "\nCARD CARD LIST IS EMPTY\n"
        
        
    '''
    Based on the "n" cards that were discarded by the user, 
    Now must add the "n" card random cards back to the deck of cards to replace the cards removed.
    ==> Will not have duplicate cards in the deck.
    '''
    print "Number of Replacement Cards:\t{}".format(number_of_replacement_cards)
    
    
    '''
    Based on the "n" cards that were discarded by the user, 
    Now must add the "n" card random cards back to the deck of cards to replace the cards removed.
    '''
        
if __name__ == '__main__':
    main()