import uuid

class Item:
    """
        Wave 02:

        represents the object for vendor with unique id

        Attributes:
        id = unique integer
        condition (from Wave 05) = 0
        
        Packages to Import:
        uuid - to help create large unique numbers as identifiers

        Methods:
        get_category = returns a string holding the name of the class

        Instances of `Vendor` have an instance method named `get_by_id`
    - This method takes one argument: an integer, representing an `Item`'s `id`
    - This method returns the item with a matching `id` from the inventory
    - If there is no matching item in the `inventory`, the method should explicitly return `None`
    """
    
    def __init__(self, id = None, condition = 0):
        if not id:
            self.id = uuid.uuid4().int
        else:
            self.id = id
        self.condition = condition

    def get_category(self):
        return self.__class__.__name__

    def __str__(self):
        """
        Wave 03:
        Methods:
        str() = convert item to string
                returns "An object of type Item with id ###.   
        """
        id = self.id
        item = self.get_category()

        return f"An object of type {item} with id {id}."

    """
        Wave 05:
        Methods:
        condition_description = describes the condition
    """


