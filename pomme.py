"pomme.py contient la classe Pomme, représentant une pomme consommable"
# Importations nécessaires
import pygame
import random


class Pomme(pygame.sprite.Sprite):
    "Une pomme consommable par le joueur"
    def __init__(self, x1:int, y1:int, x2:int, y2:int, image:str, ecran:pygame.Surface) -> None:
        """Constructeur de la pomme apparaissant à des coordonnées aléatoires.
        
        - x1: Coordonnée x minimale de la pomme dans l'intervalle de tirage
        - y1: Coordonnée y minimale de la pomme dans l'intervalle de tirage
        - x2: Coordonnée x maximale de la pomme dans l'intervalle de tirage
        - y2: Coordonnée y maximale de la pomme dans l'intervalle de tirage
        - image: chemin du fichier image représentant la pomme
        - ecran: surface d'affichage de la pomme."""

        super().__init__()
        # Surface d'affichage de la pomme
        self.ecran = ecran


        # Identifiant de la pomme
        self.identifiant = 2


        # Image de la pomme
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()


        # Tirage au hasard des coordonnées de la pomme
        self.rect.x = random.randint(x1, x2)
        self.rect.y = random.randint(y1, y2)


    def afficher(self) -> None:
        "Affiche la pomme à l'écran"
        self.ecran.blit(self.image, (self.rect.x, self.rect.y))    
