# create the MenuItem class
class MenuItem:
    # dunder init method with four parameters about the item
    def __init__(self, name, itemType, price, description):
        # initializing the attributes
        self.name = name
        self.itemType = itemType
        self.price = price
        self.description = description

    # defining getter methods for each variable
    def getName(self):
        return self.name
    def getItemType(self):
        return self.itemType
    def getPrice(self):
        return self.price
    def getDesciption(self):
        return self.description

    # dunder str for nice output of the item
    def __str__(self):
        return self.name + "(" + self.itemType + "): $" + self.price +"\n\t" + self.description