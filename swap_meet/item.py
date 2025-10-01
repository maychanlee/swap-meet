import uuid

class Item:

    def __init__(self, id=None, condition=0):
        """
        Wave 02: Represents a vendor object with a unique ID.
        Attributes: id (int) and condition (float, default 0).
        Method: get_category() returns a string with the class name.
        """
        if not id:
            self.id = uuid.uuid4().int
        else:
            self.id = id
        self.condition = condition
        

    def get_category(self):
        """
        Returns the name of the class of this instance as a string - self.__class__.__name__
        """
        return "Item"
    

    def __str__(self):
        """
        Wave 03: Provides string representation for an item.
        Method:
            __str__(): Returns a string like "An object of type Item with id ###."
        """
        item_id = self.id
        item = self.get_category()

        return f"An object of type {item} with id {item_id}."

    
    def condition_description(self):
        """
        Wave 05: Returns a description of an item's condition.
        Method: condition_description() provides a string describing the condition.
        """
        if 4 <= self.condition <= 5:
            return "Like New!"
        elif 3 <= self.condition < 4:
            return "Rarely Used!"
        elif 2 <= self.condition < 3:
            return "Decent Condition"
        elif 1 <= self.condition < 2:
            return "Pretty Used"
        else:
            return "Pretty Bad"


