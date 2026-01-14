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
    def use_item(self,game):
        print(f"vous ne pouvez pas utiliser l'objet {self.name} \n")
class Flashlight(Item):
    def __init__(self,name,description,weight):
        super().__init__(name,description,weight)
        self.on=False
    def use_item(self,game):
        self.on= not self.on
        if self.on:
            print("lampe allumé. \n")
            if game.player.current_room.darked:
                game.player.current_room.darked=False
                print(f"{game.player.current_room} est désormais éclairé !")
               
                print(game.player.current_room.get_long_description)
                
        else:
            print("lampe éteinte.\n")
class Beamer(Item):
    def __init__(self,name,description,weight):
        super().__init__(name,description,weight)
        which_room=input("choisissez un lieu parmi ceux déjà visité.\n")
        if which_room not in 
        
    
            
            
        
