"membre.py contient une classe Membre représentant un membre du coprs du serpent indépendant des autres."
import pygame


class Membre(pygame.sprite.Sprite):
    "Un membre du serpent"
    def __init__(self, image:str, ecran:pygame.Surface):
        """Constructeur du membre.
        
        - image : chemin du fichier image représentant le memlbre
        - ecran : surface d'affichage du membre."""

        # Surface d'affichage du membre
        self.ecran = ecran

        # Charger l'image du membre
        self.image = pygame.image.load(image)