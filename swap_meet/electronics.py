from swap_meet.item import Item

class Electronics(Item):

    """
    Wave 05:
    
    Attributes:
    Electronics(Item) = clone class
    type = decription of electronics, defaults to "Unknown"

    Methods:
    get_category = returns "Electronics"
    str = "An object of type Electronics with id {id}. This is a {type} device."
    """
    
    def __init__(self, id = None, condition = 0, type = "Unknown"):
        super().__init__(id, condition)
        self.type = type

    def get_category(self):
        return "Electronics"

    def __str__(self):
        first_sentence = super().__str__()
        type = self.type
        
        return f"{first_sentence} This is a {type} device."
