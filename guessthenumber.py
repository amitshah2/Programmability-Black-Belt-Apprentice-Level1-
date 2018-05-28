# This is a guess the number assignment.

import random

guessTaken = 0

number = random.randint(1,10)
print('I am thinking of a number between 1 and 10.')

while guessTaken < 5:
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    guessTaken = guessTaken + 1

    if guess < number:
        print('Your guess is too low.')

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break
    
if guess == number:
    guessTaken = str(guessTaken)
    print('Correct.')

if guess != number:
    number = str(number)
    print ('No. The number I was thinking of was ' + number)
    
