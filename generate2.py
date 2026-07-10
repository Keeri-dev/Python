#import random
#
#coin = random.choice(["heads", "tails"])
#print(coin)

#### Instead of using import random and getting all function switch to for...call just choice

#from random import choice
#
#coin = choice(["heads", "tails"])
#print(coin)

### alternative import Could be helpful for ..if you want to have a just choice variable.
### Also cleans up the code

#### Now random.randint(a,b)... means get a random integer thats between a and b.
### generate random number

#import random
#
#number = random.randint(1, 10)
#print(number)

#### used for randomizing or playing a game

#### Now random.shuffle(x)....means takes a list and shuffles it. random order
## Shuffles the argument in place...doesnt return a value.

import random

cards = ["jack", "queen", "king"]
### Pass in the variable containing our cards
random.shuffle(cards)

### how to print one at a time
for card in cards:
    print(card)
