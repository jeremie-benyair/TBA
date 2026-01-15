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
                print(f"{game.player.current_room.name} est désormais éclairé !")
               
                print(game.player.current_room.get_long_description)
                
        else:
            print("lampe éteinte.\n")
class Beamer(Item):
    def __init__(self,name,description,weight):
        super().__init__(name,description,weight)
    def use_item(self,game):  
        which_room=input("choisissez un lieu parmi ceux déjà visité.\n")
        if which_room not in game.player.historique:
            print("vous n'avez pas encore visité ce lieu, vous ne pouvez donc pas vous y déplacer.\n")
        current_room=which_room
        print(game.player.current_room.get_long_description)
        
    
            
            
        
