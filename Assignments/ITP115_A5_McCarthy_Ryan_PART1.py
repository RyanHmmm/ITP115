# Ryan McCarthy, rbmccart@usc.edu
# ITP 115, Fall 2020
# Assignment 5
# Description:
# this program takes a word, jumbles it
# it will reward the player if they can assemble it correctly without the hint, this is based on number of attempts

# imports random for game
import random

# words to be used for the game
words = ["scramble", "game", "python", "peachy"]

# selects random word
word = random.choice(words)

# defines hints here based on random word chosen
if word == "scramble":
    hint = "its what I did to the word"
elif word == "game":
    hint = "Haha, it's all fun and \"\" -s."
elif word == "python":
    hint = "What language do I speak?"
# this is so the later if statement for scoring doesn't raise style error for the hint to be undefined...
else:
    hint = "Our class nickname. Isn't it just \"\""

# defines variables to be used later
win = word
new = ""
# changes random word to list for rearrangement, then rearranges word
l_word = list(word)
for char in word:
    n_char = l_word.pop(random.randrange(len(l_word)))
    new += n_char
# tells user the word
print("Your word is", new)
# allows user to guess once before loop begins, also protects against the possibility user enters caps
guess = input("What do you think is the unscrambled word: ").lower()
# defines variables, i is for counting how many times game is played, h is for counting if the hint is used or not
i = 1
h = 0
# while loop that holds user inside until correct answer (brutal ik)
# also gives hint if the first two attempts are incorrect
while guess != win:
    print("\nIncorrect")
    if i > 1:
        print("Here is the hint: ", hint)
        h += 1
    guess = input("What do you think is the unscrambled word: ").lower()
    i += 1

# prints amount of tries based on i
print("Correct! It took you", i, "tries.")
# prints score and reasoning based on number of attempts and also if the hint was used
if h == 0 and i == 1:
    print("Your final score is 2 because it took you one try and you didn't need the hint!")
elif h == 0 and i == 2:
    print("Your final score is 1 because it took you two tries and you didn't need the hint!")
else:
    print("Your final score is 0 because it took you", i, "tries and you needed the hint! Maybe next time.")
