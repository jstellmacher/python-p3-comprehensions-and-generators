#!/usr/bin/env python3
import sys
# ! [!!!!!!!!!!!!!!!!!!!!!!!!!!! evens num_list n for n in num_list if n %2 == 0 then return even_list !!!!!!!!!!!!!!!!!! for loop n for n !! as it iterates over n the number list 1%2=1 2%2=0 3%2=1 4%2=0 5%2=1 6%2=0 modulo division (returns remain of two numbers) Below if the remainder is 0 then we know it divides evenly !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ctrl D cancels the python command]
# return_evens([0, 1, 3, 5, 7, 8, 9])

def return_evens(num_list):
    even_list = [n for n in num_list if n % 2 == 0]
    return even_list
    
# ![!!!!!!!!!!!!!!!!!!!!!!!  !!!!!!!!!!!!!!!!]
# make_exclamation(["Hello", "I'm doing great", "Python is fun"])
# ["Hello!", "I'm doing great!", "Python is fun!"]
def make_exclamation(sentence_list):
    exclamation_list = [s + "!" for s in sentence_list]
    return exclamation_list
    