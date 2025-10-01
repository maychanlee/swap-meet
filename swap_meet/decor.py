from swap_meet.item import Item

class Decor(Item):
    def __init__(self, id=None, condition=0, width=0,length=0):
        """
        Wave 05: Represents a Decor object, which is a subclass of Item.

        Attributes:
            width (str): Width of the decor item. Defaults to "0".
            length (str): Length of the decor item. Defaults to "0".

        Methods:
            get_category(): Returns the string "Decor".
            __str__(): Returns a string like
                "An object of type Decor with id {id}. It takes up a {width} by {length} sized space."
        """
        super().__init__(id, condition)
        self.width = width
        self.length = length
    
    def get_category(self):
        return "Decor"

    def __str__(self):
        first_sentence = super().__str__()
        width = self.width
        length = self.length
        
        return f"{first_sentence} It takes up a {width} by {length} sized space."