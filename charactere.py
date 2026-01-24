class Charactere:
    def __init__(self, name, description, current_room, msgs, role="static"):
        """
        role peut être :
        - "static"  : ne bouge pas (fillette, barman, boss)
        - "monster" : PNJ mobile hostile
        - "talker"  : PNJ qui parle mais ne donne pas de quête
        """
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs
        self.role = role
        self.msg_index = 0
        self.has_spoken=False

    def __str__(self):
        return f"{self.name} : {self.description} (Salle : {self.current_room.name})"

    def move(self):
       
        if self.role != "monster":
            return False  # PNJ statique

        import random

        
        if random.random() < 0.2:
            return False

        exits = [room for room in self.current_room.exits.values() if room is not None]
        if not exits:
            return False

        next_room = random.choice(exits)

        # Déplacement
        self.current_room.characters.remove(self)
        next_room.characters.append(self)
        self.current_room = next_room

        return True

    def get_msg(self):
        """Retourne un message cyclique."""
        if not self.msgs:
            return f"{self.name} n'a rien à dire."

        msg = self.msgs.pop(0)
        self.msgs.append(msg)
        return msg

class Monster(Charactere): 
    def __init__(self, name, description, current_room, health=100): 
        super().__init__(name, description, current_room, msgs=[], role="monster") 
        self.health = health 
    def is_alive(self): 
        return self.health > 0 
    def take_damage(self, amount): 
        self.health -= amount 
        if self.health <= 0: 
            self.health = 0 
            return f"{self.name} est vaincu !" 
        return f"{self.name} a encore {self.health} PV." 
    def move(self): 
        if not self.is_alive() or self.health!=100: 
            return False 
        if random.random() >= 0.3: 
            return False 
        exits = [room for room in self.current_room.exits.values() if room is not None] 
        if not exits: 
            return False 
        next_room = random.choice(exits) 
        self.current_room.characters.remove(self) 
        next_room.characters.append(self) 
        self.current_room = next_room 
        return True
    
    def attack_player(self, player):
        if not self.is_alive():
            return
    
        import random
        damage = random.randint(10,25) 
        player.health -= damage
        print(f"{self.name} t’attaque et inflige {damage} points de dégâts !")
    
        if player.health <= 0:
            player.health = 0
            print("Tu t’effondres… Le monstre t’a vaincu.")
            player.game.finished = True 
        else:
            print(f"Il te reste {player.health} points de vie.")

    

