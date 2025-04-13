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


    def charger_tete(self, fichier:str) -> pygame.Surface:
        "Charge une tête du serpent depuis un fichier PNG ou JPG, renvoie la surface correspondante."

        # Assertions
        assert (type(fichier).__name__ == "str"), "Le chemin du fichier image doit être une chaîne de caractères."
        assert (any([fichier.endswith(".png"), fichier.endswith(".jpg")])), "Le fichier image doit avoir l'extension .png ou .jpg"

        # Charger le fichier image de la tête
        return pygame.image.load(fichier)

