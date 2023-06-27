###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

def correct(d, g):
    if d[0] == g[0] and d[1] == g[1] and d[2] == g[2]:
        return True
    else:
        return False
    
def match(num, guess):
    if num[0] == guess[0] or num[1] == guess[1] or num[2] == guess[2]:
        return True
    else:
        return False
    
def close(num, guess):
    if num[0] == guess[1] or num[0] == guess[2] or num[1] == guess[0] or num[1] == guess[2] or num[2] == guess[0] or num[2] == guess[1]:
        return True
    else:
        return False

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
import random
digit = list(range(10))
random.shuffle(digit)
d = digit[:3]

# Another hint:
while True:
    g = input("What is your guess? ")
    guess = [int(x) for x in str(g)]

    # Think about how you will compare the input to the random number, what format
    # should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!

    if correct(d, guess):
        print("Correct guess! You have won!")
        break
    elif match(d, guess):
        print("Match! You've guessed a correct number in the correct position!")
    elif close(d, guess):
        print("Close! You've guessed a correct number but in the wrong position!")
    else:
        print("Nope! You haven't guess any of the numbers correctly!")