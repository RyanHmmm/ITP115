# Ryan McCarthy, rbmccart@usc.edu
# ITP 115, Fall 2020
# Assignment 9
# Description:
# language translator

def getLanguages(fileName="languages.csv"):
    # open the file
    fileIn = open(fileName, "r")
    # get the first line in a string and strip it
    firstLine = fileIn.readline().strip()
    # its a csv file so split based on commas
    langList = firstLine.split(",")
    # close the file
    fileIn.close()
    # return the list
    return langList

def getSecondLanguage(langList):
    # list for error checking
    eList = []
    # loop for each word now to get in lower casing for error checking
    for word in langList:
        word = word.lower()
        # append the word to the langList
        eList.append(word)
    # print statement for users
    print("Here is the list of languages that you can translate from: ")
    print(" - ".join(langList))
    secLang = input("Enter a language: ").lower().strip()
    while secLang not in eList:
        secLang = input("Enter a language: ").lower().strip()
    # capitalizing the second lang back for other functions to use
    secLang = secLang.capitalize()
    return secLang

def readFile(langList, langStr="English", fileName="languages.csv"):
    # open the file
    fileIn = open(fileName, "r")
    # clean up the first line
    fLine = fileIn.readline().strip()
    # put it into a list splitting by comma
    langs = fLine.split(",")
    # get the index where the language is on the first line
    langIndex = langs.index(langStr)
    # empty list to add english words to
    matchLang = []
    # iterator
    lineNum = 2
    # go through each line to get the english words
    for line in fileIn:
        # clean up and put into list
        line.strip()
        lineList = line.split(",")
        matchLang.append(lineList[langIndex])
        lineNum += 1
    # close file and return the list of english words
    fileIn.close()
    return matchLang

def createResultsFile(language, resultsFile):
    newFile = open(resultsFile, "w")
    # file header
    print("Words translated from English to", language, file=newFile)
    newFile.close()

def translateWords(englishList, secondList, resultsFile):
    fileIn = open(resultsFile, "a")
    # control var
    cont = "y"
    # error checking
    answers = ["y", "n"]
    # while loop to translate
    while cont == "y":
        # ask word
        inputWord = input("\nWhat word would you like to translate: ").lower()
        while inputWord not in englishList:
            inputWord = input("What word would you like to translate: ").lower()
        # get index then translated word
        englishIndex = englishList.index(inputWord)
        transWord = secondList[englishIndex]
        # if "-" then do this
        if transWord == "-":
            print(inputWord, "does not have a translation.")
            cont = input("Would you like to continue (y/n): ").lower()
            while cont not in answers:
                cont = input("Would you like to continue (y/n): ").lower()
        # else show translation and write it in the new file
        else:
            print(inputWord, "translated to", transWord)
            print(inputWord, "=", transWord, file=fileIn)
            cont = input("Would you like to continue (y/n): ").lower()
            while cont not in answers:
                cont = input("Would you like to continue (y/n): ").lower()

    print("Results have been saved in", resultsFile)
    # close file
    fileIn.close()

def main():
    # get the list of languages
    langList = getLanguages()
    # get the english list of languages
    englishList = readFile(langList)
    # get the second language
    secondLang = getSecondLanguage(langList)
    # get the list for the second language
    secondList = readFile(langList, secondLang)
    # get name for results file
    resultsFile = input("Name for results file (do not include \".txt\"): ") or (secondLang)
    resultsFile = resultsFile + ".txt"
    # open up the results file
    createResultsFile(secondLang, resultsFile)
    # translate the words
    translateWords(englishList, secondList, resultsFile)

main()