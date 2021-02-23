# import statements
from Menu import Menu
from Diner import Diner

# waiter class
class Waiter:
    # initialize variables with menuObject as sole parameter
    def __init__(self, menuObject):
        self.diners = []
        self.menu = menuObject

    # add a diner based on dinerObject passed in
    def addDiner(self, dinerObject):
        self.diners.append(dinerObject)

    # gets length of diners list which is how many are dining currently
    def getNumDiners(self):
        return len(self.diners)

    # print the diners status nicely
    def printDinerStatuses(self):
        # for each possible status
        for i in range(5):
            # print this
            print("Diners who are " + Diner.STATUSES[i] + ":")
            # for each diner that matches the currently selected status, print it
            for diner in self.diners:
                if i == diner.getStatus():
                    print("\t", diner)

    def takeOrders(self):
        # for each diner
        for diner in self.diners:
            # if the status of that diner is "ordering"
            name = diner.getName()
            if diner.getStatus() == 1:
                # loop through menu items and have them select one valid option per category
                for i in Menu.MENU_ITEM_TYPES:
                    # get index value of item
                    index = Menu.MENU_ITEM_TYPES.index(i)
                    # print the items for the item type
                    self.menu.printMenuItemsByType(i)
                    # error checking the choice
                    choice = int(input("\n" + name + " please select a " + Menu.MENU_ITEM_TYPES[index] + " menu item number:"))
                    # get the number of items in the itemType list
                    max = self.menu.getNumMenuItemsByType(i)
                    while choice not in range(0, max):
                        choice = int(input(name + " please select a " + Menu.MENU_ITEM_TYPES[index] + " menu item number:"))
                    # get the item and add this to order
                    item = self.menu.getMenuItem(i, choice)
                    diner.addToOrder(item)
                # print order by item
                print("\n", name, "ordered:")
                for item in diner.getOrder():
                    # print "-" and then the item for nice formatting
                    print("-", end="")
                    print(item, end="")

    # get the cost of the meal
    def ringUpDiners(self):
        for diner in self.diners:
            # if status is paying
            if 3 == diner.getStatus():
                # get name and meal cost in variables
                name = diner.getName()
                cost = diner.calculateMealCost()
                print("\n" + name + ", your meal cost is $" + str(cost))

    # remove the diners that are finished
    def removeDoneDiners(self):
        # go through the diners in reverse order
        for diner in reversed(self.diners):
            if 4 == diner.getStatus():
                name = diner.getName()
                # print thanks
                print("\n" + name + ", thank you for dining with us! Come again soon!")
                # remove based on name
                self.diners.remove(diner)

    # advance the diners with the premade methods
    def advanceDiners(self):
        self.printDinerStatuses()
        self.takeOrders()
        self.ringUpDiners()
        self.removeDoneDiners()
        for diner in self.diners:
            diner.updateStatus()
