'''
Created on Sep 22, 2022

@author: mireia
'''

import argparse

parser = argparse.ArgumentParser() #create an ArgumentParser object 

parser.add_argument("a") #add arguments to the object
parser.add_argument("b")
parser.add_argument("operation")

args = parser.parse_args() #takes arguments and invoke appropriate action

variables = vars(args) #vars() method returns the __dict__ (dictionary mapping) attribute of the given object.

print(variables)


