"membre.py contient une classe Membre représentant un membre du coprs du serpent indépendant des autres."
import pygame
from grille import *


class Membre(pygame.sprite.Sprite):
    "Un membre du serpent"
    def __init__(self, grille:Grille, image:str, ecran:pygame.Surface, ligne:int, col:int) -> None:
        """Constructeur du membre.
        
        - image : chemin du fichier image représentant le membre
        - ecran : surface d'affichage du membre
        - ligne: entier, position ligne de départ du membre
        - col : entier, position col de départ du membre."""


        super().__init__()
        # Surface d'affichage du membre
        self.ecran = ecran

        # Grille du jeu
        self.grille = grille

        # Charger l'image du membre

        self.chemin_image = image
        self.image = pygame.image.load(self.chemin_image)
        self.rect = self.image.get_rect()


        # Identifiant du membre dans la grille de jeu
        self.identifiant = 1

        # Position du membre dans la grille
        self.ligne = ligne
        self.col = col
        # Position du membre en pixels
        self.coords_cartesiennes = self.grille.cartesiennes(self.ligne, self.col, centrer=True)
        self.rect.x = self.coords_cartesiennes[0]
        self.rect.y = self.coords_cartesiennes[1]


    def changer_image(self, fichier:str, x:int, y:int) -> None:
        "Change l'image actuelle du membre pour le contenu du fichier image indiqué"
        self.chemin_image = fichier
        self.image = pygame.image.load(self.chemin_image)
        self.rect = self.image.get_rect()

        # Position du membre sur l'écran
        self.rect.x = x
        self.rect.y = y    


    def positionner(self, ligne=0, col=0) -> int:
        "Change les positions (ligne, col) du membre pour la valeur d'absisce spécifiée, 0 par défaut."
        self.coords_cartesiennes = self.grille.cartesiennes(ligne, col, centrer=True)
        self.rect.x = self.coords_cartesiennes[0]
        self.rect.y = self.coords_cartesiennes[1]
        return self.rect.x
    
    def position(self) -> tuple:
        "Renvoie la position actuelle du membre sous forme de tuple."
        return (self.rect.x, self.rect.y)

    def afficher(self):
        "Affiche le membre à l'écran."
        self.ecran.blit(self.image, (self.rect.x, self.rect.y))    
