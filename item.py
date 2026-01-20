class Item():
    def __init__(self,name,description,weight,text=None,type=None):
        self.name=name
        self.description=description
        self.weight=weight
        self.text=text 
        
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

class Weapon(Item):
    def __init__(self, name, description, weight, damage):
        super().__init__(name, description, weight)
        self.damage = damage
        self.type = "weapon"

    def use_item(self, game):
        room = game.player.current_room
        if room.enemy is None:
            print(" il n'y a rien à attaquer ici.")
        else:
            
            print(f" tu attaques le {room.enemy.name} avec {self.name} et infliges {self.damage} points de dégâts !")

class Bible(Item):
    def __init__(self, name, description, weight):
        super().__init__(name, description, weight)
        pages_avant = ["page vide" for i in range(1908)]
        
        page_speciale = ["2807"]

        pages_apres = ["page vide" for i in range(91)]

        self.pages = pages_avant + page_speciale + pages_apres

    def use_item(self, game):
        which_page = input("À quelle page voulez-vous aller ? ")
        number_of_page = int(which_page)

        
        if 0 <= number_of_page < len(self.pages):
            print(f"Contenu de la page {number_of_page} : {self.pages[number_of_page]}")
        else:
            print("Cette page n'existe pas.")
class Key(Item):
    def __init__(self, name, description, weight):
        super().__init__(name, description, weight)
        
    def use_item(self,game):
        if game.player.current_room.name!="Sanders_street":
            print("""Vous ne pouvez pas utiliser la clé menant au cinéma à cet endroit là.
                     Veuillez vous rendre au niveau de Sanders street pour ouvrir la porte du cinéma.""")
            return False
        
        
        cinema.locked=False
        print("la porte du cinéma est maintenant ouverte !\n")
        return True
        
                     
                  
    
     
     
            

    
            
            
        
