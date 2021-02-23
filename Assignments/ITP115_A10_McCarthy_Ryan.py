# Ryan McCarthy, rbmccart@usc.edu
# ITP 115, Fall 2020
# Assignment 9
# Description:
# this program creates a fake user's music library and allows them to edit it like they normally would

# importing necessary modules
import MusicLibraryHelper
import random
import string

# display the menu with basic print statement
def displayMenu():
    print("""\nWelcome to Your Music Library
Options:
 1) Display library
 2) Display all artists
 3) Add an album
 4) Delete an album
 5) Delete an artist
 6) Search library
 7) Generate a random playlist
 8) Make your own playlist
 9) Exit""")

# display the entire library
def displayLibrary(musicLibDictionary):
    # for key among the keys
    for key in musicLibDictionary.keys():
        # print the artist bc they are the keys
        print("\nArtist:", key)
        # then print each album that that artist(key) has in the playlist
        print("Albums: ")
        for i in musicLibDictionary[key]:
            print("\t-", i)

# display all of the artists
def displayArtists(musicLibDictionary):
    # same as last function, just displaying artists
    print("Displaying all artists: ")
    for key in musicLibDictionary.keys():
        print("\t-" + key)

# add an album to the dictionary
def addAlbum(musicLibDictionary):
    # get inputs
    addArtist = string.capwords(input("Enter artist: ").lower())
    addAlbum = string.capwords(input("Enter album: ").lower())
    # if its not in the add album and artist
    if addArtist not in musicLibDictionary.keys():
        musicLibDictionary[addArtist] = [addAlbum]
    else:
        # else add the album only if its not already in the values
        if addAlbum not in musicLibDictionary[addArtist]:
            musicLibDictionary[addArtist].append(addAlbum)

# delete albums
def deleteAlbum(musicLibDictionary):
    # get inputs
    delArtist = string.capwords(input("Enter artist: ").lower())
    delAlbum = string.capwords(input("Enter album: ").lower())
    # if album doesn't exist false will prompt respective output in main()
    if delAlbum not in musicLibDictionary[delArtist]:
        return False
    # else remove the album
    else:
        musicLibDictionary[delArtist].remove(delAlbum)
        # if the album woas the last one del the artist
        if not musicLibDictionary[delArtist]:
            del musicLibDictionary[delArtist]
        # then return this for main() output
        return True

# delete an artist
def deleteArtist(musicLibDictionary):
    # get input
    delArtist = string.capwords(input("Enter artist: ").lower())
    # again will check if it exists and send the respective bool to main() for respective output
    if delArtist not in musicLibDictionary.keys():
        return False
    else:
        del musicLibDictionary[delArtist]
        return True

# search words in the library
def searchLibrary(musicLibDictionary):
    # these help with printing no matching results or whatever when there are no mathcing results
    inArtist = False
    inAlbum = False
    # input search term
    wordSearch = input("Enter search term: ").lower()
    # print list of artist that contain the word
    print("Artists containing \'" + wordSearch + "\':")
    for key in musicLibDictionary.keys():
        key = key.lower()
        if wordSearch in key:
            inArtist = True
            key = string.capwords(key)
            print("-", key)
    # handles nothing mathing using bools from earlier
    if not inArtist:
        print("\tNo matching results")
    print("Albums containing \'" + wordSearch + "\'")
    # same process as above here
    for key in musicLibDictionary.keys():
        for j in musicLibDictionary[key]:
            j = j.lower()
            if wordSearch in j:
                inAlbum = True
                j = string.capwords(j)
                print("-", j)
    if not inAlbum:
        print("\tNo matching results")

# gen a random playlist
def generateRandomPlaylist(musicLibDictionary):
    print("Here is your random playlist: ")
    # for each artist select a random album
    for key in musicLibDictionary.keys():
        i = random.randrange(len(musicLibDictionary[key]))
        print("-", musicLibDictionary[key][i], "by", str(key))

# extra credit function for making a custom playlist
def generateCustomPlaylist(musicLibDictionary):
    # loop control variable and empty playlist to start and be appeneded to
    contBuilding = "y"
    userPlaylist = []
    # loop for building
    while contBuilding == "y":
        # print playlist so far
        print("Your playlist so far:")
        for i in userPlaylist:
            print("\t-", i)
        print("-----")
        # variables for logic used later
        artistNum = 0
        albumNum = 0
        artists = []
        albums = []
        artistOptions = []
        albumOptions = []
        # add each key and its index to lists made above
        for key in musicLibDictionary.keys():
            print(str(artistNum) + ") " + key)
            artists.append(key)
            artistOptions.append(artistNum)
            artistNum += 1
        # get artist selection and set it to str value
        artistNumSelected = int(input("Select an artist by number: "))
        while artistNumSelected not in artistOptions:
            print("Invalid selection")
            artistNumSelected = int(input("Select an artist by number: "))
        # exact same process and logic from above but with the artists corresponding albums now
        artistSelected = artists[artistNumSelected]
        for i in musicLibDictionary[artistSelected]:
            print("\t" + str(albumNum) + ") " + i)
            albumOptions.append(albumNum)
            albums.append(i)
            albumNum += 1

        albumNumSelected = int(input("Select an album by number: "))
        while albumNumSelected not in albumOptions:
            print("Invalid selection")
            albumNumSelected = int(input("Select an album by number: "))

        albumSelected = albums[albumNumSelected]
        # append to the user playlist in the form I want to print it in for ease later
        userPlaylist.append(albumSelected + " by " + artistSelected)
        # ask for more inputs maybe
        contBuilding = input("Would you like to continue building your playlist (y/n): ").lower()
        while contBuilding not in ["y", "n"]:
            contBuilding = input("Would you like to continue building your playlist (y/n): ").lower()
    # final playlist
    print("Your final playlist:")
    for i in userPlaylist:
        print("\t-" + i)

# main :)
def main():
    # load the library to an dict
    musicLibrary = MusicLibraryHelper.loadLibrary("musicLibrary.dat")
    # menu choices and also while loop control variable
    menuChoices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    menuChoice = 1
    # while not exit do this
    while menuChoice != 9:
        # get the choice from the user then execute
        displayMenu()
        menuChoice = int(input(">") or 0)
        while menuChoice not in menuChoices:
            print("Invalid choice. Try again:")
            menuChoice = int(input(">") or 0)
        # execute the choice based on the input
        if menuChoice == 1:
            displayLibrary(musicLibrary)
        if menuChoice == 2:
            displayArtists(musicLibrary)
        if menuChoice == 3:
            addAlbum(musicLibrary)
        if menuChoice == 4:
            result = deleteAlbum(musicLibrary)
            # handling return value from function
            if result:
                print("Album successfully deleted.")
            else:
                print("Album did not exist")
        if menuChoice == 5:
            result = deleteArtist(musicLibrary)
            # same as above
            if result:
                print("Artist successfully deleted.")
            else:
                print("Artist did not exist")
        if menuChoice == 6:
            searchLibrary(musicLibrary)
        if menuChoice == 7:
            generateRandomPlaylist(musicLibrary)
        if menuChoice == 8:
            generateCustomPlaylist(musicLibrary)
        if menuChoice == 9:
            # goodbye statements before exit
            print("Saving music library")
            print("Goodbye")
    # save the nex object to the library
    MusicLibraryHelper.saveLibrary("musicLibrary.dat", musicLibrary)

# call main
main()