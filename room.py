# Define the Room class.

class Room:

    # Define the constructor. 
    def __init__(self, name, description,darked=False):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory={}
        self.darked=darked
    
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
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"
   
    
    def get_inventory(self):
         
        if self.inventory=={}:
            return "il n'y a rien ici."
        else :
            texte="la pièce contient : \n"
            for item in self.inventory.values():
                texte+=f"    -{item}"
           
