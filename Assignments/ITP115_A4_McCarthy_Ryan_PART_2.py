# Ryan McCarthy, rbmccart@usc.edu
# ITP 115, Fall 2020
# Assignment 4
# Description:
# Part 2 is a die game where the user has no control over inputs, but may win a game with a 20 sided die
# the die is rolled 10 times with a new winning case for each roll
# the users score is tallied and returned at the end

import random

print("PART 2 - D20 Dice Game\n")
# assigning starting score to zero
score = 0
# here is the for loop that iterates through the game 10 times
for x in range(10):
    # variables to be printed many times... for conciseness
    success = "You won 50 points. Yay!"
    failure = "You didn't win this time."
    # randomly selecting a case and rolling the die
    case = random.randrange(1, 6)
    roll = random.randrange(1, 21)
    # announcing which case they are playing and playing it through the if else statements
    print("\nYou are playing for CASE " + str(case) + "\nYou will win for the following numbers:")
    if case == 1:
        for i in range(2, 21, 2):
            print(i, end=" ")
        print("\nYou rolled a", roll)
        if roll % 2 == 0:
            print(success)
            score += 50
        else:
            print(failure)
        # for spacing
        print("\n")

    elif case == 2:
        for i in range(1, 20, 2):
            print(i, end=" ")
        print("\nYou rolled a", roll)
        if roll % 2 == 1:
            print(success)
            score += 50
        else:
            print(failure)
        print("\n")

    elif case == 3:
        for i in range(5, 11, 1):
            print(i, end=" ")
        print("\nYou rolled a", roll)
        if roll in range(5, 11):
            print(success)
            score += 50
        else:
            print(failure)
        print("\n")

    elif case == 4:
        for i in range(10, 21, 2):
            print(i, end=" ")
        print("\nYou rolled a", roll)
        if roll in range(10, 21) and roll % 2 == 0:
            print(success)
            score += 50
        else:
            print(failure)
        print("\n")

    elif case == 5:
        for i in range(3, 19, 3):
            print(i, end=" ")
        print("\nYou rolled a", roll)
        if roll % 3 == 0:
            print(success)
            score += 50
        else:
            print(failure)
        print("\n")

print("Your total score is: ", score)
print("Thanks for playing. Come again!")
