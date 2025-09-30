import uuid

class Item:

    # Wave 02:

    # represents the object for vendor with unique id

    # Attributes:
    # id = unique integer
    # condition (from Wave 05) = 0
    
    # Packages to Import:
    # uuid - to help create large unique numbers as identifiers

    # Methods:
    # get_category = returns a string holding the name of the class

    def __init__(self, id = None, condition = 0):
        if not id:
            self.id = uuid.uuid4().int
        else:
            self.id = id
        self.condition = condition
        

    def get_category(self):
        # return self.__class__.__name__
        return "Item"

    #  Wave 03:
    #     Methods:
    #     str() = convert item to string
    #             returns "An object of type Item with id ###.

    def __str__(self):
        id = self.id
        item = self.get_category()

        return f"An object of type {item} with id {id}."

    # Wave 05:
    # Methods:
    # condition_description = describes the condition

    def condition_description(self):
        if self.condition in range(4,5):
            return "Like New!"
        elif self.condition in range(3,4):
            return "Rarely Used!"
        elif self.condition in range(2,3):
            return "Decent Condition"
        elif self.condition in range(1,2):
            return "Pretty Used"
        else:
            return "Pretty Bad"


