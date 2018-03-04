# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 14:32:10 2018

@author: Ben Brock and Shazia Zaman
"""

'''
Class:  PokerGameInterface


TO DO:
This class will be cleaned up tremendously.   The is the presentation class
for the Poker game.  This is where we will use all kinds of data visualizations
to make the Poker game user friendly for the poker players.
'''
from Poker import Poker
import sys

class PokerGameInterface (object):
    
    '''
    Command values
    '''
    SHOW_COMMANDS                                   = 0
    WELCOME_MESSAGE                                 = 1
    START_NEW_GAME_MESSAGE                          = 2
    INSERT_COINS                                    = 3
    DISPLAY_BANKROLL                                = 4
    PLACE_PLAYERS_BET                               = 5
    DISPLAY_PLAYERS_FIVE_CARD_STUD                  = 6
    DEAL                                            = 7
    CASH_OUT                                        = 8
    COINS_REMAINING                                 = 9
    DISPLAY_SUMMARY_OF_INTERPRETATION_OF_POKER_HAND = 10
    QUERY_CARD_0_KEEP_DISCARD                       = 11
    QUERY_CARD_1_KEEP_DISCARD                       = 12
    QUERY_CARD_2_KEEP_DISCARD                       = 13
    QUERY_CARD_3_KEEP_DISCARD                       = 14 
    QUERY_CARD_4_KEEP_DISCARD                       = 15   
    OTHER                                           = 99
    EXIT                                            = -1

    '''
    PokerGameInterface constructor
    The Poker game controller that the interface interacts with Player
    @param: self
    @param: game :  Poker object
    @return: NONE
    '''
    def __init__(self, game):
        self.__game = game
        
        
    '''
    PokerGameInterface destructor
    No needed for this class at this time. Done only for completeness sake.
    @param: self
    @return: NONE
    '''
    def __del__(self):
        pass
        
    '''
    display_welcome
    Displays the welcome screen
    @param: self
    @return: NONE
    '''
    def display_welcome(self):
        print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
        print "                      Welcome to Poker!\n"
        print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
        
    '''
    display_new_game
    Displays a new game
    @param: self
    @return: NONE
    '''
    def display_new_game(self):
        print
        print "*****************************************************************\n"
        print "                       Starting New Poker game!\n"
        print "*****************************************************************\n"
        
        
    '''
    display_players_five_card_stud_hand_table_summary
    Displays the current table for the current player
    @param: self
    @return: NONE
    '''
    def display_players_five_card_stud_hand_table_summary(self):
        #print "\nENTER PokerGameInterface::display_players_five_card_stud_hand_table_summary()\n"
        print 
        print "-----Display players 5 card stud hand table summary ------"
        print 
        #self.__game.get_player().show_hand()
        "Hand:\t{}\n".format(self.__game.get_player().show_hand_by_index())
        print "-----------------------------------------------------------\n"
        print "Positions:\t\t  0 |   1 |   2 |   3 |   4\n\n"
        #print "\nEXIT PokerGameInterface::display_players_five_card_stud_hand_table_summary()\n"
        
        
    '''
    display_winnings
    Displays the amount of coins the player won
    @param: self
    @param: amount: The amount the player won
    @return: NONE
    '''
    def display_winnings(self, amount):
        print ("You won:\t{} coins!\n".format(amount))
        
        
    '''
    display_bank_roll
    Displays the player's current bankroll
    @param: self
    @param: amount: The amount the player won
    @return: NONE
    '''
    def display_bank_roll(self):
        print "Bankroll:\t{} coins\n\n".format(self.__game.get_player_funds())
    
    
    '''
    display_action_result
    Displays the result of the player's action
    @param: self
    @param: result: Information that pertains to the player's actions
    @return: NONE
    '''
    def display_action_result(self, result):
        print "{}\n".format(result)
    
    
    '''
    get_deposit
    Gets the player's deposit
    A player deposits an arbitrary number of coins into the machine.
    - Each coin has equal value.
    - The number of coins deposited is the player's bankroll
    
    NOTE:  
    The player does not have to increase his number of coins when playing poker
    @param: self
    @return: int : The amount that the player would like to deposit
    '''
    def get_deposit(self):
        
        '''
        https://stackoverflow.com/questions/19440952/how-do-i-check-if-raw-input-is-integer-in-python-2-7
        https://stackoverflow.com/questions/3501382/checking-whether-a-variable-is-an-integer-or-not
        '''
        ## Read raw input from the key board via ~ Python 2.7 Style
        deposit_amount = raw_input("Type in the number of coins you would like to deposit: ")
        
        '''
        Validate that the deposit_amount is a valid digit.
        Here it is ok, for the deposit_amount to be =0 or more. 
        '''
        if deposit_amount.isdigit() == True:
            #print "This is a number:\t{}".format(deposit_amount)
            return deposit_amount
        else:
            print "This is not a valid number\t{}\n".format(deposit_amount)
            return self.get_deposit()
            
        
    
    
    '''
    get_bet
    Gets the player's bet

    Valid Bet Amount:  1:5 or 1, 2, 3, 4, 5
    @param: self
    @return: int : The amount that the player would like to bet
    '''
    def get_bet(self):

        #self.display_bank_roll()
        
        ## Read raw input from the key board via ~ Python 2.7 Style
        bet_amount = raw_input("Type in the amount you would like to bet (1-5): ")
        if bet_amount.isdigit() == True and int(bet_amount) in range(1,6):
            #print("Valid Range Entered.")
            return bet_amount
        else:
            print("Invalid Range Entered! Please be more careful and re-enter a valid range.")
            return self.get_bet()
    
        
    
    '''
    get_action
    Gets the player's action

    Valid Actions:  'k' or 'd'
    
    TO DO:
    From a Pythonic point of view, must make sure that the indices are correctly
    handled when removing items from the list based on the card position.
    Note: This is 0-based for the 1st position in the list and so on.
    
    @param: index: Index of the card to keep or discard
    @return: string : The action that the player would like to perform  ==> 'k' or 'd'
    '''
    def get_action(self, index):
    
        ## Read raw input from the key board via ~ Python 2.7 Style
        action = raw_input("Would you like to 'k' (keep) or 'd' (discard) the card at position\t{}   ".format(index) )
        if action.isalpha() and str(action) in ['k', 'd']:
            #print("Valid selection. You selected action:\t{}".format(action))
            return action
        else:
            print("Invalid Action Entered! Please be more careful and re-enter a valid action.")
            return self.get_action(index)
            
        
    
    '''
    get_end_of_game_action
    Get the player's action for the end of a game
    
    Valid actions: 'Continue', 'Deposit', or 'Quit'

    @param: self
    @return: string : The action that the player would like to perform
    '''
    def get_end_of_game_action(self):
        
        ## Read raw input from the key board via ~ Python 2.7 Style
        action = raw_input("Would you like to 'continue', 'deposit', or 'quit':  ")
        if action.isalpha() and str(action) in ['continue', 'deposit', 'quit']:
            #print("Valid selection. You selected action:\t{}".format(action))
            return action.lower()
        else:
            print("Invalid Action Entered! Please be more careful and re-enter a valid action.")
            return self.get_end_of_game_action()
            
        
    
    '''
    get_game
    Get the Poker Game object

    @param: self
    @return: Poker Game object
    '''
    def get_game(self):
        return self.__game
        
'''
Dummy methods.  Not needed.  Only used to create skeleton for the class methods.
'''
def checker():
  inputt = raw_input("how many u want to check?")
  try:
      return int(inputt)
      
  except ValueError:
      print "Error!, pls enter int!"
      return checker()


def checkerv1():
    test = raw_input("Enter some text here: ")
    if test.isdigit() == True:
        print("This is a number.")
        return test
    else:
        print("This is not a number.")
        return checkerv1()

def checker_range():
    bet_amount = raw_input("Type in the amount you would like to bet (1-5): ")
    if bet_amount.isdigit() == True and int(bet_amount) in range(1,6):
        #print("Valid Range Entered.")
        return bet_amount
    else:
        print("Invalid Range Entered! Please be more careful and re-enter a valid range.")
        return checker_range()
    
    
def checker_action(index):
    action = raw_input("Would you like to 'k' (keep) or 'd' (discard) the card at position\t{}   ".format(index) )
    #if action.isalpha() and str(action) in range('k', 'd'):
    if action.isalpha() and str(action) in ['k', 'd']:
        print("Valid selection. You selected action:\t{}".format(action))
        return action
    else:
        print("Invalid Action Entered! Please be more careful and re-enter a valid action.")
        return checker_action(index)
        
def checker_game_continue():
    action = raw_input("Would you like to 'continue', 'deposit', or 'quit':  ")
    
    if action.isalpha() and str(action) in ['continue', 'deposit', 'quit']:
        print("Valid selection. You selected action:\t{}".format(action))
        return action
    else:
        print("Invalid Action Entered! Please be more careful and re-enter a valid action.")
        return checker_game_continue()
        
## Unit Test of the PokerGameInterface Class ####
def main():
    
    print "\nUnit Testing of the PokerGameInterface Class.....\n"
    
    print "\n.... This is where most of the Poker Game Interface logic will be located for the Poker Game presentation...\n"
    
    from PokerGameInterface import PokerGameInterface
    from Player import Player
    from Deck import Deck
    
    '''
    Scenario 1:
    Test PokerGameInterface class with Player without any HAND object
    
    Execute all of the methods in the PokerGameInterface class to insure 
    that we have no errors.
    '''
    # create a poker game "controller"
    game = Poker()
    
    # add a 'view' to the "controller"
    game_view = PokerGameInterface(game)
    
    
    print "\nNow Going Thru Scenario 1\n"
    '''
    Add  player Joe without a HAND to the PokerGame
    '''
    player_joe = Player("joe")
    print "\n...Adding Player Joe hand to the poker game via 'game.add_player() method .....\n"
    game.add_player(player_joe)
    
    print "The number of cards in the deck of cards:\t{}".format(game.get_deck().get_deck_size())
    
    game.add_view(game_view)
    
    game_view.display_welcome()
    
    game_view.display_new_game()
    
    game_view.display_players_five_card_stud_hand_table_summary()
    
    
    game_view.display_winnings (450)
    
    game_view.display_bank_roll()
    
    result = 1000
    game_view.display_action_result(result)
    
    deposit_amount = game_view.get_deposit()
    
    print "Players Deposit Amount:\t{}\n".format(deposit_amount)
    
    bet_amount = game_view.get_bet()
    
    print "Players Bet Amount:\t{}\n".format(bet_amount)
    
    index = 0
    action = game_view.get_action(index)
    
    print "Players Action 'Keep' or 'Discard':\t{}\n".format(action)
    
    action = game_view.get_end_of_game_action()
    
    print "Players Action 'continue', 'deposit', or 'quit':\t{}\n".format(action)
    
    #sys.exit(2)
    
    
    '''
    Scenario 2:
    Test PokerGameInterface class with Player with HAND object or a valid
    set of 5 cards.
    
    Re-execute all of the methods in the PokerGameInterface class to insure 
    that we have no errors.
    
    This scenario will mimic a one poker hand being played.  This is done to 
    flush out the bugs and make sure the application is properly working as 
    intended.
    '''
    print "\nNow Going Thru Scenario 2\n"
    bob = Player("bob")
    print "Players name:\t{}\n".format(bob.get_name())
    
    #deck = Deck()
    #deck.shuffle()
    
    print "The number of cards in the deck of cards:\t{}".format(game.get_deck().get_deck_size())
    
    #sys.exit(2)
    
    '''
    Add a player to the PokerGame
    '''
    print "\n...Adding Bob hand to the poker game via 'game.add_player() method .....\n"
    game.add_player(bob)
    
    game_view.display_welcome()
    
    # Ask the player to add funds
    deposit_amount = game_view.get_deposit();
    game.get_player().add_funds(deposit_amount);
    
    game_view.display_new_game()
    game_view.display_bank_roll()
    
    bet_amount = game_view.get_bet()
    
    for i in range(0, 5):
        game.get_player().add_card(game.get_deck().draw_card())
        
    '''
    List Comprehension
    The above command is coded up in the Pythonic way listed below.
    '''
    #[game.get_player().add_card(game.get_deck().draw_card()) for i in range(0, 5)]
        
    game_view.display_players_five_card_stud_hand_table_summary()
            
    print "The number of cards in the deck of cards:\t{}".format(game.get_deck().get_deck_size())
    
    # Card Position Keep/Delete Card Management
    game.player_card_keep_delete_position_management()
    
    game_view.display_players_five_card_stud_hand_table_summary()
            
    print "The number of cards in the deck of cards:\t{}".format(game.get_deck().get_deck_size())
    
    print "\nCONVERTED HAND LIST IS {}".format(game.get_poker_hand_utility().get_converted_current_hand_list())
    print "CONVERTED HAND STRING IS {}\n".format(game.get_poker_hand_utility().get_converted_current_hand_string())

    cards = game.get_poker_hand_utility().get_converted_current_hand_string()

    cmd = game.evaluate_hand(bet_amount)
    
    print("%-18r %-15s %r" % (cards, cmd.getCommandName(), cmd.getTieBreaker()))
    
    print "\nPAYOUT is {}".format(cmd.calculate_payout())
    
if __name__ == '__main__':
    main()
    