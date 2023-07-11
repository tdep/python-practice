"""
  Write a program to find out how often a streak of six heads or a 
  streak of six tails comes up in a randomly generated list of heads
  and tails. Your program breaks up the experiment into two parts:
    - The first part generates a list of randomly selected 'heads' and 
      'tails' values.
    - The second part checks if there is a streak in it.
  Put all of this code in a loop that repeats the experiment 10,000 times
  so we can find out what percentage of the coin flips contains a streak of 
  six heads or tails in a row.

  As a hint, the function call random.randint(0,1) will return a 0 value 50%
  of the time and a 1 value the other 50% of the time.
"""

import random

numberOfStreaks = 0

for experimentNumber in range(10000):
    heads = 0
    tails = 0
    flips = []
    while len(flips) < 100:
        flips.append(random.randint(0,1))

    for side in flips:
        if side == 0:
            if tails != 6:
                tails += 1
            elif tails == 6:
                numberOfStreaks += 1
                tails = 0
        else:
            if heads != 6:
                heads += 1
            elif heads == 6:
                numberOfStreaks += 1
                heads = 0
    

print('Chance of streak: %s%%' % (numberOfStreaks / 10000))