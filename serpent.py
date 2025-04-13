"serpent.py contient une classe Serpent qui représente le serpent du joueur."
import pygame

class Serpent(pygame.sprite.Sprite):
    "Serpent du joueur"
    def __init__(self):
        "Constructeur"
        # Différentes images pour la tête du serpent$
        self.tetes = ["assets/images/tete.png", "assets/images/teteE.png", "assets/images/teteN.png",
                      "assets/images/teteS.png", "assets/images/teteW.png"]