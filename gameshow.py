#!/usr/bin/python3
# Adam Evans
# Game Show Simulator

import sys
import shlex
import codecs
import random

class door():    
    isPrize = False
class game():
    door1 = door()
    door2 = door()
    door3 = door()
    doors = [door1, door2, door3]
    prizedoor = random.randint(0,2)
    doors[prizedoor].isPrize = True;


# cmdline format: ./gameshow.py <# of rounds>
if len(sys.argv) != 2:
    print("Usage: ./gameshow.py <number of rounds>\ni.e. ./gameshow 100")
    exit(1)
rounds = sys.argv[1]
swapWins = 0
stayWins = 0

for x in range(int(rounds)): 
    myGame = game()
    # Choose a door randomly
    chosenDoor = myGame.doors[random.randint(0,2)]
    #myGame.doors.Remove(chosenDoor)
    # Remove a door that is not chosen or a prize 
    # ^^ No need to actually program this in unless you have more than 3 doors:
    # The host always removes a door that doesn't have a prize. One door is yours,
    # the other is not your door. Either your door has the prize or it doesn't and
    # you should have swapped.

    # If door chosen is prize, stayWins++ Else, swapWins++
    if (chosenDoor.isPrize): stayWins += 1
    else: swapWins += 1
stayRate = float(stayWins) / float(rounds)
swapRate = float(swapWins) / float(rounds)
print(f"=== Rounds: {rounds} ===")
print(f"Wins if Stay: {stayWins} (Rate: {stayRate})")
print(f"Wins if Swap: {swapWins} (Rate: {swapRate})")