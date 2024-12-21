'''
GO2COD PYTHON PROGRAMMING INTERNSHIP
TASK 01 : A NUMBER GUESSING AI
NAME: SHIV BHAVSAR

This program will generate a random number between 0 and 100 and
then it will ask the user to guess the number until the user guesses it correctly and
it will also display the no. of attempts taken to guess the number correctly at the end.

'''

import random

# generate a random number
number = random.randint(0,100)
count = 0

# prompt the user to guess the number
guess = int(input("Enter your guess between 0 and 100: "))

# input validation and error message
if (guess<0) or (guess>100):
    print("ERROR: Enter your guess between 0 and 100: ")
    guess = int(input("Enter your guess: "))

# loop to keep game running until user guess the number correctly    
while(guess != number):

    # display message about whether the guess is too high or too low
    if (guess < number):
        print("Your guess is too low.")
        print(" ")
    
    elif (guess > number):
        print("Your guess is too high.")
        print(" ")

    # prompt the user to reguess the number if previous guess was incorrect    
    guess = int(input("Enter your guess: "))
    if (guess<0) or (guess>100):
        print("ERROR: Enter your guess between 0 and 100: ")
        guess = int(input("Enter your guess: "))
        # do not count the attempt if guess is out of range
        count -+ 1

    # accumulate the 'count' to count no. of attempts    
    count += 1

# display message if the guess is correct
if (guess == number):
    print(" ")
    print("Great! You guessed is correct.")
    print("No. of attempts to guess the number correctly: ",(count+1))
