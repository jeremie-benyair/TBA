from quest import QuestManager
# Define the Player class.
class Player():
    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.historique = []
        self.inventory={}
        self.equipped_item= None
        self.max_weight=2.5
        self.health_stat=100
        self.rewards = []
        self.quest_manager = QuestManager(self)
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
        if self.inventory == {}:
            return "Votre inventaire est vide."
        else:
            texte = "Vous disposez des items suivants :\n"
            for item in self.inventory.values():
    
                from item import Medkit
                if isinstance(item, Medkit) and item.number > 1:
                    texte += f"  - {item.name} (x{item.number})\n"
                else:
                    texte += f"  - {item.name}\n"
                
            return texte

             
    def add_reward(self, reward):
        """
        Add a reward to the player's rewards list.
        
        Args:
            reward (str): The reward to add.
            
        Examples:
        
        >>> player = Player("Bob")
        >>> player.add_reward("Épée magique") # doctest: +NORMALIZE_WHITESPACE
        <BLANKLINE>
        🎁 Vous avez obtenu: Épée magique
        <BLANKLINE>
        >>> "Épée magique" in player.rewards
        True
        >>> player.add_reward("Épée magique") # Adding same reward again
        >>> len(player.rewards)
        1
        """
        if reward and reward not in self.rewards:
            self.rewards.append(reward)
            
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
    def show_rewards(self):
        """
        Display all rewards earned by the player.
        
        Examples:
        
        >>> player = Player("Charlie")
        >>> player.show_rewards() # doctest: +NORMALIZE_WHITESPACE
        <BLANKLINE>
        🎁 Aucune récompense obtenue pour le moment.
        <BLANKLINE>
        >>> player.add_reward("Bouclier d'or") # doctest: +NORMALIZE_WHITESPACE
        <BLANKLINE>
        🎁 Vous avez obtenu: Bouclier d'or
        <BLANKLINE>
        >>> player.show_rewards() # doctest: +NORMALIZE_WHITESPACE
        <BLANKLINE>
        🎁 Vos récompenses:
        • Bouclier d'or
        <BLANKLINE>
        """
        if not self.rewards:
            print("\n🎁 Aucune récompense obtenue pour le moment.\n")
        else:
            print("\n🎁 Vos récompenses:")
            for reward in self.rewards:
                print(f"  • {reward}")
            print()
    def total_weight(self): 
        return sum(item.weight * getattr(item, "number", 1) for item in self.inventory.values())



    
