class Charactere:
    def __init__(self, name, description, current_room, msgs):
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs
        self.msg_index = 0


    def __str__(self):
        return f"{self.name} : {self.description} (Salle : {self.current_room.name}) (Messages : {self.msgs})\n"

    def move(self):
        import random

        if random.random() < 0.5:
            return False

        exits = [room for room in self.current_room.exits.values() if room is not None]
        if not exits:
            return False

        next_room = random.choice(exits)

        self.current_room.characters.remove(self)
        next_room.characters.append(self)
        self.current_room = next_room

        return True
    def get_msg(self):
        if not self.msgs:
            return f"{self.name} n'a rien à dire."

        # Retire et récupère le premier message
        msg = self.msgs.pop(0)

        # Le remet à la fin pour créer un cycle
        self.msgs.append(msg)

        return msg

