# Define the Room class.



class Room:
    
    """
    Cette classe représente une salle dans le jeu. Chaque salle possède un nom,
    une description et un ensemble de sorties menant vers d'autres salles.

    Attributs :
            name (str) = le nom de la salle
            description (str) = la description textuelle de la salle
            exits (dict) = un dictionnaire associant une direction (str) à une salle (Room)

    Méthodes :
            __init__(self, name, description) = le constructeur
            get_exit(self, direction) = retourne la salle associée à une direction
            get_exit_string(self) = retourne une chaîne listant les sorties disponibles
            get_long_description(self) = retourne une description complète de la salle

    Exemples :
            >>> from room import Room
            >>> forest = Room("Forest", "dans une forêt enchantée.")
            >>> cave = Room("Cave", "dans une grotte sombre.")
            >>> forest.exits = {"N": cave, "E": None, "S": None, "O": None}
            >>> cave.exits = {"S": forest, "N": None, "E": None, "O": None}

            >>> forest.name
            'Forest'
            >>> forest.description
            'dans une forêt enchantée.'

            >>> forest.get_exit("N").name
            'Cave'
            >>> forest.get_exit("E") is None
            True

            >>> forest.get_exit_string()
            'Sorties: N'

            >>> forest.get_long_description()
            '\\nVous êtes dans une forêt enchantée.\\n\\nSorties: N\\n'
    """



    # Define the constructor. 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
    
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"
