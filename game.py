# Description: Game class

# Import modules

from room import Room
from room import Cinema
from room import Cave
from player import Player
from command import Command
from actions import Actions
from item import Item
from item import Flashlight
from item import Weapon
from item import Beamer
from item import Bible
from item import Key
from item import MedKit
from charactere import Charactere
from quest import Quest

DEBUG = True
class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.barman_secret = 28  
        self.barman_attempts = 0 
        self.barman_game_active = False 
        self.barman_found = False

    # Setup the game
    def setup(self):


        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O) ou <sortie>", Actions.go, 1)
        #modif au dessus
        self.commands["go"] = go
        history = Command("history", " : afficher l'historique des lieux visités", Actions.history, 0)
        self.commands["history"] = history
        back = Command("back", " : revenir à la salle précédente", Actions.back, 0)
        self.commands["back"] = back
        look=Command("look"," : afficher tous les items présents dans la pièce s'il y en a",Actions.look,0)
        self.commands["look"]=look
        take=Command("take"," : prendre et ajouter un objet à son inventaire parmi tous les objets présents dans un lieu",Actions.take,1)
        self.commands["take"]=take
        drop=Command("drop"," : se débarasser d'un objet de son inventaire et le déposer dans le lieu où se trouve le joueur",Actions.drop,1)
        self.commands["drop"]=drop
        check=Command("check"," : jeter un oeil à son inventaire",Actions.check,0)
        self.commands["check"] = check 
        carry=Command("carry"," <objet>  équiper un objet présent dans votre inventaire.",Actions.carry,1 )
        self.commands["carry"]=carry
        use=Command("use"," : utiliser l'objet équipé.",Actions.use,0)
        self.commands["use"]=use

        talk = Command("talk", " <someone> : parler à un personnage non joueur", Actions.talk, 1)
        self.commands["talk"] = talk
        read=Command("read"," <objet> : lire un objet lisible présent dans votre inventaire",Actions.read,1)
        self.commands["read"]=read
        give= Command("give","<objet> : donner un objet à un pnj.",Actions.give,1)
        self.commands["give"]=give


        # Setup rooms

        # Setup rooms

        # Setup rooms

        Neely_street = Room("Neely Street", "Une rue déserte enveloppée de brouillard.\nÀ l’est se trouve l’hôtel abandonné, à l’ouest le parc pour enfants.\nAu nord, la rue mène vers le croisement central.")
        self.rooms.append(Neely_street)
        cinema = Cinema("Cinéma abandonné", "Un vieux cinéma plongé dans l’obscurité.\nLes sièges éventrés et l’odeur de poussière donnent l’impression que le temps s’est arrêté.", darked=True, locked=True)
        self.rooms.append(cinema)
        hotel = Room("Hotel abandonné", "Un hall silencieux où le papier peint se décolle des murs.\nLe comptoir d’accueil est renversé, et un courant d’air froid traverse la pièce.")
        self.rooms.append(hotel)
        parc = Room("Parc pour enfants abandonné", "Un parc désert où les balançoires grincent sous un vent invisible.\nLes jouets rouillés semblent t’observer.")
        self.rooms.append(parc)
        bar = Room("Bar", "Un bar délabré où les bouteilles brisées jonchent le sol.\nUne odeur d’alcool rance flotte encore dans l’air.")
        self.rooms.append(bar)
        pharma = Room("Pharmacie", "Des étagères renversées et des boîtes de médicaments éventrées.\nLe néon au plafond clignote faiblement.")
        self.rooms.append(pharma)
        croisement = Room("intersection", "Un croisement désert où le brouillard semble plus dense.\nAu nord se trouve Sanders Street, à l’est Lindsey Street, à l’ouest Martin Street.\nAu sud Neely Street.")
        self.rooms.append(croisement)
        Martin_street = Room("Martin Street", "Une rue étroite bordée de maisons abandonnées.\nÀ l’ouest se trouve le parc pour enfants, au nord l’église abandonnée.\nAu sud le croisement.")
        self.rooms.append(Martin_street)
        Lindsey_street = Room("Lindsey_Street", "Une longue rue plongée dans la brume.\nÀ l’est se trouve la bibliothèque, à l’ouest la pharmacie.\nAu sud le croisement.")
        self.rooms.append(Lindsey_street)
        Sanders_street = Room("Sanders Street", "Une rue sombre où les lampadaires sont tous brisés.\nÀ l’est se trouve le cinéma abandonné, à l’ouest le bar.\nAu sud le croisement.")
        self.rooms.append(Sanders_street)
        biblio = Room("bibliothèque", "Une bibliothèque silencieuse où les livres sont éparpillés au sol.\nL’odeur de papier humide envahit la pièce.")
        self.rooms.append(biblio)
        eglise = Room("église abandonnée", "Une église délabrée où les vitraux sont brisés.\nUne atmosphère lourde et sacrée persiste malgré l’abandon.")
        self.rooms.append(eglise)
        etage = Room("1er étage", "Un étage poussiéreux où le parquet craque sous tes pas.\nLes portes sont entrouvertes, comme si quelqu’un venait de passer.")
        self.rooms.append(etage)
        chambre_1 = Room("chambre_1", "Une petite chambre plongée dans le noir.\nLes meubles sont renversés et un miroir fissuré reflète ton ombre.", darked=True)
        self.rooms.append(chambre_1)
        chambre_2 = Room("chambre_2", "Une chambre froide et silencieuse.\nLe lit est défait, comme si quelqu’un l’avait quitté précipitamment.")
        self.rooms.append(chambre_2)
        cave = Cave("cave", "Une cave humide et obscure.\nL’air y est glacial et un goutte-à-goutte résonne dans le silence.", locked=True)
        self.rooms.append(cave) 

        #setup pnj

        quete_doudou = Quest( "Retrouver le doudou", "La fillette a perdu son doudou. Retrouvez-le et ramenez-le-lui.", objectives=[], reward="Clé du cinéma" )
        fillette = Charactere("fillette","Une petite fille apeurée.",parc,["Tu n'aurais pas vu mon doudou ?","Depuis que la brume est arrivée, tout le monde a disparu… même maman. Et puis… des monstres ont commencé à sortir de l’ombre."],role="static")
        parc.characters.append(fillette)
        barman = Charactere( "barman", "Un homme au regard fatigué, essuyant un verre sale derrière le comptoir.", bar, ["Tu veux un verre ?"] ) 
        bar.characters.append(barman)
        quete_barman = Quest( "Réussir le défi du barman", "Devinez le nombre que le barman a en tête comprit entre 1 et 100 en 9 essais maximum.\nEn cas d’échec, trouvez un objet spécial pour retenter votre chance.", objectives=["Trouver le juste prix"], reward="Indice : 28" ) 
       
        


        #setup items
        map=Item("map","carte officielle du centre-ville de Silent Hill" ,0 ,
                 """
        

         
                
                            _________________   |        |        |  _________________
                            |               |   |                 |  |               |
                            |   bar         |   |        |        |  |  cinéma       |   ____________________         
                            |               |   |     Sanders     |  |               |  |                   |
                            –––––––––––––––––   |     Streets     |  |               |  |    Pharmacie      |
           ––––––––––––––––––––––––––––––––––   |        |        |  –––––––––––––––––--|                   |
    _|_    |_________________________________|  |                 | |___________________|___________________|_______________                                           
     |     –––––––––––––––––––––––––––––––––––––|        |        |–––––––––––––––––––––––––––––––––––––––––––––––––––––––––
––––––––––
| église |
|________|    --   --Martin Street-   __   __   __                 __   __   __   __   _ Lindsey Street  __   __   __   __   

                                            
           ––––––––––––––––––––––––––––––––––––––                 –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
                     - - - - - - - - - - - - -   |       |        | ---------------------------------------------------------
                     |                       |   |                | |_______________________________________________________|
                     |                       |   |       |        | 
                     |                       |   |     Neely      |  _______________________________
                     |    parc               |   |       |        | |                               |
                     |    pour enfants       |   |     Street     | |                               |                              
                     |                       |   |       |        | |                               |
                     |                       |   |                | |        hôtel                  |
                     |                       |   |       |        | |                               |
                     - - - - - - - - - - - - -   |                | |                               |
                                                 |       |        | |                               |
                                                 |                |  --------------------------------     
                                
                 
                                    
        
                """,type="text")
        chambre_2.inventory["map"]=map
        flyer=Item("flyer", "tract promotionnel de la ville de Silent Hill provenant de l'office de tourisme",0,
                   """
        ----------------------------------------------------------
                        BIENVENUE À SILENT HILL !
        ----------------------------------------------------------

        Située entre lacs et collines, Silent Hill est une charmante 
        petite ville américaine réputée pour son calme, sa nature et 
        son accueil chaleureux.

        À NE PAS MANQUER :
        - Le cinéma de Sanders Street, un bâtiment historique récemment 
          restauré, apprécié pour son ambiance retro et ses projections format pellicule !
          
        - Le Grand Parc Municipal, vaste espace vert familial, idéal pour 
          les promenades, pique-niques et jeux d’enfants. Très prisé durant 
          l’été, il accueille régulièrement des animations pour petits et grands.

        - L’église Saint Mary’s, construite en 1908, connue pour son 
          architecture traditionnelle et sa jolie cloche visible depuis 
          la place centrale.

        Que vous soyez amateur de nature, d’histoire ou de balades paisibles, 
        Silent Hill vous ouvre ses portes avec le sourire.

        Office de Tourisme — 12 Jefferson Ave, SIlent Hill
                    """,type="text")
        hotel.inventory["flyer"]=flyer
        flashlight=Flashlight("flashlight","lampe-torche servant à éclairer des pièces.",0.25)
        chambre_2.inventory["flashlight"]=flashlight
        batte = Weapon("batte", "Une vieille batte de baseball cloutée", 1.0, damage=10)
        chambre_1.inventory["batte"] = batte
        bible=Bible("bible","une vieille bible étrange qui mériterait qu'on l'examine.",0.3)
        eglise.inventory["bible"]=bible
        
        doudou = Item("doudou", "un petit ours en peluche", 0.15)
        pharma.inventory["doudou"] = doudou
        beamer = Beamer("beamer", "un appareil étrange permettant de se téléporter", 0.5) 
        Neely_street.inventory["beamer"] = beamer
        medkit_parc = MedKit("medkit", "une trousse de soins utile en cas de blessure", 0.35)
        parc.inventory["medkit"] = medkit_parc
        medkit_hotel = MedKit("medkit", "une trousse de soins utile en cas de blessure", 0.35)
        hotel.inventory["medkit"] = medkit_hotel

        














         # Create exits for rooms

        
        bar.exits = {"sortie" :Sanders_street ,"N" : None, "E" : None, "S" : None, "O" : None,"Est": None, "Ouest": None,"Nord": None,"Sud": None,"est": None, "ouest": None,"nord": None,"sud": None}
        cinema.exits = {"sortie" : Sanders_street,"N": None,  "E" : None, "S" : None, "O" : None,"Est": None, "Ouest": None,"Nord": None,"Sud": None,"est": None, "ouest": None,"nord": None,"sud": None}
        eglise.exits = {"sortie" : Martin_street ,"N" : None, "E" : None, "S" : None, "O" : None,"Est": None, "Ouest": None,"Nord": None,"Sud": None,"est": None, "ouest": None,"nord": None,"sud": None}
        parc.exits = {"sortie": Neely_street , "N" : None, "E" : None, "S" : None, "O" : None,"Est": None, "Ouest": None,"Nord": None,"Sud": None,"est": None, "ouest": None,"nord": None,"sud": None}
        Neely_street.exits = {"N" : croisement, "E" : hotel, "S" : None, "O" : parc ,"Est": hotel, "Ouest": parc,"Nord": croisement,"Sud": None,"est": hotel, "ouest": parc,"nord": croisement,"sud": None}
        pharma.exits = {"N" : None, "E" : None, "S" : None, "O" : None,"Est": None, "Ouest": None,"Nord": None,"Sud": None,"est": None, "ouest": None,"nord": None,"sud": None}
        croisement.exits={"N":Sanders_street,"E":Lindsey_street,"O":Martin_street,"S":Neely_street,"Est": Lindsey_street, "Ouest": Martin_street,"Nord": Sanders_street,"Sud": Neely_street,"est": Lindsey_street, "ouest": Martin_street,"nord": Sanders_street,"sud":Neely_street}
        Martin_street.exits={"N":eglise,"S": croisement,"O":parc,"E": None,"Est": None, "Ouest": parc,"Nord": eglise,"Sud": croisement,"est": None, "ouest": parc,"nord": eglise,"sud": None}
        Sanders_street.exits={"N": None,"E": cinema,"O":bar,"S": croisement,"Est": cinema, "Ouest": bar,"Nord": None,"Sud": croisement,"est": cinema, "ouest": bar,"nord": None,"sud": croisement}
        Lindsey_street.exits={"N": None,"E":biblio,"O":pharma,"S":croisement,"Est": biblio, "Ouest": pharma,"Nord": None,"Sud": croisement,"est": biblio, "ouest": pharma,"nord": None,"sud": croisement}
        cave.exits={"sortie":hotel, "N": None,"E":None,"O":None,"S":None,"Est":None, "Ouest":None,"Nord": None,"Sud": None,"est": None, "ouest": None,"nord": None,"sud": None}
        hotel.exits={"sortie":Neely_street,"cave":cave, "étage": etage,"N": None,"E":None,"O":None,"S":None,"Est":None, "Ouest":None,"Nord": None,"Sud": None,"est": None, "ouest": None,"nord": None,"sud": None}
        etage.exits={"chambre_1": chambre_1, "chambre_2": chambre_2,"hotel":hotel}
        chambre_1.exits={"étage":etage}
        chambre_2.exits={"étage":etage}

        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = Neely_street
        self.player.quest_manager.add_quest(quete_doudou)
        self.player.quest_manager.add_quest(quete_barman)

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:

    # Déplacement des PNJ
            for room in self.rooms:
                for pnj in room.characters:
                    pnj.move()
            # Commande du joueur 
            self.process_command(input("> "))



    def process_command(self, command_string) -> None:
        # Bloc spécial : jeu du barman
        if self.barman_game_active and command_string.strip().isdigit():
            nombre = int(command_string.strip())
            self.barman_attempts += 1
    
            if nombre < self.barman_secret:
                print("C’est plus.")
            elif nombre > self.barman_secret:
                print("C’est moins.")
            else:
                print("Bravo ! C’était le bon prix.")
                print("Le barman te glisse à l’oreille : ‘Souviens-toi de ce chiffre… 07.’")
                print("Il ajoute en souriant : ‘Et tiens, pour ta victoire… 28. Ça pourrait t’être utile.’")
                self.player.quest_manager.complete_objective("Réussir le défi du barman", "Trouver le juste prix")
                
                self.barman_game_active = False
                self.barman_found = True
                return
    
            if self.barman_attempts >= 9:
                print(" 'Raté.'Tu as épuisé tes 9 essais.")
                self.barman_game_active = False
                quest = self.player.quest_manager.get_quest_by_title("Réussir le défi du barman")
                if quest and "Ramener l’objet au barman" not in quest.objectives:
                    
                    quest.objectives.append("Ramener l’objet au barman")
                    print("🆕 Nouvel objectif ajouté à la quête : Ramener l’objet au barman")
            return
                    

            
    
        # Traitement normal des commandes
        list_of_words = command_string.split(" ")
        command_word = list_of_words[0]
    
        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)



    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")

        print(self.player.current_room.get_long_description())


def main():
    # Create a game object and play the game
    Game().play()


if __name__ == "__main__":
    main()
