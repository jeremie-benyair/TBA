class Item():
    def __init__(self,name,description,weight,text=None,type=None):
        self.name=name
        self.description=description
        self.weight=weight
        self.text=text 
        
        self.type=type
    def __str__(self):
        return f"{self.name} : {self.description} ({self.weight} kg)\n"
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
               
                print(game.player.current_room.get_long_description())
                
                
                game.player.add_reward("Indice : 05")
                print("🎁 Récompense : Indice : 05\n") 
                
        else:
            print("lampe éteinte.\n")
class Beamer(Item):
    def __init__(self,name,description,weight):
        super().__init__(name,description,weight)
    def use_item(self,game):  
        which_room=input("choisissez un lieu parmi ceux déjà visité.\n").strip().lower()
        if which_room not in [room.name.lower() for room in game.player.historique]:
            print("vous n'avez pas encore visité ce lieu, vous ne pouvez donc pas vous y déplacer.\n")
            return
        for room in game.rooms:    
            if room.name.lower() == which_room: 
                game.player.current_room = room 
                print(f"✨ Téléportation vers {room.name} réussie !") 
                print(room.get_long_description()) 
                return 
        print("❌ Salle introuvable malgré l'historique. Vérifiez le nom.")

class Weapon(Item):
    def __init__(self, name, description, weight, damage):
        super().__init__(name, description, weight)
        self.damage = damage
        self.type = "weapon"

    def use_item(self, game):
        player = game.player
        room = player.current_room
    
        # Vérifie que l'objet est une arme
        if self.type != "weapon":
            print(f"{self.name} ne peut pas être utilisée comme une arme.")
            return
    
        # Cherche un monstre vivant dans la pièce
        for c in room.characters:
            if c.role == "monster":
                
                print(c.take_damage(self.damage))
    
                
                import random
                if c.is_alive() and random.random() < 0.33:
                    print(f"{c.name} contre-attaque !")
                    c.attack_player(player)
                    
                return
    
        print("Il n’y a aucun monstre à attaquer ici.")


class Bible(Item):
    def __init__(self, name, description, weight):
        super().__init__(name, description, weight)
        pages_avant = ["page vide" for i in range(1908)]
        
        page_speciale = ["07"]

        pages_apres = ["page vide" for i in range(91)]

        self.pages = pages_avant + page_speciale + pages_apres

    def use_item(self, game):
        which_page = input("À quelle page voulez-vous aller ?\n (retapez use à chaque fois pour accéder à une nouvelle page)")
        number_of_page = int(which_page)

        
        if 0 <= number_of_page < len(self.pages):
            print(f"Contenu de la page {number_of_page} : {self.pages[number_of_page]}")
        else:
            print("Cette page n'existe pas.")
class Key(Item):
    def __init__(self, name, description, weight):
        super().__init__(name, description, weight)
        
    def use_item(self,game):
        if game.player.current_room.name!="Sanders Street":
            print("""Vous ne pouvez pas utiliser la clé menant au cinéma à cet endroit là.
                     Veuillez vous rendre au niveau de Sanders street pour ouvrir la porte du cinéma.""")
            return False
        for room in game.rooms:
            if room.name == "Cinéma abandonné":
                cinema_room = room

        
        
        cinema_room.locked=False
        print("la porte du cinéma est maintenant ouverte !\n")
        return True
        
class MedKit(Item):
    def __init__(self, name, description, weight,health_point=25,number=1):
        super().__init__(name, description, weight)
        self.health_point=health_point
        self.number=number

    def use_item(self, game): 
        player = game.player 
        # Si la vie est déjà pleine 
        if player.health == 100: 
            print("Votre barre de vie est déjà à 100%.") 
            return False 
            
        before = player.health 
        player.health = min(100, player.health + self.health_point) 
        healed = player.health - before 
        print(f"Vous utilisez une trousse de soins et récupérez {healed} points de vie.") 
        print(f"Votre santé est maintenant de {player.health/100}%.") 
        
        
        self.number -= 1
        if self.number <= 0: 
            del player.inventory[self.name]
        return True
        
        
        
        
    
                  
    
     
     
            

    
            
            
        
