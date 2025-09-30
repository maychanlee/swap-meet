class Vendor:
    """ Represents a vendor that manages an inventory of items.
    Attributes:inventory (list) Default =[]

    Methods: 
    add(item): Adds an item to the inventory.
               Returns the item that was added.
    remove(item): Removes the matching item from the inventory.
            Returns the item that was removed.
            Returns False if the item is not found.
    """

    def __init__(self,inventory = None):
        if not inventory:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self,item):
        self.inventory.append(item)
        return item
    
    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

