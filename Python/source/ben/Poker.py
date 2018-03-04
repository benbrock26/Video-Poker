# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 21:58:28 2018

@author: Ben Brock and Shazia Zaman
"""

from Deck import Deck
from Player import Player
from PokerGameTheoryStrategy import PokerGameTheoryStrategy
from PokerHandUtility import PokerHandUtility
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
        self.__poker_game_theory_strategy   = PokerGameTheoryStrategy()  # Nash Equilibrium Game Theory
        self.__poker_hand_utility = PokerHandUtility()   # Poker Hand Utility object which evaluates any 5 card hand
    
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
    
    def evaluate_hand(self, bet_amount):
    
        if self.__poker_game_theory_strategy:
            
            # get the current card hand in string format
            cards = self.__poker_hand_utility.get_converted_current_hand_string()
            
            # Now, call the poker hand utility class to evaluate the current hand
            rank_result = self.__poker_hand_utility.rank(cards, bet_amount)
            return rank_result

        
    def reset_table(self):
        pass
    
    def get_play_game(self):
        return self.__play_game
    
    def get_player(self):
        return self.__player
    
    def get_game_view(self):
        return self.game_view
    
    def get_poker_hand_utility(self):
        return self.__poker_hand_utility
    
    
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
            
            
            if self.__number_of_replacement_cards > 0:
                
                # removed the player's requested cards from the player's current hand
                self.remove_cards_from_hand()
                
                # add new random card or cards to the players hand
                self.add_new_cards_to_hand()
                
                # Update poker game player user experience or hand summary
                self.__game_view.display_players_five_card_stud_hand_table_summary()
                
                self.__poker_hand_utility.set_poker_hand(self.__player.get_hand().get_cards())
              
                '''
                Based on the "n" cards that were discarded by the user, 
                Now must add the "n" card random cards back to the deck of cards to replace the cards removed.
                ==> Will not have duplicate cards in the deck.
                '''
                # add the discarded cars back to the Deck
                self.add_discarded_cards_back_to_deck()
                
            #elif self.__number_of_replacement_cards == 0:
            else:
                self.__poker_hand_utility.set_poker_hand(self.__player.get_hand().get_cards())
            
                
                    
        else:
            print "CANNOT KEEP OR DISCARD MANAGEMENT OF PLAYERS' HAND ==> PLAYERS HAND IS EMPTY NO CARDS ARE IN THE HAND\n"
            
        
    def add_new_cards_to_hand(self):
        
        #[ self.__player.get_hand().add_card(self.__deck.draw_card()) for index in range(0, self.__number_of_replacement_cards) ]
        
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
    
    from HandCommandPattern import HandCommandPattern
    #from PokerHandUtility import PokerHandUtility
    #from PokerCommands import RoyalFlushCommand
    
    print "\nUnit Testing of the Poker Class.....\n"
    
    print "\n.... This is where most of the complex logic will be located for the Poker Game...\n"
       
    print "\nUnit Testing of the PokerGameInterface Class.....\n"
    
    print "\n.... This is where most of the Poker Game Interface logic will be located for the Poker Game presentation...\n"
    
    from PokerGameInterface import PokerGameInterface
    
    # create a poker game "controller"
    poker = Poker()
    
    # add a 'view' to the "controller"
    poker_game_interface = PokerGameInterface(poker)
    
    poker.add_view(poker_game_interface)
    
    print "\nNow Going Thru Scenario 2\n"
    bob = Player("bob")
    print "Players name:\t{}\n".format(bob.get_name())
    
    print "The number of cards in the deck of cards:\t{}".format(poker.get_deck().get_deck_size())
    
    
    '''
    Add a player to the PokerGame
    '''
    print "\n...Adding Bob hand to the poker game via 'game.add_player() method .....\n"
    poker.add_player(bob)
    
    poker_game_interface.display_welcome()
    
    poker_game_interface.display_new_game()
    
    # Ask the player to add funds
    deposit_amount = poker_game_interface.get_deposit();
    poker.get_player().add_funds(deposit_amount);
    
    poker_game_interface.display_new_game()
    poker_game_interface.display_bank_roll()
    
    
    bet_amount = poker_game_interface.get_bet()
    
    
    for i in range(0, 5):
        poker.get_player().add_card(poker.get_deck().draw_card())
    
        
    '''
    List Comprehension
    The above command is coded up in the Pythonic way listed below.
    '''
    
    #[game.get_player().add_card(game.get_deck().draw_card()) for i in range(0, 5)]
        
    poker_game_interface.display_players_five_card_stud_hand_table_summary()
            
    print "The number of cards in the deck of cards:\t{}".format(poker.get_deck().get_deck_size())
    
    # Card Position Keep/Delete Card Management
    poker.player_card_keep_delete_position_management()
    
    hand = poker.get_player_hand()
    #print "POKER HAND {}".format(hand)
    #print "CONVERTED HAND IS {}".format(poker.get_poker_hand_utility().get_hand())
    
    '''
    This is awkward for the user to do this task.  This should be done automatically.
    '''
    #poker.get_poker_hand_utility().convert_hand_to_list()
    #poker.get_poker_hand_utility().convert_hand_to_string()
    
    print "CONVERTED HAND LIST IS {}".format(poker.get_poker_hand_utility().get_converted_current_hand_list())
    print "CONVERTED HAND STRING IS {}".format(poker.get_poker_hand_utility().get_converted_current_hand_string())

   
    cards = poker.get_poker_hand_utility().get_converted_current_hand_string()

    cmd = poker.evaluate_hand(bet_amount)

    
    #print("%-18r %-15s %r" % (cards, r[0], r[1]))
    print("%-18r %-15s %r" % (cards, 
                              cmd.getCommandName(), 
                              cmd.getTieBreaker()))
    
    print "HAND TYPE IS:\t{}:".format(PokerHandUtility.POKER_HAND_COMMAND_NAME[cmd.getCommandName()])
    
    print "\nCALCULATE PAYOUT IS {}".format(cmd.calculate_payout())
    
    '''
    CARD_SUIT = dict(
           Spades   = "s",
           Clubs    = "c",
           Diamonds = "d",
           Hearts   = "h")
  
    ORDERED_RANK = {
            "Ace":"a", 
            "2":2,
            "3":3,
            "4":4,
            "5":5,
            "6":6,
            "7":7,
            "8":8,
            "9":9,
            "10":10,
            "Jack":"j",
            "Queen":"q",
            "King" :"k"}
    
    card_hand = []
    for card in hand.get_cards():
        card.print_card()
        print"{}{}".format(ORDERED_RANK[card.get_rank()], CARD_SUIT[card.get_suit()])
        deal = '{}{}'.format(ORDERED_RANK[card.get_rank()], CARD_SUIT[card.get_suit()])
        card_hand.append(deal)
        
    print card_hand
    '''
    
    '''    
    for key in CARD_SUIT:
        print CARD_SUIT[key]
    
    for key in ORDERED_RANK:
        print ORDERED_RANK[key]
    '''
    
if __name__ == '__main__':
    main()