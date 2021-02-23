from MenuItem import MenuItem

# creating the menu class
class Menu:
    # given list of item types on the menu
    MENU_ITEM_TYPES = ["Drink", "Appetizer", "Entree", "Dessert"]
    # dunder init method taking the file as sole parameter
    def __init__(self, menu="menu.csv"):
        # open up the file object
        readMenu = open(menu, "r")
        # initialize the menu item dictionary (extra credit)
        self.menuItemDict = {"Drink":[], "Appetizer": [], "Entree": [], "Dessert": []}
        # counter for next for loop
        i = 0
        for line in readMenu:
            # split the line into a list
            itemList = line.split(",")
            # assign the values of the new list to the MenuItem Object
            newItem = MenuItem(itemList[0], itemList[1], itemList[2], itemList[3])
            # append object to proper list in menuItemDict
            self.menuItemDict[itemList[1]].append(newItem)
        # close the file object
        readMenu.close()

    # get menu item method based on itemType and itemIndex
    def getMenuItem(self, itemType, itemIndex):
        # return the menu item
        return self.menuItemDict[itemType][itemIndex]

    # print the items that are of the same item type specified
    def printMenuItemsByType(self, itemType):
        # loop through the respective list and pretty print it
        # counter
        i = 0
        # print item type
        print("\n-----" + itemType + "-----")
        for item in self.menuItemDict[itemType]:
            # print the list number
            print(str(i) + ")", end=" ")
            # print the item using the __str__ method
            print(item, end="")
            # update counter
            i += 1

    # return the length of the list that represents the number of items for the itemType
    def getNumMenuItemsByType(self, itemType):
        return len(self.menuItemDict.get(itemType))
