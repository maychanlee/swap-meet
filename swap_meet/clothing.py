from swap_meet.item import Item

class Clothing(Item):
    """
    Wave 05:
    
    Attributes:
    Clothing(Item) = clone class
    fabric = decription of clothing, defaults to "Unknown"

    Methods:
    get_category = returns "Clothing"
    str = "An object of type Clothing with id {id}. It is made from {fabric} fabric."
    """

    def __init__(self, id = None, condition = 0, fabric = "Unknown"):
        super().__init__(id, condition)
        self.fabric = fabric

    def get_category(self):
        return "Clothing"

    def __str__(self):
        first_sentence = super().__str__()
        fabric = self.fabric
        
        return f"{first_sentence} It is made from {fabric} fabric."
