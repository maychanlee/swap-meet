from swap_meet.item import Item

class Decor(Item):
    def __init__(self,id = None, condition = 0,width = 0,length = 0):
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
    
        

    """
        Wave 05:
        
        Attributes:
        Decor(Item) = clone class
        width = decription of decor, defaults to "0"
        length = decription of decor, defaults to "0"
        

        Methods:
        get_category = returns "Decor"
        str = "An object of type Decor with id {id}. It takes up a {width} by {length} sized space."
    """