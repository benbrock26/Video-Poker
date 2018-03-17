# -*- coding: utf-8 -*-
"""
Created on Sun Mar 04 19:24:13 2018

@author: Ben Brock
"""

def test_var_args_call_1(arg1, arg2, arg3):
    print "arg1:", arg1
    print "arg2:", arg2
    print "arg3:", arg3

kwargs = {"arg3": 3, "arg2": "two"}
test_var_args_call_1(1, **kwargs)


def print_everything(*args):
    for count, thing in enumerate(args):
        print( '{0}. {1}'.format(count, thing))
        
print_everything('apple', 'banana', 'cabbage')


def table_things(**kwargs):
    for name, value in kwargs.items():
        print( '{0} = {1}'.format(name, value))
        
table_things(apple = 'fruit', cabbage = 'vegetable')


def print_values(**kwargs):
    for key, value in kwargs.items():
        print("The value of {} is {}".format(key, value))

print_values(my_name="thor", your_name="hulk")