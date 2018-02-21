
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 17:24:16 2018

https://brilliant.org/wiki/programming-blackjack/

https://www.programiz.com/python-programming/examples/shuffle-card

@author: Ben Brock
"""
from colour import Color


import sys


class Card:
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit    # 1,2,3,4 = ♥♦♣♠
        self.color = Color('red')

    def print_card(self):
        #print self.color
        print("┌───────┐")
        print("| {:<2}    |".format(self.value))
        print("|       |")
        print("|   {}   |".format(chr(self.suit+2)))
        print("|   {}   |".format(self.suit))
        print("|       |")
        print("|    {:>2} |".format(self.value))
        print("└───────┘") 
        
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

#following from Python cookbook, #475186
def has_colours(stream):
    if not hasattr(stream, "isatty"):
        return False
    if not stream.isatty():
        return False # auto color only on TTYs
    try:
        import curses
        curses.setupterm()
        return curses.tigetnum("colors") > 2
    except:
        # guess false in case of error
        return False
has_colours = has_colours(sys.stdout)


def printout(text, colour=WHITE):
        if has_colours:
                seq = "\x1b[1;%dm" % (30+colour) + text + "\x1b[0m"
                sys.stdout.write(seq)
        else:
            sys.stdout.write(text)
            
if __name__ == '__main__':
    
    c = Color("blue")
    print c
    
    x = Card('K', 1)
    x.print_card()
    
    x = Card('K', 2)
    x.print_card()
    
    x = Card('K', 3)
    x.print_card()
    
    x = Card('K', 4)
    x.print_card()
    
    #
    # Test
    #
#    printout("[debug]   ", GREEN)
#    print("in green")
#    printout("[warning] ", YELLOW)
#    print("in yellow")
#    printout("[error]   ", RED)
#    print("in red")