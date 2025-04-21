"grille.py représente la grille de jeu"
import pygame

class Grille:
    "Grille du jeu"
    def __init__(self, x1:int, x2:int,y1:int, y2:int, marge:int, ecran:pygame.Surface) -> None:
        """Constructeur de la grille.
        
        - x1: position x à laquelle l'affichage commence
        - x2: fin de l'affichage
        - y1: position y de début de l'affichage
        - y2: fin de l'affichage
        - ecran: surface d'affichage."""