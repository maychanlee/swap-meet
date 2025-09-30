from swap_meet.item import Item
class Vendor:

    # Wave 01:
    # Represents a vendor that manages an inventory of items.

    # Attributes:
    # inventory (list) Default =[]

    # Methods: 
    # add(item): Adds an item to the inventory.
    #         Returns the item that was added.

    # remove(item): Removes the matching item from the inventory.
    #         Returns the item that was removed.
    #         Returns False if the item is not found.
    

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
    
    # Wave 02:

    # Methods:
    # get_by_id = takes one argument (int of Item's id)
    #             returns item with matching id
    #             if no matching, return None
 
    def get_by_id(self,id):

        for item in self.inventory:
            if item.id == id:
                return item       
        return None

    # Wave 03:

    # Methods:
    # swap_items = takes 3 arguments: Vendor(others), Item(my_item), Item(their_item)
    #     removes my_item from inventory and put to Vendor(others)
    #     removes their_item from invetory and put to Vendor(self)
    #     if no matching item, returns False

    def swap_items(self, other_vendor, my_item, their_item):

        self.other_vendor = other_vendor
        self.my_item = my_item
        self.their_item = their_item

        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        if my_item in self.inventory:
            self.remove(my_item)
            other_vendor.add(my_item)
            other_vendor.remove(their_item)
            self.add(their_item)
            return True
  
    # Wave 04:

    # Methods:
    # swap_first_item = takes 1 argument: Vendor(others)
    # removes first item from my_item inventory and put to Vendor(others)
    # removes first item from their_item invetory and put to Vendor(self)
    # returns True
    # if inventory is an empty list, returns False
    
    def swap_first_item(self, other_vendor):
        
        if not self.inventory or not other_vendor.inventory:
            return False
        
        self.inventory[0], other_vendor.inventory[0] = other_vendor.inventory[0], self.inventory [0]
        return True

    # Wave 06:
    
    # Methods:
    # get_by_category = takes 1 argument: string representing category
    #         returns list of object with in category
    #         returns empty list if none
    # get_best_by_category = takes 1 argument: string representing category
    #         returns single item with highest condition
    #         returns None if no matching
    # swap_best_by_category = takes 3 arguments: other_vendor, my_priority, their_priority
    #         takes item from vendor(self) inventory that matches their priority and swap with items from other_vendor best item with my_priority
    #         returns True
    #         returns None if no matching
 
    def get_by_category(self, category):
       
        # self.category = []
        # if not self.inventory in category:
        #      return []
        category_list = []
        
        if not category:
            return category_list

        for item in self.invetory:
            if item.get_category() == category:
                category_list.append(item)
                
        return category_list
     
   