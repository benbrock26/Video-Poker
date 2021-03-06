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
        self.__players_current_round_of_poker_hands = []
        self.__player_poker_hand_management_dict = {}     # player poker's hand to player management
        
        # instantiate the objects controlled by the Poker object
        self.__deck = Deck()        ## 1 deck of cards
        self.__player = None        ## 1 player  -- used for testing only
        self.__players = []         ## 1 to many player's -- used in actual code
        self.__game_view = None     ## 1 PokerGameInterface
        self.__player_poker_hands = []  ## history of all player's poker hands played
        self.__poker_game_theory_strategy   = PokerGameTheoryStrategy()  # Nash Equilibrium Game Theory
        self.__poker_hand_utility = PokerHandUtility()   # Poker Hand Utility object which evaluates any 5 card hand
    
    
    
    '''
    decided not to implement the destructor for the Poker class. Let the Python internal destructor free and allocate memory.
    That is much better than just having a pas command!!!
    
    def __del__(self):
        pass
    '''
    
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
        
    def get_players_current_round_of_poker_hands(self):
        return self.__players_current_round_of_poker_hands
    
    def play(self):
    
        # Meet the Browns or get a chance to greet and meet the poker players
        # Query name and amount to put in their bank roll
        self.start_game_get_player_names()
        
        # Let the poker games begin!!!!
        play_game = True
        while play_game == True:
          
            i = 1;
            for player in self.__players:
                print "Player's {} name is {}".format(i, player.get_name())
                
                # display players' bank roll
                self.__game_view.display_player_bank_roll(player)
                
                # query user for the current HAND bet amount and set the bet amount
                self.__get__and_set_current_player_bet(player)
                
                # deal the five card poker hand to the current player
                self.__deal_poker_hand(player)
                
                # display the current players' hand
                self.__game_view.display_current_player_five_card_stud_hand_table_summary(player)
                
                # Current Player HAND Manipulation --- Card Position Keep/Delete Card Management
                self.__current_player_card_keep_delete_position_management(player)
                
                # evaluate the poker hand in poker terminology or terms.
                command = self.evaluate_hand(player.get_bet_amount())
                
                self.__save_players_hand(command, player)
                
                self.__pretty_print_command_results(command)
                
                '''
                #
                # Check each players hand or compare all of the player's hands to see who won the current round
                # Based on the poker hand rule requirements
                # - Royal Flush Hand versus Non-Royal Hands
                #    --> There is a difference between the two when you see who actually won the current poker round
               
                '''
                # Here we are really doing modulus math, that is, 
                # number % len(self.__players)  == 0, indicating we have received all poker hands in the current round
                #
                # poker round is complete when --> (number % len(self.__players)) == 0
                #
                if i == len(self.__players):
                    print "\n\n<<<<<<<< NEED TO COMPARE ALL OF THE POKER PLAYERS HANDS TO SEE WHO WON FOR THE GAME ITERATION <<<<<<<<"
                    
                    # Let's get ready to rumble and see which player won the current of poker
                    self.determine_players_poker_hand_winner()
                    
                    if debug == 1:
                        # print the player poker hand management dictionary to see the active current round of poker players
                        print self.__player_poker_hand_management_dict
                    
                    '''
                    After determining the winner for the players in the game current round of poker hands, you must reset or clear 
                    this variable to get ready for the next poker round
                    '''
                    self.__players_current_round_of_poker_hands = []
                    self.__player_poker_hand_management_dict = {}
                    i = 1
                    
                else:
                    print "\n\n++++++++ NOT READY TO COMPARE ALL OF THE POKER PLAYERS HANDS YET +++++++++"
                    i = i + 1
                
                # query user for continue/deposit/quit action
                play_game = self.__get_continue_deposit_quit_action()
                
                
                # clear bet and hand so you will start fresh the next go around
                player.reset()
                
    
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

    def __pretty_print_command_results(self, command):
        print "\nHAND TYPE IS:\t{}:".format(PokerHandUtility.POKER_HAND_COMMAND_NAME[command.getCommandName()])
        print "\nAMOUNT OF BET:{}".format(command.get_bet_amount())
        print "PAYOUT MULTIPLIER:{}".format(command.get_payout_multiplier())
        print "PAYOUT CALCULATION:{}".format(command.calculate_payout())
        print "\nCALCULATE PAYOUT IS {} for HAND TYPE {}".format(command.calculate_payout(), 
                                                                 PokerHandUtility.POKER_HAND_COMMAND_NAME[command.getCommandName()])
        print "HAND STRING FORMAT: {}".format(command.get_hand_string_format())
        print "TIE BREAKER: {}".format(command.getTieBreaker())
        
        
    def __save_players_hand(self, command, player):
        # save current player's hand
        player.get_poker_hands().append(command)
                
        # save all players hands
        self.__player_poker_hands.append(command)
        
        # save the current round of players poker hands
        self.__players_current_round_of_poker_hands.append(command)
        
        self.__player_poker_hand_management_dict[command] = player
                
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

    
    def add_new_cards_to_current_player_hand(self, player):
        
        #[ self.__player.get_hand().add_card(self.__deck.draw_card()) for index in range(0, self.__number_of_replacement_cards) ]
        
        if debug == 1:
            print
            for index in range(0, self.__number_of_replacement_cards):
                print "MUST ADD NEW CARD: CALL NUMBER: {}".format(index)
            
        for i in range(0, self.__number_of_replacement_cards):
            player.get_hand().add_card(self.__deck.draw_card())
            
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
            
            
    def remove_cards_from_current_player_hand(self, player):
        
        if debug == 1:
            print "\nREMOVE THE FOLLOWING CARDS FROM THE PLAYER's HAND\n"
            
            [ card.print_card()  for card in self.__discard_card_list ]
    
        
            print "\n\nPLAYERS CURRENT HAND -- BFORE --\n\n"
            player.show_hand()
        
            print player.get_hand().get_cards()
        
            print "\n..... DELETE CARDS FROM HAND BASED ON USER's REQUEST ....."
        
        [ player.get_hand().get_cards().remove(card) for card in self.__discard_card_list ]
    
        if debug == 1:
            print "\n\nPLAYERS CURRENT HAND -- AFTER --\n\n"
            player.show_hand()
            
            
            
    def __current_player_card_keep_delete_position_management(self, player):
        
        self.__discard_indices_list = []
        self.__discard_card_list = []
        self.__number_of_replacement_cards = 0
        
        if player.get_hand():
            
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
                        temp_card = player.get_hand().get_cards()[idx]
                        
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
                self.remove_cards_from_current_player_hand(player)
                
                # add new random card or cards to the players hand
                self.add_new_cards_to_current_player_hand(player)
                
                # Update poker game player user experience or hand summary
                self.__game_view.display_current_player_five_card_stud_hand_table_summary(player)
                
                self.__poker_hand_utility.set_poker_hand(player.get_hand().get_cards())
              
                '''
                Based on the "n" cards that were discarded by the user, 
                Now must add the "n" card random cards back to the deck of cards to replace the cards removed.
                ==> Will not have duplicate cards in the deck.
                '''
                # add the discarded cars back to the Deck
                self.add_discarded_cards_back_to_deck()
                
            #elif self.__number_of_replacement_cards == 0:
            else:
                self.__poker_hand_utility.set_poker_hand(player.get_hand().get_cards())
            
                
                    
        else:
            print "CANNOT KEEP OR DISCARD MANAGEMENT OF PLAYERS' HAND ==> PLAYERS HAND IS EMPTY NO CARDS ARE IN THE HAND\n"            
            
            
    '''
    exitCommand
    Allow the customer to exit the Poker Game Simulator.
  
    
    @params:    none
    @return     none
    ''' 
    def exitCommand(self):
        print '\nThank you for your business!\n' 
        
        
    '''
    exitCommand
    Allow the customer to exit the Poker Game Simulator.
  
    
    @params:    none
    @return     none
    ''' 
    def exitAddingPlayerCommand(self):
        print '\nFinished adding players to poker game!\n' 
        
        print "Number of Poker players is {}".format(len(self.__players))
        
        i = 1
        for name in self.__players:
            print "{}: Players Name: {}\tAvailable Funds: {}".format(i, name.get_name(), name.get_funds())
            i = i + 1
    
        
    def start_game_get_player_names(self):
        self.__game_view.display_welcome()

        get_player_names_flag = True
        while get_player_names_flag == True:
        
            action =  self.get_add_player_action() 
            
            if action.isalpha() and str(action) in ['add']:
                #print("Valid selection. You selected action:\t{}".format(action))

                get_player_names_flag = True
       
                # get the players name
                name = self.get_name_action()
                player = Player(name)
                
                # Ask the player to add funds
                deposit_amount = self.__game_view.get_deposit();
                player.add_funds(deposit_amount);
                
                # add player to the players list
                self.__players.append(player)
                
            elif action.isalpha() and str(action) in ['quit']: 
                self.exitAddingPlayerCommand()
                get_player_names_flag = False
        
        if len(self.__players) >= 1:        
            self.__game_view.display_new_game()
        else:
            print "\n\nMUST HAVE AT LEAST ONE POKER PLAYER!"
            print "CURRENTLY, THERE ARE NO POKERS PLAYER'S IN THE GAME"
            self.exitCommand()
            sys.exit()
        
    '''
    get_end_of_game_action
    Get the player's action for the end of a game
    
    Valid actions: 'Continue', 'Deposit', or 'Quit'

    @param: self
    @return: string : The action that the player would like to perform
    '''
    def get_add_player_action(self):
        
        ## Read raw input from the key board via ~ Python 2.7 Style
        action = raw_input("Would you like to 'add' a new player or 'quit':  ")
        if action.isalpha() and str(action) in ['add', 'quit']:
            #print("Valid selection. You selected action:\t{}".format(action))
            return action
        else:
            print("Invalid Action Entered! Please be more careful and re-enter a valid action.")
            return self.get_add_player_action()
    
    
    def get_name_action(self):
        
        ## Read raw input from the key board via ~ Python 2.7 Style
        action = raw_input("Enter the player's name:  ")
        if action.isalpha():
            #print("Valid selection. You selected action:\t{}".format(action))
            return action.lower()
        else:
            print("Invalid Action Entered! Please be more careful and re-enter a valid action.")
            return self.get_name_action()
        
        
    def __get_continue_deposit_quit_action(self):
        
        action =  self.__game_view.get_end_of_game_action() 
        
        if action.isalpha() and str(action) in ['continue', 'deposit']:
            print("Valid selection. You selected action:\t{}".format(action))
            play_game_flag = True
            
        elif action.isalpha() and str(action) in ['quit']: 
            self.exitCommand()
            play_game_flag = False
            
        return play_game_flag
    
    
    def __get__and_set_current_player_bet(self, player):
        
        bet_amount = self.__game_view.get_bet()
        player.set_bet_amount(bet_amount)
        
    
    def __deal_poker_hand(self, player):
        
        # deals 5 random cards for the players' Poker 5 card Hand
        for i in range(0, 5):
            player.add_card(self.get_deck().draw_card())
            
    def determine_players_poker_hand_winner(self):
        
        winner = []
        losers = []
        
        if debug == 1:
            for hand in self.__players_current_round_of_poker_hands:
                print hand
            
        sort_ordered_hands_by_poker_hand_rank = sorted(self.__players_current_round_of_poker_hands, 
                                                       key=lambda command: command.get_rank(), 
                                                       reverse=False)
        
        '''
        we know generically, the winner is located at 
        winner = sort_ordered_hands_by_poker_hand_rank[0]
        
        and the losers are at 
        losers = sort_ordered_hands_by_poker_hand_rank[1:]
        
        we may be using this to make sure we solve this problem correctly when it comes time to deduct the money or pot from
        the losing players.
        
        It was so easy using the sorted function to determine the winners and losers of the poker game so quickly!!
        '''
        winner_command_type, winning_poker_hands = \
                                      self.__poker_hand_utility.determine_the_winning_poker_hand(sort_ordered_hands_by_poker_hand_rank)
                                      
        if winner_command_type == PokerHandUtility.POKER_HAND_COMMAND_NAME["royal_flush"]:
            
            if len(winning_poker_hands) == 1:
                
                winner =  winning_poker_hands[0]
                losers = winning_poker_hands[1:]
                
                '''
                This code should work too!!!
                winner =  sort_ordered_hands_by_poker_hand_rank[0]
                losers = sort_ordered_hands_by_poker_hand_rank[1:]
                '''
                
                print "\n\n **** WINNING COMMAND POKER HAND TYPE IS {} ****".format(winner_command_type)
                print " **** THE NUMBER OF {} WINNERS is {}".format(winner_command_type, len(winning_poker_hands))
                
                print "****  The winner of this round of poker is '{}' with poker hand of a {}".format(self.__player_poker_hand_management_dict[winner].get_name().capitalize(),
                                                                                                       winner.getCommandName())

                
            elif len(winning_poker_hands) > 1:
                print "\n\n **** WINNING COMMAND POKER HAND TYPE IS {} ****".format(winner_command_type)
                print " **** THE NUMBER OF {} WINNERS is {}".format(winner_command_type, len(winning_poker_hands))
                print " **** MUST SPLIT THE WINNING POT BETWEEN ALL OF THE POKER PLAYERS WITH THE ROYAL FLUSH POKER HAND"
                
                
                if debug == 1:
                    for command in winning_poker_hands:
                        print command
                            
                for winner in winning_poker_hands:
                    print "ROYAL FLUSH WINNERS ARE PLAYER NAMED {}".format(self.__player_poker_hand_management_dict[winner].get_name().capitalize())
                    
                    
        elif winner_command_type != PokerHandUtility.POKER_HAND_COMMAND_NAME["royal_flush"]:
            print "\n\nLet's Get Ready to Rumble!!!\n\n"
            print "WINNING POKER HAND IS {}".format(winner_command_type)
            print "NUMBER OF WINNING POKER HANDS in the CURRENT ROUND is {}".format(len(winning_poker_hands))
            
            if debug == 1:
                for command in winning_poker_hands:
                    print command
            
            print "\n\nLet investigate the list of poker hands named {}".format(winner_command_type) 
            
            # Determine the winning NON-Royal Flush Hand in the current round of poker player's
            winner = self.__poker_hand_utility.determine_the_winning_poker_non_royal_flush_hand(winner_command_type, winning_poker_hands)
            
            ## Need to determine the losers quickly on the fly.
            ## This should be easy!!!
            
            #print "\n\n ***** Let's see who won!!!  *********"
            print "****  The winner of this round of poker is '{}' with poker hand of a {} with a total poker hand of cards with a value of {}".format(self.__player_poker_hand_management_dict[winner].get_name().capitalize(),
                                                                                                                                                       winner.getCommandName(),
                                                                                                                                                       winner.getTotalPokerHandCardValue())
            #print "PLAYER's NAME: {}".format(self.__player_poker_hand_management_dict[winner].get_name())
        

                                          
                                      

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
    
    
    # deals 5 random cards for the players' Poker 5 card Hand
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
    
    #print "CONVERTED HAND LIST IS {}".format(poker.get_poker_hand_utility().get_converted_current_hand_list())
    #print "CONVERTED HAND STRING IS {}".format(poker.get_poker_hand_utility().get_converted_current_hand_string())

   
    cards = poker.get_poker_hand_utility().get_converted_current_hand_string()

    cmd = poker.evaluate_hand(bet_amount)

    
    #print("%-18r %-15s %r" % (cards, r[0], r[1]))
    print("%-18r %-15s %r" % (cards, 
                              cmd.getCommandName(), 
                              cmd.getTieBreaker()))
    
    print "\nHAND TYPE IS:\t{}:".format(PokerHandUtility.POKER_HAND_COMMAND_NAME[cmd.getCommandName()])
    
    
    print "\nAMOUNT OF BET:{}".format(cmd.get_bet_amount())
    print "PAYOUT MULTIPLIER:{}".format(cmd.get_payout_multiplier())
    print "PAYOUT CALCULATION:{}".format(cmd.calculate_payout())
    print "TOTAL POKER HAND VALUE OF ORDINAL CARDS:\t{}".format(cmd.getTotalPokerHandCardValue())
    print "\nCALCULATE PAYOUT IS {} for HAND TYPE {}".format(cmd.calculate_payout(), 
                                                             PokerHandUtility.POKER_HAND_COMMAND_NAME[cmd.getCommandName()])
    
    ## Store the Poker Hand on the Players' list
    poker.get_player().add_hand_to_list_of_players_hands(cmd)
    
    print "\nNUMBER OF HANDS IN THE PLAYERS HISTORY OF COMMANDS:\t{}".format(poker.get_player().get_list_of_players_hands_size())
    
    winnings = cmd.calculate_payout()
    
    poker.get_player().add_funds(winnings)
    
    poker_game_interface.display_winnings(winnings)
    poker_game_interface.display_bank_roll()
    
    #poker.play()
    
    '''
    gameView->displayWinnings(winnings);
            gameView->displayBankroll();
    '''
    
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