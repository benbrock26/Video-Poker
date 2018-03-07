# -*- coding: utf-8 -*-
"""
Created on Wed Mar 07 08:02:59 2018

@author: Ben Brock
"""

from Poker import Poker
from PokerGameInterface import PokerGameInterface

'''
The main function to start the Poker Game.
'''           
def main():

    # create a poker game "controller"
    poker = Poker()
    
    # add a 'view' to the "controller"
    poker_game_interface = PokerGameInterface(poker)
    
    # connect the poker object and PokerGameInterface for messaging
    poker.add_view(poker_game_interface)
    
    # Start the poker game simulation
    poker.play()
    
if __name__ == '__main__':
    main()

