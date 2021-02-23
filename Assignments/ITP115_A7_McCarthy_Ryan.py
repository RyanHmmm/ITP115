# Ryan McCarthy, rbmccart@usc.edu
# ITP 115, Fall 2020
# Assignment 6
# Description:
# this program allows the user to play rock, paper, scissors against a computer (my program)

# random
import random
# display menu function
def displayMenu():
    print("\nWelcome! Let's play rock, paper, scissors.")
    print("The rules of the game are:\nRock smashes scissors\nScissors cut paper\nPaper covers rock")
    print("If both the choices are the same, it's a tie")

# computer choice function
def getComputerChoice():
    c_choice = random.randrange(3)
    return c_choice
# user choice function
def getUserChoice():
    p_choice = int(input("Please choose (0) for rock, (1) for paper or (2) for scissors: "))
    # forces user to give valid input, this is for improved error handling
    while p_choice not in [0, 1, 2]:
        p_choice = int(input("Please choose (0) for rock, (1) for paper or (2) for scissors: "))
    return p_choice
# will determine who won based on the inputs and return the winner in the form of an integer
def playRound(c_choice, p_choice):
    # if statements covering all game possibilities
    if c_choice == 0 and p_choice == 2:
        return -1
    elif c_choice == 0 and p_choice == 1:
        return 1
    elif c_choice == 1 and p_choice == 0:
        return -1
    elif c_choice == 1 and p_choice == 2:
        return 1
    elif c_choice == 2 and p_choice == 0:
        return 1
    elif c_choice == 2 and p_choice == 1:
        return -1
    else:
        return 0
# function that controls if the game will continue
def continueGame():
    cont = input("Would you like to continue (y/n): ").lower()
    # again, some imporved error handling so program is more user friendly
    while cont not in ["y", "n"]:
        cont = input("Would you like to continue (y/n): ").lower()
    if cont == "y":
        return True
    else:
        return False
# main function that runs the entire game as instructed
def main():
    # scores to be displayed at the end
    c_score = 0
    u_score = 0
    t_score = 0
    # predetermined output for continueGame() for first iteration
    cont = True
    # while loop controlling game
    while cont:
        # display the menu and get the choices
        displayMenu()
        uchoice = getUserChoice()
        cchoice = getComputerChoice()
        # find the choice in terms of words form the number
        if uchoice == 0:
            ushow = "Rock"
        elif uchoice == 1:
            ushow = "Paper"
        else:
            ushow = "Scissors"

        if cchoice == 0:
            cshow = "Rock"
        elif cchoice == 1:
            cshow = "Paper"
        else:
            cshow = "Scissors"
        # sets result
        result = playRound(cchoice, uchoice)
        # shows user the respective choices
        print("You chose", ushow)
        print("The computer chose", cshow)
        # tallies scores based on winner or a tie
        if result == 1:
            print(ushow, "beats", cshow, "- You win!")
            u_score += 1
        elif result == -1:
            print(cshow, "beats", ushow, "- The computer won :(.")
            c_score += 1
        else:
            print("Tie!")
            t_score += 1
        # continue the game?
        cont = continueGame()
    # printing the final scores for this play
    print("\nYou won", u_score, "game(s).")
    print("The computer won", c_score, "game(s)")
    print(t_score, "game(s) were tied")

main()

