"serpent.py contient une classe Serpent qui représente le serpent du joueur."
import pygame

class Serpent(pygame.sprite.Sprite):
    "Serpent du joueur"
    def __init__(self):
        "Constructeur"
        # Différentes images pour la tête du serpent
        self.img_tetes = ["assets/images/tete.png", "assets/images/teteE.png", "assets/images/teteN.png",
                      "assets/images/teteS.png", "assets/images/teteW.png"]
        

        self.tete = self.charger_tete(self.img_tetes[0])

        self.rects = []
        self.rect_tete = self.tete.get_rect()
        self.rects.append(self.rect_tete)

        # Liste des positions du serpent
        self.positions = []
        self.positions.append((self.rect_tete.x, self.rect_tete.y))

        # Ajouter deux premiers noeuds au serpent
        self.noeud_1 = pygame.image.load("assets/images/noeud1.png")
        self.noeud_2 = pygame.image.load("assets/images/noeud2.png")


    def charger_tete(self, fichier:str) -> pygame.Surface:
        "Charge une tête du serpent depuis un fichier PNG ou JPG, renvoie la surface correspondante."

        # Assertions
        assert (type(fichier).__name__ == "str"), "Le chemin du fichier image doit être une chaîne de caractères."
        assert (any([fichier.endswith(".png"), fichier.endswith(".jpg")])), "Le fichier image doit avoir l'extension .png ou .jpg"

        # Charger le fichier image de la tête
        return pygame.image.load(fichier)

