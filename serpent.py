"serpent.py contient une classe Serpent qui représente le serpent du joueur."
import pygame
from membre import *
from historique_coordonnees import *
from grille import *
        

    
class Serpent(pygame.sprite.Sprite):
    "Serpent du joueur"
    def __init__(self, grille:Grille, ecran:pygame.Surface):
        "Constructeur"
        # Différentes images pour la tête du serpent selon sa direction actuelle
        self.img_tetes = {
            "haut": "assets/images/teteN.png", 
            "bas": "assets/images/teteS.png",
            "gauche": "assets/images/teteW.png", 
            "droite": "assets/images/teteE.png"
            }
        
        # Nombre de mouvements effectués par le serpent
        self.n_mouvements = 0

        # Grille du jeu
        self.grille = grille
        

        # Direction dans laquelle le serpent se déplace
        self.direction = "gauche"
        self.ecran = ecran

        # Historique des coordonnées des membres du serpent
        self.historique_coords = HistoriqueCoords()

        self.taille = 3 # Taille du serpent (nombre de membres)

        self.membres = []
        # Liste des positions de chaque membre du serpent
        self.positions = []


        self.tete = Membre(self.grille, self.img_tetes["gauche"], self.ecran, 0, 0)

        # Ajouter deux premiers noeuds au serpent
        self.noeud_1 = Membre(self.grille, "assets/images/noeud1.png", self.ecran, 0, 1)
        self.noeud_2 = Membre(self.grille, "assets/images/noeud2.png", self.ecran, 0, 2)

        self.membres.extend([self.tete, self.noeud_1, self.noeud_2])
        self.positions.extend([self.grille.cartesiennes(0, 0), self.grille.cartesiennes(0, 1), self.grille.cartesiennes(0, 2)])
        self.n_mouvements += 1
        self.historique_coords.ajouter(self.positions, self.n_mouvements)

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
        # La colonne et la ligne de départ sont celles de la tête
        col_depart, ligne_depart = self.grille.coordonnees(self.tete.rect.x, self.tete.rect.y)

        positions = []

        # Si on doit aligner les membres à la verticale
        if sens == "verticale":
            for membre in self.membres:
                # Positionner le membre actuel à la verticale
                for n in range(1, self.taille + 1):
                    ligne = ligne_depart + 1
                    membre.positionner(ligne, col_depart)
                    positions.append(membre.position())
                    position_membre = membre.position()
                    self.positions.append(position_membre)


        # Si on doit aligner les membres à l'horizontale
        elif sens == "horizontale":
            for membre in self.membres:
                # Positionner le membre actuel à l'horizontale
                for n in range(1, self.taille + 1):
                    col = col_depart + 1
                    membre.positionner(ligne_depart, col)
                    positions.append(membre.position())

        return positions



    def supprimer_membres_inutiles(self) -> list:
        """Supprime les membres inutiles de la liste des membres du serpent.
        Un membre est considéré comme inutile à partir du moment où sa position est incorrecte suite à un mouvement."""

        pass        
                   


    
    def ajouter_noeuds(self, image:str, taille_max:int, ligne:int, colonne:int) -> list:
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
                noeud = Membre(self.grille, image, self.ecran, ligne, colonne)
                self.noeuds_ajoutes.append(noeud)
                self.membres.append(noeud)
                self.positions.append(noeud.position())

        # Mettre à jour la taille du serpent
        self.taille = taille_max

        return self.noeuds_ajoutes
    

    def changer_direction(self, nouvelle_direction:str) -> str:
        """Change la direction actuelle du serpent et renvoie cette dernière."""
        tete_x, tete_y = self.tete.rect.x, self.tete.rect.y
        # Tuple des direction autorisées
        directions_autorisees = ("haut", "bas", "gauche", "droite")

        assert (nouvelle_direction in directions_autorisees), "La nouvelle direction est invalide. Doit être haut, bas, gauche ou droite."

        self.direction = nouvelle_direction
        # Remplacer la tête actuelle et la mettre à jour dans la liste des membres
        if self.direction == "haut":
            print(self.direction)
            self.tete.changer_image(self.img_tetes["haut"], tete_x, tete_y)
            #self.membres.insert(0, self.tete)
            self.n_mouvements += 1

            pygame.display.update()

        elif self.direction == "bas":
            print(self.direction)
            self.tete.changer_image(self.img_tetes["bas"], tete_x, tete_y)
            #self.membres.insert(0, self.tete)
            pygame.display.update()

        elif self.direction == "gauche":
            print(self.direction)
            self.tete.changer_image(self.img_tetes["gauche"], tete_x, tete_y)
            #self.membres.insert(0, self.tete)
            pygame.display.update()

        elif self.direction == "droite":
            print(self.direction)
            self.tete.changer_image(self.img_tetes["droite"], tete_x, tete_y)
            #self.membres.insert(0, self.tete)
            pygame.display.update()

                

        return self.direction

    def deplacer_haut(self) -> None:
        "Déplace le serpent vers le haut"
        # Positions col et ligne actuelles de la tête
        col, ligne = self.grille.coordonnees(self.tete.rect.x, self.tete.rect.y)
        self.tete.positionner(ligne-1, col)



        # Position précédente de chaque membre du serpent
        self.positions_prec = [membre.position() for membre in self.membres]

        

        # Faire suivre les segments
        for i in range(1, len(self.membres)):
            # Position précédente du membre
            pos_prec = self.positions_prec[i-1]
            # Repositionner le membre
            self.membres[i].positionner(pos_prec[0]-1, pos_prec[1])


        # Supprimer les anciens membres, désormais inutiles
        """while len(self.membres) > self.taille:
            self.membres.pop()"""    

    
    def deplacer_bas(self) -> None:
        "Déplace le serpent vers le bas"
        # Positions col et ligne actuelles de la tête
        col, ligne = self.grille.coordonnees(self.tete.rect.x, self.tete.rect.y)
        self.tete.positionner(ligne+1, col)



        # Position précédente de chaque membre du serpent
        self.positions_prec = [membre.position() for membre in self.membres]

        # Faire suivre les segments
        for i in range(1, len(self.membres)):
            # Position précédente du membre
            pos_prec = self.positions_prec[i-1]
            # Repositionner le membre
            self.membres[i].positionner(pos_prec[0]+1, pos_prec[1])

        """ while len(self.membres) > self.taille:
            self.membres.pop() """


    def deplacer_gauche(self) -> None:
        "Déplace le serpent vers la gauche"
        # Positions col et ligne actuelles de la tête
        col, ligne = self.grille.coordonnees(self.tete.rect.x, self.tete.rect.y)
        self.tete.positionner(ligne, col-1)



        # Position précédente de chaque membre du serpent
        self.positions_prec = [membre.position() for membre in self.membres]


        # Faire suivre les segments
        for i in range(1, len(self.membres)):
            # Position précédente du membre
            pos_prec = self.positions_prec[i-1]
            # Repositionner le membre
            self.membres[i].positionner(pos_prec[0], pos_prec[1]-1)


        # Supprimer les anciens membres, désormais inutiles
        """while len(self.membres) > self.taille:
            self.membres.pop() """


    def deplacer_droite(self) -> None:
        "Déplace le serpent vers la droite"
         # Positions col et ligne actuelles de la tête
        col, ligne = self.grille.coordonnees(self.tete.rect.x, self.tete.rect.y)
        self.tete.positionner(ligne, col+1)


        # Position précédente de chaque membre du serpent
        self.positions_prec = [membre.position() for membre in self.membres]

        # Faire suivre les segments
        for i in range(1, len(self.membres)):
            # Position précédente du membre
            pos_prec = self.positions_prec[i-1]
            # Repositionner le membre
            self.membres[i].positionner(pos_prec[0], pos_prec[1]+1)


        # Supprimer les anciens membres, désormais inutiles

        """while len(self.membres) > self.taille:
            self.membres.pop() """

    def hors_ecran(self) -> bool:
        """Vérifie si le serpent est hors de l'écran, renvoie un booléen.
        \n Plus précisément, pour que le résultat renvoyé soit True, il faut que chaque membre du serpent ait au moins une coordonnée x ou y en dehors des limites de l'écran.
        Pour tout membre dérogeant à cette règle, la fonction renvoie False."""

        # Vérifier si chacun des membre du serpent sort de l'écran
        # Ici, on vérifie que tout memnbre du serpent a au moins une coordonnée x ou y sortant des limites de l'écran (de 0 à 700 pixels.)
        return all(any([membre.position()[0] < 0, 
                        membre.position()[1] < 0, 
                        membre.position()[0] > 700, 
                        membre.position()[1] > 700]) for membre in self.membres)

               




    def afficher(self) -> None:
        "Affiche le serpent à l'écran."
        for membre in self.membres:
            membre.afficher()




