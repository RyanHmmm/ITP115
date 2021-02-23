from MenuItem import MenuItem

class Diner:
    STATUSES = ["seated", "ordering", "eating", "paying", "leaving"]
    # initialize the variables
    def __init__(self, dinerName):
        self.name = dinerName
        self.order = []
        self.status = 0

    # defining getter methods for each variable
    def getName(self):
        return self.name
    def getOrder(self):
        return self.order
    def getStatus(self):
        return self.status

    # adds one to the self.status
    def updateStatus(self):
        self.status += 1

    # adds the item to the order
    def addToOrder(self, MenuItemObject):
        self.order.append(MenuItemObject)

    # prints the order
    def printOrder(self):
        for item in self.order:
            # print the item type and list number
            print("-----" + self.name + "-----")
            print("- ", end=" ")
            # print the item using the __str__ method
            print(item)
    # calculates the meal cost
    def calculateMealCost(self):
        cost = 0
        # loops through order and adds the 3 item in list to the cost (this is the item cost)
        for item in self.order:
            price = item.getPrice()
            cost += float(price)
        # return the cost
        return cost

    # pretty print diner name and status
    def __str__(self):
        return "Diner " + self.name + " is currently " + Diner.STATUSES[self.status]
