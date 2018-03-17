# -*- coding: utf-8 -*-
"""
Created on Sun Mar 04 19:20:24 2018

@author: Ben Brock
"""

def test_var_args(farg, *args):
    print "formal arg:", farg
    for arg in args:
        print "another arg:", arg

test_var_args(1, "two", 3)