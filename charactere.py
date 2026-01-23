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

        # 50% de chance de bouger
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

    

