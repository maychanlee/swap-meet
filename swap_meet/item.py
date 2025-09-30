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
    """

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


