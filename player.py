# Define the Player class.
class Player():
    """
    Cette classe représente le joueur. Elle prend comme un variable le prénom du joueur et est composé de plusieurs attributs et de plusieurs méthodes.

    Attributs : 
            name(str)= le nom du joueur
            current_room(str)= la salle où se trouve le joueur
    
    Méthodes :
            __init__(self,name)= le constructeur 
            move(self,name)= la méthode permettant de faire bouger le joueur
    Exemples : 
            >>> from player import Player
            >>> from room import Room
            >>> forest = Room("Forest", "dans une forêt enchantée.")
            >>> cave = Room("Cave", "dans une grotte sombre.")
            >>> forest.exits = {"N": cave, "E": None, "S": None, "O": None}
            >>> cave.exits = {"S": forest, "N": None, "E": None, "O": None}
            >>> player = Player("Jérémie")
            >>> player.name
            'Jérémie'
            >>> player.current_room = forest
            >>> player.current_room.name
            'Forest'
            >>> player.move("N")
            '\nVous êtes dans une grotte sombre.\n\nSorties: S\n'
            True
            >>> player.move("E")
            '\nAucune porte dans cette direction !\n'
            False

    

   





    """


    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
    
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True

    