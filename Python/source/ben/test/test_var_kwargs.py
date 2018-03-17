# -*- coding: utf-8 -*-
"""
Created on Sun Mar 04 19:22:02 2018

@author: Ben Brock
"""

def test_var_kwargs(farg, **kwargs):
    print "formal arg:", farg
    for key in kwargs:
        print "another keyword arg: %s: %s" % (key, kwargs[key])

test_var_kwargs(farg=1, myarg2="two", myarg3=3)