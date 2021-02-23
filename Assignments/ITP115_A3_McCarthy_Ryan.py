# Ryan McCarthy
# ITP 115, Fall 2020
# Assignment 3
# Description:
# this program takes inputs from the user and then returns the avg, largest, and smallest given

# defining looping variable for first loop
run = "y"

while run == "y":
    # defining variables to be used in and for second loop
    u_input = 0
    i = 0
    high = -2
    low = 10000000000000000000000
    total = 0
    avg = "nothing"

    # asking question
    print("Input an integer greater than or equal to 0 (-1 to quit)")
    # interior loop that takes the inputs and then tracks highest, lowest, and avg of the numbers
    while u_input != -1:
        u_input = int(input(">"))
        if u_input != -1:
            total += u_input
            i += 1
            if u_input > high:
                high = u_input
            if u_input < low:
                low = u_input
            avg = total / i


    # prints stats
    print("The largest number is " + str(high) + "\nThe smallest number is " + str(low) +
          "\nThe average number is " + str(avg))
    # gives chance to evaluate fist loop to true or false
    run = input("\nWould you like to try again? (y/n): ")

# :)
print("\n\nThanks for playing!")

# if possible could you explain how I could refactor so if the user
# gives -1 on the first iteration it doesn't print the fake stuff?
# I will look at the notes for the grade
# Thanks!!!
