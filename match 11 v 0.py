# This is our cool card game *** Match-11 ***
# L, B and J, Jun 2020
#

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

    # input the player's choices

    # check if they made a match

    # go on to the next player
    nextplayer += 1

    # End of game loop. Continue with another round of turns.

# game finished so say goodbye
print("Game finished, hope you enjoyed it! Play again soon.")