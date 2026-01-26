# Silent Hill - Jeu d’aventure textuel

Ce dépôt contient la version finale du jeu d’aventure textuel inspiré de l’univers de Silent Hill.

Le joueur incarne un homme à la recherche de sa femme disparue dans une ville brumeuse et inquiétante. Le jeu propose déjà une exploration libre, des objets interactifs, des personnages non-joueurs (PNJ), des monstres hostiles, ainsi qu’un système de quêtes dynamiques.

Cette version constitue une base complète sur laquelle d’autres fonctionnalités pourront être ajoutées.

## Structuration

Le projet est actuellement structuré en plusieurs modules, chacun contenant une ou plusieurs classes :

- `game.py` / `Game` : boucle principale du jeu, initialisation de l’univers, gestion des conditions de victoire et de défaite  
- `room.py` / `Room`, `Cinema`, `Cave` : gestion des lieux, de leurs descriptions, sorties, inventaire et conditions d’accès (obscurité, verrouillage)  
- `player.py` / `Player` : gestion du joueur, de son inventaire, de sa santé, de ses déplacements et de ses récompenses  
- `command.py` / `Command` : structure des commandes disponibles et de leur syntaxe  
- `actions.py` / `Actions` : ensemble des commandes exécutables par le joueur (déplacement, interaction, inventaire, combat, etc.)  
- `item.py` / `Item`, `Weapon`, `Flashlight`, `Bible`, `Beamer`, `Key`, `MedKit` : objets interactifs avec des comportements spécifiques  
- `charactere.py` / `Charactere`, `Monster` : PNJ statiques ou mobiles, monstres hostiles, dialogues et IA de déplacement  
- `quest.py` contient deux classes :  
  - `Quest` : structure d’une quête, ses objectifs, sa progression et sa récompense  
  - `QuestManager` : gestion centralisée des quêtes du joueur  

## Installation

Clonez ce dépôt, puis exécutez le fichier `game.py` dans un terminal Python. Toutes les interactions se font via des commandes textuelles saisies dans le terminal.

## L’univers et la quête

Vous incarnez un homme à la recherche de sa femme disparue dans la ville brumeuse et inquiétante de Silent Hill. La ville est plongée dans le silence, peuplée de créatures monstrueuses et de personnages énigmatiques. Pour retrouver votre femme, vous devrez explorer les lieux, interagir avec les PNJ, résoudre des énigmes, et accomplir plusieurs quêtes.

## Commandes disponibles

- `help` : afficher la liste des commandes  
- `quit` : quitter le jeu  
- `go <direction>` : se déplacer (N, E, S, O, ou noms de sorties spéciales comme `sortie`, `cave`, etc.)  
- `history` : afficher l’historique des lieux visités  
- `back` : revenir à la salle précédente  
- `look` : observer les objets et personnages présents dans la pièce  
- `take <objet>` : ramasser un objet  
- `drop <objet>` : déposer un objet  
- `check` : consulter l’inventaire  
- `carry <objet>` : équiper un objet  
- `use` : utiliser l’objet actuellement équipé  
- `read <objet>` : lire un objet lisible (lettre, flyer, bible…)  
- `talk <personnage>` : parler à un PNJ  
- `give <objet>` : donner un objet à un PNJ  
- `quests` : afficher la liste des quêtes  
- `quest <titre>` : afficher les détails d’une quête  
- `activate <titre>` : activer une quête  
- `rewards` : afficher les récompenses obtenues  

## Lieux

Le jeu comprend plus d’une dizaine de lieux interconnectés, chacun avec son ambiance, ses objets, ses personnages et ses secrets. Quelques exemples :

- Neely Street : point de départ du joueur  
- Cinéma abandonné : plongé dans l’obscurité, nécessite une lampe torche pour être exploré  
- Bar, Pharmacie, Église, Parc pour enfants, Hôtel, Cave : chacun avec ses propres mystères, objets et dangers  

Certains lieux sont verrouillés ou plongés dans le noir, nécessitant des objets spécifiques (clé, lampe torche, code secret) pour y accéder.

## Personnages et objets

- Des PNJ statiques (fillette, barman) ou hostiles (monstres) peuplent la ville  
- Les monstres se déplacent aléatoirement et peuvent attaquer le joueur  
- Les objets sont variés : armes, soins, indices, objets de quête, etc.  
- Certains objets ont des effets spéciaux (lampe torche éclaire les pièces sombres, bible révèle un indice caché, beamer permet de se téléporter…)  

## Quêtes

Le jeu comporte plusieurs quêtes principales et secondaires, activables via les interactions ou les objets. Exemples :

- Retrouver le doudou : aider une fillette à retrouver son doudou  
- Réussir le défi du barman : deviner un nombre secret dans un mini-jeu  
- Trouver l’hôtel : localiser un lieu important  
- Sauver votre femme : quête principale finale  

Les quêtes sont gérées dynamiquement via le `QuestManager`, avec suivi des objectifs, progression et récompenses.

## Conditions de victoire et de défaite

- Victoire : toutes les quêtes principales sont complétées et le joueur atteint la cave pour retrouver sa femme  
- Défaite : le joueur meurt (PV à 0) ou échoue à entrer le bon code dans la cave après 10 essais  

## Guide développeur

L’architecture du jeu repose sur une structure orientée objet claire et modulaire. Chaque entité (joueur, pièce, objet, quête, PNJ) est représentée par une classe dédiée. Le moteur du jeu (`Game`) orchestre les interactions entre ces entités.

Voici un diagramme de classes permettant de comprendre l'organisation des différentes classes :

## Perspectives de développement

- Ajout d’une interface graphique (images, boutons, navigation visuelle)  
- Nouvelles salles, objets, monstres et quêtes pour enrichir l’univers  
- Salles spéciales (pièces cachées, énigmes lumineuses, portes secrètes)  
- Dialogues conditionnels selon les objets, quêtes ou interactions passées  
- Système de sauvegarde/chargement de partie  
- Succès cachés ou fins alternatives selon les choix du joueur  
