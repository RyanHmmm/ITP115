# Name, USC email
# ITP 115, Spring 2020
# Assignment 2
# Description:
# This program creates a harry potter vending machine.
# It determines change and gives a discount.

# First I will get user choice and handles possibility of capital input
choice = input('''
Please choose one of the following:
a) Butterbeer: 58 knuts
b) Quill: 10 knuts
c) The Daily Prophet: 7 knuts
d) Book of Spells: 400 knuts
e) Sandwisp: 32 knuts
>''').lower()

# this defines cost and handles invalid user input for choice (also handles for capital input)
if choice == "a":
    cost = 58
    item = "a Butterbeer"
elif choice == "b":
    cost = 10
    item = "a Quill"
elif choice == "c":
    cost = 7
    item = "The Daily Prophet"
elif choice == "d":
    cost = 400
    item = "a Book of Spells"
elif choice == "e":
    cost = 32
    item = "a Sandwisp"
else:
    print('''You have entered an invalid option. You will be given a Butterbeer for 58
knuts.''')
    cost = 58
    item = "a Butterbeer"

# get variable called disc_i to determine if they are willing to post for a discount (also handles capital input here)
disc_i = input("Are you willing to share your purchase on instagram for 5 knuts off? Enter (y/n): ").lower()

if disc_i == "y":
    disc = 5
    discount = "with a coupon for 5 knuts"
    cost -= 5
elif disc_i == "n":
    disc = 0
    discount = "without a coupon"
else:
    print("You have entered an invalid option. No discount will be given.")
    disc = 0
    discount = "without a coupon"
# obtain how they will be paying for the item (this is for the extra credit piece)
g_pay = int(input("Enter how many galleons will you be paying with: "))
s_pay = int(input("Enter how many sickles will you be paying with: "))
k_pay = int(input("Enter how many knuts will you be paying with: "))

# calculates total currency  in knuts given by user and assigns it to the variable pay
pay = (g_pay*493) + (s_pay*29) + k_pay

# terminates program if user does not insert enough to pay for item
if pay < cost:
    print("That is not going to cover it. Check the tray below for your money and please try again.")
    exit()

# tells them what they purchased, for how much, and with what coins
print("You bought " + item + " for " + str(cost) + " knuts (" + discount +
      ") and paid with " + str(g_pay) + " galleon, " + str(s_pay) + " sickles, and "
      + str(k_pay) + " knuts.")

# calculates change (total and by coin)
change = pay - cost
gal_rem = change // 493
rem_change = change % 493
s_rem = rem_change // 29
rem_change_2 = rem_change % 29

# prints the users change
print("Here is your change " + str(change) + ":")
print("Galleon: " + str(gal_rem))
print("Sickle: " + str(s_rem))
print("Knuts: " + str(rem_change_2))
