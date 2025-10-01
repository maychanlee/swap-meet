from swap_meet.item import Item
from swap_meet.decor import Decor
from swap_meet.clothing import Clothing
from swap_meet.electronics import Electronics

class Vendor:

    """
    Wave 01: Represents a vendor managing an inventory of items.
    Attributes: inventory (list), default is an empty list.
    Methods: add(item) adds and returns the item; 
    remove(item) removes and returns the item or False if not found.
    """

    def __init__(self, inventory=None):
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
    

    def get_by_id(self,id):
        """
        Wave 02: Provides method to retrieve an item by its ID.
        Method: get_by_id(id) searches inventory for matching item ID.
        Returns the item if found, otherwise returns None.
        """
        for item in self.inventory:
            if item.id == id:
                return item       
        return None

    
    def swap_items(self, other_vendor, my_item, their_item):
        """
        Wave 03: Handles swapping items between two vendors.
        Method: swap_items(other_vendor, my_item, their_item) exchanges items between inventories.
        Returns False if either item is not found; otherwise completes the swap.
        """

        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        self.remove(my_item)
        other_vendor.add(my_item)
        other_vendor.remove(their_item)
        self.add(their_item)
        return True
    
    
    def swap_first_item(self, other_vendor):
        """
        Wave 04: Swaps the first item between two vendors.
        Method: swap_first_item(other_vendor) exchanges the first item of each inventory.
        Returns True if swap is successful; returns False if either inventory is empty.
        """
        
        if not self.inventory or not other_vendor.inventory:
            return False
        
        self.inventory[0], other_vendor.inventory[0] = other_vendor.inventory[0], self.inventory[0]
        return True

    
    def get_by_category(self, category):
        """
        Wave 06: Provides category-based item management and swapping between vendors.
        Methods: get_by_category(category) returns all items in the category; 
        get_best_by_category(category) returns the item with highest condition or None; 
        swap_best_by_category(other_vendor, my_priority, their_priority) swaps best-matching items and returns True or None if no match.
        """
        
        category_list = []
        
        if not category:
            return category_list

        for item in self.inventory:
            if item.get_category() == category:
                category_list.append(item)
                
        return category_list

    
    def get_best_by_category(self,category):
        """
        Returns the item with the highest condition in the given category.
        Returns None if no items in that category exist.
        """
        category_list = self.get_by_category(category)

        if not category_list:
            return None

        best_item = category_list[0]

        for item in category_list:
            if item.condition > best_item.condition:
                best_item = item
        return best_item

    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        """
        Swaps the best item of the specified categories between self and other_vendor.
        Returns True if swap is successful, or False if either item is not found.
        """
        my_best_item = self.get_best_by_category(their_priority)
        their_best = other_vendor.get_best_by_category(my_priority)

        if not my_best_item or not their_best:
            return False 
            
        self.swap_items(other_vendor, my_best_item, their_best)
        return True