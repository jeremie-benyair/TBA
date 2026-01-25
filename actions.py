from item import Key
key_cinema = Key("clé", "Une clé rouillée du cinéma", weight=0.1)

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
            
        #next_room=game.player.current_room.exits[direction]#
        next_room = game.player.current_room.exits.get(direction)
        if next_room is None: 
            print("Il n’y a pas de sortie dans cette direction.") 
            return False
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
        Affiche la liste des commandes disponibles avec leur description.
        """
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(f"❌ La commande '{command_word}' attend {number_of_parameters} paramètre(s).")
            return False

        print("\n📜 Voici les commandes disponibles :\n")
        for command in game.commands.values():
            print(f"\t- {command.name}{command.description}")
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
        # Vérifie si la piece est sombre
        if getattr(room, "darked", False): 
            equipped = game.player.equipped_item 
            if not equipped or equipped.name != "flashlight" or not getattr(equipped, "on", False): 
                print("Il fait trop sombre ici... Vous ne pouvez rien distinguer sans lumière.") 
                return True

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


    def take(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
    
        objet = list_of_words[1]
        room = game.player.current_room
    
        
        if objet not in room.inventory:
            print("Cet objet n'est pas dans cette pièce\n")
            return False
    
        item = room.inventory[objet]  
    
        # Vérifie le poids
        poids_total = game.player.total_weight()
        poids_objet = item.weight
    
        if poids_total + poids_objet > game.player.max_weight:
            print("Vous ne pouvez pas prendre cet objet : votre inventaire est plein.\nPour libérer de l'espace, tapez : drop <objet>\n")
            return False
    
        # Gestion spéciale pour les MedKit
        from item import MedKit
        if isinstance(item, MedKit):
            if objet in game.player.inventory:
                game.player.inventory[objet].number += 1
            else:
                item.number = 1
                game.player.inventory[objet] = item
        else:
            game.player.inventory[objet] = item
    
        print(f"L'item {item.name} a été ajouté à votre inventaire\n")
        del room.inventory[objet]
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
            
            from item import MedKit 
            for item in game.player.inventory.values(): 
                if isinstance(item, MedKit) and item.number > 1: 
                    print(f" - {item.name} (x{item.number})") 
                else: print(f" - {item.name}")
            
            print("""\n rappel des commandes : 
            "read <item>" : lire le contenu d'un objet s'il est lisible.
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
    
        target_name = list_of_words[1].lower()
        room = game.player.current_room
    
        if not room.characters:
            print("\nIl n'y a personne à qui parler ici.\n")
            return False
    
        for pnj in room.characters:
            if pnj.name.lower() == target_name:
                # Cas spécial : barman
                if pnj.name.lower() == "barman":
                    print("Barman : Tu veux jouer au juste prix ?\n1. Oui\n2. Non")
                    choix = input("> ").strip()
                    if choix == "1":
                        quest = game.player.quest_manager.get_quest_by_title("Réussir le défi du barman") 
                        if not quest: 
                            from quest import Quest 
                            quete_barman = Quest( "Réussir le défi du barman", "Devinez le nombre que le barman a en tête compris entre 1 et 100, objectives=["Trouver le juste prix"], reward="Indice : 28" ) 
                            game.player.quest_manager.add_quest(quete_barman) 
                            game.player.quest_manager.activate_quest("Réussir le défi du barman") 
                            print("🗝️ Nouvelle quête activée : Réussir le défi du barman")
                        if game.barman_found:
                            print("Barman : Tu as déjà trouvé le bon prix. Tu veux rejouer ? Trop tard.")
                            return True
                        if game.barman_found and ("Tuer un monstre" not in quest.objectives):
                            print(" 'Tu as déjà joué. Va tuer un monstre si tu veux rejouer.\n' ")
                        
                        game.barman_game_active = True
                        game.barman_attempts = 0
                        print("Très bien. Devine le prix exact de la bouteille de whisky.")
                        print("C’est un nombre entre 1 et 100. Tu as 7 essais.")
                        print("Tape simplement un nombre pour jouer.")
                        game.player.quest_manager.activate_quest("Réussir le défi du barman")
                    else:
                        print("Barman : Tant pis, une autre fois peut-être.")
                    return True
    
                # Dialogue normal
                print(pnj.get_msg())
    
                if not pnj.has_spoken:
                    pnj.has_spoken = True
                    if pnj.name.lower() == "fillette":
                        if not game.player.quest_manager.get_quest_by_title("Retrouver le doudou"): 
                            from quest import Quest 
                            quete_doudou = Quest( "Retrouver le doudou", "La fillette a perdu son doudou. Retrouvez-le et ramenez-le-lui.", objectives=[], reward="Clé du cinéma" ) 
                            game.player.quest_manager.add_quest(quete_doudou) 
                            game.player.quest_manager.activate_quest("Retrouver le doudou")
                       
    
                return True
    
            print(f"\nIl n'y a pas de personnage nommé '{target_name}' ici.\n")
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
        return True

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

        
        if item_name == "doudou" and "parc" in room.name.lower():
            print("\n'Merci beaucoup ! Tiens, j'ai trouvé ça, ça pourrait te servir.'")
            print("la fillette est partie.\n")
            game.player.inventory["clé"]=key_cinema
            

            del player.inventory["doudou"]
            player.add_reward("Clé du cinéma")
            #player.quest_manager.complete_quest("Retrouver le doudou")#
            player.quest_manager.get_quest_by_title("Retrouver le doudou").complete_quest(player)

            #player.quest_manager.complete_objective("Retrouver le doudou", "Donner le doudou à la fillette")#
            print("la clé a été ajouté à votre inventaire.\n")


            # Optionnel : retirer la fillette si tu veux qu’elle disparaisse
            room.characters = [pnj for pnj in room.characters if "fillette" not in pnj.name.lower()]

            return True

        print("Il n'y a personne ici à qui donner ça.")
        return False

   
        

       

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


        
                

            
                
            

        
        
        
        
            
            

            
        
            
            

