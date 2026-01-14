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
    def __init__(self,name,description,weight,on):
        super().__init__(name,description,weight)
        self.on=False
    def state(self,game):
        self.on= not self.on
        if self.on:
            print("lampe allumé. \n")
        else:
            print("lampe éteinte.\n")
            
        
