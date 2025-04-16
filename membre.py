"membre.py contient une classe Membre représentant un membre du coprs du serpent indépendant des autres."
import pygame


class Membre(pygame.sprite.Sprite):
    "Un membre du serpent"
    def __init__(self, image:str, ecran:pygame.Surface, x:int, y:int) -> None:
        """Constructeur du membre.
        
        - image : chemin du fichier image représentant le membre
        - ecran : surface d'affichage du membre
        - x: entier, position x de départ du membre
        - y : entier, position y de départ du membre."""

        # Surface d'affichage du membre
        self.ecran = ecran

        # Charger l'image du membre
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

        # Position du membre sur l'écran
        self.rect.x = x
        self.rect.y = y


    def positionner_x(self, x=0) -> int:
        "Change la position x du membre pour la valeur d'absisce spécifiée, 0 par défaut."
        self.rect.x = x
        return self.rect.x

    def positiionner_y(self, y=0) -> int:
        "Change la position y du membre pour la valeur d'ordonnée spécifiée, 0 par défaut."
        self.rect.y = y
        return self.rect.y

    def afficher(self):
        "Affiche le membre à l'écran."
        self.ecran.blit(self.image, (self.rect.x, self.rect.y))    
