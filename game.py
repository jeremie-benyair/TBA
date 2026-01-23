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


        
        # Setup rooms

        Neely_street= Room("Neely Street"," au niveau de Neely Street ")
        self.rooms.append(Neely_street)
        cinema = Cinema("Cinéma abandonné", " ",darked=True,locked=True)
        self.rooms.append(self.cinema)
        hotel = Room("Hotel abandonné", " ")
        self.rooms.append(hotel)
        parc = Room("Parc pour enfants abandonné", " ")
        self.rooms.append(parc)
        bar= Room("Bar", "")
        self.rooms.append(bar)
        pharma = Room("Pharmacie", " ")
        self.rooms.append(pharma)
        croisement=Room("intersection"," au nord se situe Neely Street, au sud se situe Martin Street, à l'est se situe Lindsey Street et à l'ouest se situe Sanders Street.  ")
        self.rooms.append(croisement)
        Martin_street=Room("Martin Street", " ")
        self.rooms.append(Martin_street)
        Lindsey_street=Room("Lindsey_Street", " ")
        self.rooms.append(Lindsey_street)
        Sanders_street=Room("Sanders Street", " ")
        self.rooms.append(Sanders_street)
        biblio=Room("bibliothèque", " ")
        self.rooms.append(biblio)
        eglise=Room("église abandonnée", " ")
        self.rooms.append(eglise)
        etage=Room("1er étage", " ") 
        self.rooms.append(etage)
        chambre_1=Room("chambre_1", " ",darked=True)
        self.rooms.append(chambre_1)
        chambre_2=Room(" chambre_2", " ")
        self.rooms.append(chambre_2)
        
        cave=Cave("cave", " ",locked=True)
        self.rooms.append(cave)
        #setup pnj
        
        quete_doudou = Quest( "Retrouver le doudou", "La fillette a perdu son doudou. Retrouvez-le et ramenez-le-lui.", objectives=["Trouver le doudou", "Donner le doudou à la fillette"], reward="Clé du cinéma" )
        fillette = Charactere("fillette","Une petite fille apeurée.",parc,["Tu n'aurais pas vu mon doudou ?","Depuis que la brume est arrivée, tout le monde a disparu… même maman. Et puis… des monstres ont commencé à sortir de l’ombre."],role="static")
        self.player.quest_manager.add_quest(quete_doudou)

        

        
        
        pnj_2 = Charactere( "pnj_2","description",cinema,["phrase 1", "phrase 2"])
        cinema.characters.append(pnj_2)
        pnj_3 = Charactere( "pnj_3","description",hotel,["phrase 1", "phrase 2"])
        hotel.characters.append(pnj_3)


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
        key_cinema=Key("clé"," la clé menant au cinéma trouvé par une fillette mystérieuse. ",0.1)
        doudou = Item("doudou", "un petit ours en peluche", 0.15)
        pharmacie.inventory["doudou"] = doudou



        
  
    
    
        
        
                 
                 
                 
                 
         # Create exits for rooms
        
        biblio.exits={"sortie":Lindsey_street,"N": None,"E": None,"O":None,"S": None, "Est": None, "Ouest": None,"Nord": None,"Sud": None,"est": None, "ouest": None,"nord": None,"sud": None}
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
    
    def _setup_commands(self):
        """Initialize all game commands."""
        self.commands["help"] = Command("help"
                                        , " : afficher cette aide"
                                        , Actions.help
                                        , 0)
        self.commands["quit"] = Command("quit"
                                        , " : quitter le jeu"
                                        , Actions.quit
                                        , 0)
        self.commands["go"] = Command("go"
                                      , "<N|E|S|O> : se déplacer dans une direction cardinale"
                                      , Actions.go
                                      , 1)
        self.commands["quests"] = Command("quests"
                                          , " : afficher la liste des quêtes"
                                          , Actions.quests
                                          , 0)
        self.commands["quest"] = Command("quest"
                                         , " <titre> : afficher les détails d'une quête"
                                         , Actions.quest
                                         , 1)
        self.commands["activate"] = Command("activate"
                                            , " <titre> : activer une quête"
                                            , Actions.activate
                                            , 1)
        self.commands["rewards"] = Command("rewards"
                                           , " : afficher vos récompenses"
                                           , Actions.rewards
                                           , 0)

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

