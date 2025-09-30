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

    def __str__(self):
        id = self.id
        fabric = self.fabric
        type = super().get_category()
        
        return f"An object of type {type} with id {id}. It is made from {fabric} fabric."
