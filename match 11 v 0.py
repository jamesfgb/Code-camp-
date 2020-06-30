# This is our cool card game *** Match-11 ***
# L, B and J, Jun 2020

# 30/06/2020 Started - input player names, and show the cards face down

# === SETUP : Python libraries and program settings ===

import random
import time

SUITS = ['Sp', 'Ht', 'Dm', 'Cl']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 25, 100, 500]
SUITS_IN_PACK = 2

# === FUNCTIONS needed throughout the program ===


# === GET THE GAME STARTED ===

# set how many players are in the game
print("Hi there, welcome to Match 11!!")
name = input("What is your name? ")
print("\nHi",name,)
friends = int(input("On this game, you can play against other people. \n"
               "How many friends do you have that want to play? "))
players = friends + 1

print('Lets input their names')
for n in range(1, players):
    print('Player', n + 1, '= ? ', end='')
    name = input() 



# construct the pack of cards
pack = []
for suit in SUITS[0:SUITS_IN_PACK]:
    for rank in RANKS:
        card = {'rank':rank, 'suit':suit}
        pack.append(card)


# shuffle the pack - randomly move cards
for i in range(100):
    cardpos = random.randint(0, len(pack) - 1)
    newpos = random.randint(0, len(pack) - 2)
    card = pack.pop(cardpos)
    pack.insert(0, card)



# === MAIN GAME LOOP ===

nextplayer = 0

while True:
    # start the player's turns

    
    # display the grid of cards

    for n in range(len(pack)):
        print(n, '???',) 
        (pack[n])
        #print(pack[n])

    # input the player's choices

    move = input('Please input your move')
    # check if they made a match

    
    # go on to the next player
    nextplayer += 1

    # End of game loop. Continue with another round of turns.

# game finished so say goodbye
print("Game finished, hope you enjoyed it! Play again soon.") 
