"serpent.py contient une classe Serpent qui représente le serpent du joueur."
import pygame
from membre import *
        

    
class Serpent(pygame.sprite.Sprite):
    "Serpent du joueur"
    def __init__(self, ecran:pygame.Surface):
        "Constructeur"
        # Différentes images pour la tête du serpent
        self.img_tetes = ["assets/images/tete.png", "assets/images/teteE.png", "assets/images/teteN.png",
                      "assets/images/teteS.png", "assets/images/teteW.png"]
        

        # Direction dans laquelle le serpent se déplace
        self.direction = "gauche"
        self.ecran = ecran

        self.taille = 3 # Taille du serpent (nombre de membres)

        self.membres = []
        self.tete = Membre(self.img_tetes[0], self.ecran, 0, 0)

        # Ajouter deux premiers noeuds au serpent
        self.noeud_1 = Membre("assets/images/noeud1.png", self.ecran, 10, 10)
        self.noeud_2 = Membre("assets/images/noeud2.png", self.ecran, 10, 10)

        self.membres.append(self.tete)
        self.membres.append(self.noeud_1)
        self.membres.append(self.noeud_2)

    def charger_tete(self, fichier:str) -> pygame.Surface:
        "Charge une tête du serpent depuis un fichier PNG ou JPG, renvoie la surface correspondante."

        # Assertions
        assert (type(fichier).__name__ == "str"), "Le chemin du fichier image doit être une chaîne de caractères."
        assert (any([fichier.endswith(".png"), fichier.endswith(".jpg")])), "Le fichier image doit avoir l'extension .png ou .jpg"

        # Charger le fichier image de la tête
        return pygame.image.load(fichier)
    

    def ajuster_membres(self, sens="verticale") -> list:
        """"Ajuste (aligne) les membres du serpent et renvoie la liste des positions actualisée.
        sens: direction de l'alignement (verticale ou horizontale)."""
        # Le x et le y de départ sont ceux de la tête
        x_depart = self.tete.rect.x
        y_depart = self.tete.rect.y

        positions = []

        # Si on doit aligner les membres à la verticale
        if sens == "verticale":
            for membre in self.membres:
                # Positionner le membre actuel à la verticale
                for n in range(1, self.taille + 1):
                    y  = y_depart + 20 * n
                    membre.positionner_y(y)
                    positions.append(membre.position())

        # Si on doit aligner les membres à l'horizontale
        elif sens == "horizontale":
            for membre in self.membres:
                # Positionner le membre actuel à l'horizontale
                for n in range(1, self.taille + 1):
                    x = x_depart + 20 * n
                    membre.positionner_x(x)
                    positions.append(membre.position())

        return positions        
                   


    
    def ajouter_noeuds(self, taille_max:int) -> list:
        """Ajoute de nouveaux noeuds au serpent jusqu'à atteindre la taille taille_max. Retourne la liste des surfaces correspondantes à ces nouveaux noeuds."""

        # Assertions
        assert (type(taille_max).__name__ == "int"), "taille_max doit être un nombre entier"
        assert (taille_max > self.taille), "taille_max doit être supérieure à la taille actuelle du serpent"

        # Liste des fichiers image représentant des noeuds
        images_noeuds = ["assets/images/noeud1.png", "assets/images/noeud2.png"]

        self.noeuds_ajoutes = []
        # Charger et ajouter les nouveaux noeuds
        for i in range(self.taille, taille_max + 1):
            for n in range(len(images_noeuds)):
                # Image du nouveau noeud actuel
                noeud = pygame.image.load(images_noeuds[n])
                self.noeuds_ajoutes.append(noeud)
                self.membres.append(noeud)

        # Mettre à jour la taille du serpent
        self.taille = taille_max

        return self.noeuds_ajoutes
    

    def changer_direction(self, nouvelle_direction:str) -> str:
        """Change la direction actuelle du serpent et renvoie cette dernière."""

        # Tuple des direction autorisées
        directions_autorisees = ("haut", "bas", "gauche", "droite")

        assert (nouvelle_direction in directions_autorisees), "La nouvelle direction est invalide. Doit être haut, bas, gauche ou droite."

        self.direction = nouvelle_direction
        return self.direction

    def deplacer_haut(self):
        "Déplace le serpent vers le haut"
        # Positions x et y actuelles de la tête
        tete_x, tete_y = self.tete.rect.x, self.tete.rect.y
        # Remplacer la tête actuelle et la mettre à jour dans la liste des membres
        self.tete = Membre("assets/images/teteN.png", self.ecran, tete_x, tete_y)
        self.tete.positionner_y(tete_y - 5)
        self.membres[0] = self.tete

        # Position précédente de chaque membre du serpent
        self.positions_prec = [membre.position() for membre in self.membres]

        

        # Faire suivre les segments
        for i in range(1, len(self.membres)):
            # Position précédente du membre
            pos_prec = self.positions_prec[i-1]
            # Repositionner le membre
            self.membres[i].positionner_x(pos_prec[0])
            self.membres[i].positionner_y(pos_prec[1])




    def afficher(self):
        for membre in self.membres:
            membre.afficher()




