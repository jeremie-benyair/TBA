class Item():
    def __init__(self,name,description,weight,text=None,damage=None,type=None):
        self.name=name
        self.description=description
        self.weight=weight
        self.text=text 
        self.damage=damage
        self.type=type
    def __str__(self):
        return f"{self.name} : {self.description} ({self.weight}) kg)\n"
class Flashlight(Item):
    def ___init___(self,name,description,weight):
        super().___init___(name,description,weight)
    def state(self,game):
        
