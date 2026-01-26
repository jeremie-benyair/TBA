# Define the Room class.

class Room:

    # Define the constructor. 
    def __init__(self, name, description,darked=False, locked=False):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory={}
        self.darked=darked
        self.characters=[]
        self.locked=locked
        
    
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Issues possibles : " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        if self.darked:
            return "\nIl fait trop sombre ici... Trouvez un moyen d'éclairer la pièce pour pouvoir la découvrir.\n"
    
        description = f"\nVous êtes dans {self.name}\n{self.description}\n\n{self.get_exit_string()}\n"
    
        if self.characters:
            description += "\nPersonnages présents :\n"
            for c in self.characters:
                description += f" - {c.name} : {c.description}\n"
    
        return description



       
    
    def get_inventory(self):
         
        if self.inventory=={}:
            return "il n'y a rien ici."
        else :
            texte="la pièce contient : \n"
            for item in self.inventory.values():
                texte+=f"    -{item}"
            return texte
    
    def on_locked_attempt(self, player,game): 
        print("Cette porte est verrouillée... ")


class Cinema(Room): 
         def on_locked_attempt(self, player,game): 
             #print("il semblerait que la porte du cinéma soit verrouillée.")#
             print("""Cette porte est verrouillée...par une serrure : Trouvez la clé, équipez-la puis utilisez-la.\n""")
class Cave(Room): 
         def on_locked_attempt(self, player,game): 
             #print("La porte de la cave est verrouillée par un digicode : tapez le code directement si vous pensez avoir la réponse ou tapez <quit> si vous ne voulez plus interragir avec le digicode \n ") 
             print("Cette porte est verrouillée...par un digicode : tapez le code directement si vous pensez avoir la réponse ou \ntapez <quit> si vous ne voulez plus interragir avec le digicode. \nVous avez 10 essais maximum. Au delà de ces 10 essais, vous perdez la partie. ")
             compteur=0
             while True:
                code = input("Entrez le code : ") 
                if code==("quit"):
                     print("Vous abandonnez pour le moment.")
                     return 
                
                if "28" in code and "05" in code and "07" in code:
                     print("La porte s'ouvre ! Vous pouvez maintenant rentrer dans ce lieu.") 
                     self.locked = False 
                     return 
                print("code incorrect : réessayez ou taper <quit> pour arrêter vos tentatives.")
                compteur+=1
                if compteur==10:
                    print("Vous avez atteint votre nombre de tentatives maximums...\nLa cave se met à exploser...vous entendez des cris d'agonie : votre femme périt.\n")
                    game.loose()
                print(f"il vous reste {10-compteur} essais avant de perdre complètement la partie.\n")
                
                 
                 

                     
                     
                    
                     
                 
             
             
            
              
                     
               
      
           
