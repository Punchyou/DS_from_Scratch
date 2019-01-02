# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 20:47:42 2019

@author: maria_p
"""
"""Conditionl Probabilities."""

"""A family with two unknown children."""
from random import choice, seed
def random_kid():
    return choice(["boy", "girl"])

both_girls = 0
older_girl = 0
either_girl = 0

seed(5) # seed() returns a different sequence of values

for _ in range(10000):
    younger = random_kid()
    older = random_kid()
    if older == "girl":
        older_girl += 1
    if older == "girl" and younger == "girl":
        both_girls += 1
    if older == "girl" or younger == "girl":
        either_girl += 1
print("P(both | older): ", both_girls / older_girl)
print("P(both | either: ", both_girls / either_girl)