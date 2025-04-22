"membre.py contient une classe Membre représentant un membre du coprs du serpent indépendant des autres."
import pygame
from grille import *


class Membre(pygame.sprite.Sprite):
    "Un membre du serpent"
    def __init__(self, grille:Grille, image:str, ecran:pygame.Surface, ligne:int, col:int) -> None:
        """Constructeur du membre.
        
        - image : chemin du fichier image représentant le membre
        - ecran : surface d'affichage du membre
        - ligne: entier, ligne de départ du membre
        - col : entier, colonne de départ du membre."""


        super().__init__()
        # Surface d'affichage du membre
        self.ecran = ecran


        # Grille du jeu
        self.grille = grille

        # Charger l'image du membre
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()


        # Identifiant du membre dans la grille de jeu
        self.identifiant = 1

        # Position du membre sur l'écran en coordonnées cartésiennes
        self.rect.x, self.rect.y = self.grille.cartesiennes(ligne, col)
        

        # Coordonnées (ligne, col) du membre
        self.ligne, self.col = self.grille.coordonnees(self.rect.x, self.rect.y)


    def changer_image(self, fichier:str, x:int, y:int) -> None:
        "Change l'image actuelle du membre pour le contenu du fichier image indiqué"
        self.image = pygame.image.load(fichier)
        self.rect = self.image.get_rect()

        # Position du membre sur l'écran
        self.rect.x = x
        self.rect.y = y

        # Coordonnées (ligne, col) du membre
        self.ligne, self.col = self.grille.coordonnees(self.rect.x, self.rect.y)    


    def positionner(self, ligne=0, col=0) -> tuple:
        """Positionne le membre aux coordonnées (ligne, col)."""
        x, y = self.grille.cartesiennes(ligne, col)
        print(x)
        print(type(x), type(y))
        self.rect.x = x
        self.rect.y =y
        return (self.rect.x, self.rect.y)

    
    def position(self) -> tuple:
        "Renvoie la position actuelle du membre dans la grille sous forme de tuple."
        return self.grille.coordonnees(self.rect.x, self.rect.y)

    def afficher(self):
        "Affiche le membre à l'écran."
        self.ecran.blit(self.image, (self.rect.x, self.rect.y))    
