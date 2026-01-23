# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.


# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

class Actions:

    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False

        """
        
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the direction from the list of words.
        direction = list_of_words[1].lower()
        direction_alternatives={ "o": "O", "ouest": "O", "est": "E", "e": "E", "n": "N", "nord": "N", "s": "S", "sud": "S" }
        if direction in direction_alternatives: 
            direction = direction_alternatives[direction]
            
        next_room=game.player.current_room.exits[direction]
        if next_room.locked: 
            next_room.on_locked_attempt(player) 
            return False
        
            
        # Move the player in the direction specified by the parameter.
        player.move(direction)
        return True

    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True
    def history(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        print("\n" + game.player.get_history())
        return True

    def back(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        return game.player.back()
    def look(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        room = game.player.current_room

        # Objets
        if not room.inventory:
            print("\nAucun objet n'est disponible ici.\n")
        else:
            print("\nVoici les objets disponibles dans cette pièce :\n")
            for item in room.inventory.values():
                print(f"      - {item.name}")

        # PNJ
        if room.characters:
            print("\nPersonnages présents :\n")
            for c in room.characters:
                print(f"      - {c.name} : {c.description}")
        else:
            print("\nAucun personnage ici.\n")
    
        return True


    def take(game,list_of_words,number_of_parameters):
        l=len(list_of_words)
        if l!=number_of_parameters + 1:
            command_word=list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        elif list_of_words[1] not in game.player.current_room.inventory:
            print("Cet objet n'est pas dans cet pièce\n")
        else:
            objet=list_of_words[1]
            game.player.inventory[objet]=game.player.current_room.inventory[objet]
            print(f"L'item {game.player.current_room.inventory[objet].name} a été ajouté à votre inventaire\n")
            del game.player.current_room.inventory[objet]
        return True


    def drop(game,list_of_words,number_of_parameters):
        l=len(list_of_words)
        if l!=number_of_parameters + 1:
            command_word=list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        elif list_of_words[1] not in game.player.inventory:
            print("Cet objet n'est pas dans votre inventaire\n")
        else:
            objet=list_of_words[1]
            
            game.player.current_room.inventory[objet]=game.player.inventory[objet]
            del game.player.inventory[objet]
            print(f"L'item a été retiré de votre inventaire et déposé sur le sol.\n")
        return True
        
    def check(game,list_of_words,number_of_parameters):
        l=len(list_of_words)
        if l!=number_of_parameters + 1:
            command_word=list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        if game.player.inventory=={}:
                print("Aucun objet n'est présent dans votre inventaire.\n")
        else:
            print("Vous avez actuellement dans votre inventaire : \n")
            for item in game.player.inventory.values():
                print (f"        -{item}   ")
            print("""\n rappel des commandes : "read <item>" : lire le contenu d'un objet s'il est lisible.
                                                   "use <item>" : equiper un objet.
                                                   "drop <item>" :  déposer un objet sur le sol.\n
                      """)
                                                
                                               
        return True


    def carry(game,list_of_words,number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        else:
            item_name=list_of_words[1]
            if item_name not in game.player.inventory:
                print("cet objet n'est pas dans votre inventaire.\n")
            else:
                item=game.player.inventory[item_name]
                game.player.equipped_item=item
                print(f"{item.name} est désormais équipé.\n")
                return True
    def talk(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        target_name = list_of_words[1]
        room = game.player.current_room

        if not room.characters:
            print("\nIl n'y a personne à qui parler ici.\n")
            return False

        for pnj in room.characters:
            if pnj.name.lower() == target_name.lower():
                print(f"\n{pnj.name} dit : {pnj.get_msg()}\n")
                return True

        print(f"\nIl n’y a personne nommé '{target_name}' ici.\n")
        return False

            
            
    def use(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        
        if game.player.equipped_item==None:
             print("Aucun objet n'est actuellement équipé.Veuillez d'abord équiper l'arme de votre choix avec la commande carry <item> \n")
             return False
         
        
        item = game.player.equipped_item
                
                
        item.use_item(game)

    def read(game, list_of_words, number_of_parameters):
        
        player = game.player
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        item_name = list_of_words[1]

        if item_name not in player.inventory:
            print(f"Vous n'avez pas {item_name} dans votre inventaire.")
            return False

        item = player.inventory[item_name]

        if item.text is None:
            print(f"Vous ne pouvez pas lire {item_name}.")
            return False

       
        print(item.text)

    def give(game, list_of_words, number_of_parameters):
        player = game.player
        room = player.current_room
 
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
    

        item_name = list_of_words[1].lower()
    
        
        if item_name not in player.inventory:
            print("Tu n'as pas cet objet.")
            return False
    
        #  CAS SPÉCIAL : DONNER LE DOUDOU À LA FILLETTE 
        if item_name == "doudou" and room.name.lower() == "parc":
    
            
            fillette = None
            for pnj in room.characters:
                if pnj.name.lower() == "fillette":
                    fillette = pnj
                    break
    
            if fillette is None:
                print("Il n'y a personne ici à qui donner ça.")
                return False
    
           
            print("\nLa fillette dit : 'Merci beaucoup ! Tiens, j'ai trouvé ça, ça pourrait te servir.'")
            
            del player.inventory["doudou"]
    
            player.add_reward("Clé du cinéma")
        
            player.quest_manager.complete_quest("Retrouver le doudou")
            room.characters.remove(fillette)
    
            return True

   
        print("Il n'y a personne ici à qui donner ça.")
        return False

       

        return True
    def quests(game, list_of_words, number_of_parameters):
        """
        Show all quests and their status.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.quests(game, ["quests"], 0)
        <BLANKLINE>
        📋 Liste des quêtes:
          ❓ Grand Explorateur (Non activée)
          ❓ Grand Voyageur (Non activée)
          ❓ Découvreur de Secrets (Non activée)
        <BLANKLINE>
        True
        >>> Actions.quests(game, ["quests", "param"], 0)
        <BLANKLINE>
        La commande 'quests' ne prend pas de paramètre.
        <BLANKLINE>
        False

        """
        # If the number of parameters is incorrect, print an error message and return False.
        n = len(list_of_words)
        if n != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Show all quests
        game.player.quest_manager.show_quests()
        return True


    @staticmethod
    def quest(game, list_of_words, number_of_parameters):
        """
        Show details about a specific quest.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.quest(game, ["quest", "Grand", "Voyageur"], 1)
        <BLANKLINE>
        📋 Quête: Grand Voyageur
        📖 Déplacez-vous 10 fois entre les lieux.
        <BLANKLINE>
        Objectifs:
          ⬜ Se déplacer 10 fois (Progression: 0/10)
        <BLANKLINE>
        🎁 Récompense: Bottes de voyageur
        <BLANKLINE>
        True
        >>> Actions.quest(game, ["quest"], 1)
        <BLANKLINE>
        La commande 'quest' prend 1 seul paramètre.
        <BLANKLINE>
        False

        """
        # If the number of parameters is incorrect, print an error message and return False.
        n = len(list_of_words)
        if n < number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the quest title from the list of words (join all words after command)
        quest_title = " ".join(list_of_words[1:])

        # Prepare current counter values to show progress
        current_counts = {
            "Se déplacer": game.player.move_count
        }

        # Show quest details
        game.player.quest_manager.show_quest_details(quest_title, current_counts)
        return True


    @staticmethod
    def activate(game, list_of_words, number_of_parameters):
        """
        Activate a specific quest.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.activate(game, ["activate", "Grand", "Voyageur"], 1) # doctest: +ELLIPSIS
        <BLANKLINE>
        🗡️  Nouvelle quête activée: Grand Voyageur
        📝 Déplacez-vous 10 fois entre les lieux.
        <BLANKLINE>
        True
        >>> Actions.activate(game, ["activate"], 1)
        <BLANKLINE>
        La commande 'activate' prend 1 seul paramètre.
        <BLANKLINE>
        False

        """
        # If the number of parameters is incorrect, print an error message and return False.
        n = len(list_of_words)
        if n < number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the quest title from the list of words (join all words after command)
        quest_title = " ".join(list_of_words[1:])

        # Try to activate the quest
        if game.player.quest_manager.activate_quest(quest_title):
            return True

        msg1 = f"\nImpossible d'activer la quête '{quest_title}'. "
        msg2 = "Vérifiez le nom ou si elle n'est pas déjà active.\n"
        print(msg1 + msg2)
        # print(f"\nImpossible d'activer la quête '{quest_title}'. \
        #             Vérifiez le nom ou si elle n'est pas déjà active.\n")
        return False


    @staticmethod
    def rewards(game, list_of_words, number_of_parameters):
        """
        Display all rewards earned by the player.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.rewards(game, ["rewards"], 0)
        <BLANKLINE>
        🎁 Aucune récompense obtenue pour le moment.
        <BLANKLINE>
        True
        >>> Actions.rewards(game, ["rewards", "param"], 0)
        <BLANKLINE>
        La commande 'rewards' ne prend pas de paramètre.
        <BLANKLINE>
        False
        """
        # If the number of parameters is incorrect, print an error message and return False.
        n = len(list_of_words)
        if n != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Show all rewards
        game.player.show_rewards()
        return True


        
                

            
                
            

        
        
        
        
            
            

            
        
            
            

