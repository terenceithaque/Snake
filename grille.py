"grille.py représente la grille de jeu"
import pygame

class Grille:
    "Grille du jeu"
    def __init__(self, contenu: list, x1:int, x2:int,y1:int, y2:int, marge:int, taille:int, ecran:pygame.Surface) -> None:
        """Constructeur de la grille.
        - contenu: contenu de la grille
        - x1: position x à laquelle l'affichage commence
        - x2: fin de l'affichage
        - y1: position y de début de l'affichage
        - y2: fin de l'affichage
        - ecran: surface d'affichage."""
        

        self.contenu = contenu

        self.taille = taille

        # Surface d'affichage
        self.ecran = ecran

        # Marge entre les cases de la grille
        self.marge = marge

        self.hauteur_case = 70
        self.largeur_case = 50

        # Positions x et y de départ
        self.x1 = x1
        self.y1 = y1

        # Positions x et y de fin
        self.x2 = x2
        self.y2 = y2

    def afficher(self):
        "Affiche la grille"

        for i in range(self.taille):
            for y in range(self.taille + 1):
                pygame.draw.line(self.ecran, (128, 128, 128), (0, y*self.hauteur_case + self.marge), (self.taille*(self.largeur_case + self.marge), (y*self.hauteur_case+self.marge)), 10)


            for j in range(self.taille + 1):
                pygame.draw.line(self.ecran, (128, 128, 128), (j * (self.largeur_case + self.marge), 0), 
                             (j * (self.largeur_case + self.marge), self.taille * (self.hauteur_case + self.marge)), 10)     
