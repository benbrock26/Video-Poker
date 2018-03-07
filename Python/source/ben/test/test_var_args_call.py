# -*- coding: utf-8 -*-
"""
Created on Sun Mar 04 19:23:08 2018

@author: Ben Brock
"""

def test_var_args_call(arg1, arg2, arg3):
    print "arg1:", arg1
    print "arg2:", arg2
    print "arg3:", arg3

args = ("two", 3)
test_var_args_call(1, *args)