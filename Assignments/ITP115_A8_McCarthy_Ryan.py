# Ryan McCarthy, rbmccart@usc.edu
# ITP 115, Fall 2020
# Assignment 8
# Description:
# a game of tic-tac-toe to be played between "two" people

# import this module, unsure why it says module not found in my editor, but its working...
import TicTacToeHelper
# random to help the computer
import random

# bonus pretty board function, looped through each twice then printed third seperate so there was no | or ------.....
def printPrettyBoard(board_list):
    print()
    counter = 0
    for i in range(2):
        for j in range(2):
            print(board_list[counter], end=" | ")
            counter += 1
        print(board_list[counter])
        counter += 1
        print("---------")
    for o in range(2):
        print(board_list[counter], end=" | ")
        counter += 1
    print(board_list[counter], "\n")
    counter += 1

# function to see if move is valid
def isValidMove(boardList, spot):
    # if its on the board its true, else false and the playGame() will loop until its found
    if spot in boardList:
        return True
    else:
        return False


# updates the board with the correct move
def updateBoard(boardList, spot, playerLetter):
    # replace the spot with the player letter
    spot = int(spot)
    boardList[spot] = playerLetter


# function to play the game
def playGame():
    # list for the players
    players = ["x", "o"]
    # list for the board
    boardList = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    # counter for the turn and for game ending logic
    count = 1
    turn = 0
    gameStatus = "n"
    # extra work for allowing player to choose who starts with error checking
    start = input("Who would you like to start (x/o): ")
    while start not in players:
        start = input("Who would you like to start (x/o): ")
    if start == "x":
        turn = 0
    else:
        turn = 1
    print("Here is a fresh board!")
    printPrettyBoard(boardList)
    # while loop for the duration of one game
    while gameStatus == "n":
        # get input for spot
        move = input("Player " + players[turn % 2] + " pick a spot: ")
        # loop question if input is invalid spot on board
        while not isValidMove(boardList, move):
            print("\nInvalid move, please try again.")
            move = input("Player " + players[turn % 2] + " pick a spot: ")
        # updates the board
        updateBoard(boardList, move, players[turn % 2])
        # sets gameStatus equal to function to see result of each round
        gameStatus = TicTacToeHelper.checkForWinner(boardList, count)
        # prints the board after each round
        printPrettyBoard(boardList)
        # adds one to count
        count += 1
        turn += 1
    # prints game result based on game result lol
    print("And that's the game!!!")
    if gameStatus in ["x", "o"]:
        print("Player " + gameStatus + " wins!!!")
    else:
        print("Tough luck. That's a stalemate!")

# play against the computer, copied most code from my multiplayer function
def playComputer():
    print("You are now playing against the computer. Enjoy!")
    print("The computer will play as player x.")
    # list for the players
    players = ["x", "o"]
    # list for the board
    boardList = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    # counter for the turn and for game ending logic
    count = 1
    turn = 0
    gameStatus = "n"
    # extra work for allowing player to choose who starts with error checking
    start = input("Who would you like to start? Remember that you are player o. (x/o): ")
    while start not in players:
        start = input("Who would you like to start? Remember that you are player o. (x/o): ")
    if start == "x":
        turn = 0
    else:
        turn = 1

    print("Here is a fresh board!")
    printPrettyBoard(boardList)
    # while loop for the duration of one game
    while gameStatus == "n":
        # get computer choice, have to cast to string for isValidMove function
        if players[turn%2] == "x":
            move = str(random.randint(0, 8))
            while not isValidMove(boardList, move):
                move = str(random.randint(0, 8))
            print("The computer chose spot " + move + ".")
        # get player input for spot
        else:
            move = input("Pick a spot: ")
            # loop question if input is invalid spot on board
            while not isValidMove(boardList, move):
                print("\nInvalid move, please try again.")
                move = input("Pick a spot: ")
        # updates the board
        updateBoard(boardList, move, players[turn % 2])
        # sets gameStatus equal to function to see result of each round
        gameStatus = TicTacToeHelper.checkForWinner(boardList, count)
        # prints the pretty board after each round
        printPrettyBoard(boardList)
        # adds one to count
        count += 1
        turn += 1
    # prints game result based on game result lol
    print("And that's the game!!!")
    if gameStatus in ["x", "o"]:
        if gameStatus == "x":
            print("Computer wins. They always do...")
        else:
            print("You win!!!")
    else:
        print("Tough luck. That's a stalemate!")

# main function to put everything together
def main():
    # variable to control the possibility of sequential games
    play = "y"
    while play == "y":
        # single or multiplayer
        player = input("Single player or multiplayer? (s/m): ").lower()
        while player not in ["s", "m"]:
            print("Invalid choice. Try again:")
            player = input("Single player or multiplayer? (s/m): ")
        if player == "s":
            playComputer()
        else:
            playGame()
        play = input("Would you like to continue (y/n): ")
        # additional error checking
        while play not in ["y", "n"]:
            print("Invalid choice. Try again:")
            play = input("Would you like to continue (y/n): ")


# run it
main()
