# Ryan McCarthy, rbmccart@usc.edu
# ITP 115, Fall 2020
# Assignment 1
# Description:
# This program creates a Mad Libs story about a night at the casino from user inputs

noun = input("Enter a city: ")
verb1 = input("Enter a past tense verb: ")
verb_ing = input("Enter a verb ending with -ing: ")
adj = input("Enter an adjective: ")
adj2 = input("Enter another adjective: ")
friends = input("Enter a number: ")
cash = int(input("Enter a second number: "))
cash2 = int(input("Enter a third number (smaller than second): "))
chance = input("Enter a number 0-100 with a decimal: ")

newcash = cash + cash2

print(
    '\nI was in "' + noun + '" with "' + friends + '''" of my best friends. 
We were "''' + verb_ing + '" to the casino and I felt "' + adj + '''". 
I had "''' + str(cash) + '''" dollars with me. I decided to 
take "''' + str(cash2) + '''" and put it on red. I closed my eyes because 
I was so "''' + adj2 + '''", but then I heard all of my friends yelling. 
I won!!! I won and would be leaving with "''' + str(newcash) + '''" dollars! 
There was only a "''' + chance + '''%" chance of that happening. 
I "''' + verb1 + '" out and would never forgot that night.')
