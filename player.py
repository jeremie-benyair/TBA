# Define the Player class.
class Player():
    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.historique = []
        self.inventory={"beamer"}
        self.arme_equipé= None
        self.max_weight=2

    def get_history(self):
        if not self.historique:
            return "Aucun lieu visité pour le moment."

        texte = "Historique des lieux visités :\n"
        for i, lieu in enumerate(self.historique, start=1):
            texte += f"{i}. {lieu.name}\n"
        return texte

    def move(self, direction):
        next_room = self.current_room.exits.get(direction)

        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False

        self.current_room = next_room
        self.historique.append(next_room)

        print(self.current_room.get_long_description())
        print(self.get_history())

        return True
    def get_inventory(self):
        if  self.inventory=={}:
            return "Votre inventaire est vide."
        else:
            texte = "Vous disposez des items suivants :\n"
            for item in self.inventory.values():
                texte += f"  - {item}\n"
            return texte
             
    
    def back(self):
        if len(self.historique) < 2:
            print("\nImpossible de revenir en arrière.\n")
            return False
        self.historique.pop()
        previous_room = self.historique[-1]
        self.current_room = previous_room
        print(self.current_room.get_long_description())
        print(self.get_history())

        return True



    
