# Define the Player class.
class Player():
    # Define the constructor.
    def __init__(self, name,inventory):
        self.name = name
        self.current_room = None
        self.historique = []

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
        if self.inventory=={}:
            return "votre inventaire est vide."
        else :
            return f"vous disposez des items suivants :\n"
            for item in self.inventory.keys():
                print(item)


    
