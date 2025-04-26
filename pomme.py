"pomme.py contient la classe Pomme, représentant une pomme consommable"
# Importations nécessaires
import pygame
import random
from grille import *


class Pomme(pygame.sprite.Sprite):
    "Une pomme consommable par le joueur"
    def __init__(self, grille:Grille, ligne_min:int, col_min:int, ligne_max:int, col_max:int, image:str, ecran:pygame.Surface) -> None:
        """Constructeur de la pomme apparaissant à des coordonnées aléatoires.
        
        - grille: grille du jeu où afficher la pomme
        - ligne_min: Coordonnée ligne minimale de la pomme dans l'intervalle de tirage
        - col_min: Coordonnée col minimale de la pomme dans l'intervalle de tirage
        - ligne_max: Coordonnée ligne maximale de la pomme dans l'intervalle de tirage
        - col_max: Coordonnée col maximale de la pomme dans l'intervalle de tirage
        - image: chemin du fichier image représentant la pomme
        - ecran: surface d'affichage de la pomme."""

        super().__init__()
        # Surface d'affichage de la pomme
        self.ecran = ecran




        # Grille du jeu
        self.grille = grille


        # Image de la pomme
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()


        # Tirage au hasard des coordonnées de la pomme
        self.ligne = random.randint(ligne_min, ligne_max)
        self.col = random.randint(col_min, col_max)

        # Placer la pomme dans la grille
        #self.grille.placer_objet(self.identifiant, self.ligne, self.col)


        # Coordonnées cartésiennes de la pomme
        self.coords_cartesiennes = self.grille.cartesiennes(self.ligne, self.col, centrer=True)
        self.rect.x = self.coords_cartesiennes[0]
        self.rect.y = self.coords_cartesiennes[1]

        print(f"Pomme placée en {(self.rect.x, self.rect.y)}, soit {self.grille.coordonnees(self.rect.x, self.rect.y)} dans la grille")


    def afficher(self) -> None:
        "Affiche la pomme à l'écran"
        self.ecran.blit(self.image, (self.rect.x, self.rect.y))    
