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



        self.tete = self.ajouter_membre(self.grille, self.ecran, self.img_tetes["gauche"], 7, 7, True)
        self.noeud_1 = self.ajouter_membre(self.grille, self.ecran,"assets/images/noeud1.png" , 7, 8)
        self.noeud_2 = self.ajouter_membre(self.grille, self.ecran, "assets/images/noeud2.png", 7, 9)

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

        self.tete = self.obtenir_tete()
        # Le x et le y de départ sont ceux de la tête
        ligne_depart, col_depart = self.grille.coordonnees(self.tete.rect.x, self.tete.rect.y)


        positions = []

        # Si on doit aligner les membres à la verticale
        
        for n, membre in enumerate(self.membres, start=1):
            if sens == "verticale":
                ligne = ligne_depart + n
                col = col_depart


            # Si on doit aligner les membres à l'horizontale
            elif sens == "horizontale":
                ligne = ligne_depart
                col = col_depart + n

            else:
                ligne_depart = ligne_depart
                col = col_depart    

        membre.positionner(ligne, col)
        positions.append((ligne, col))
        return positions
    

    def obtenir_tete(self)-> Membre:
        "Renvoie la tête du serpent"
        return self.membres[0]



    def supprimer_membres_inutiles(self) -> list:
        """Supprime les membres inutiles de la liste des membres du serpent.
        Un membre est considéré comme inutile à partir du moment où sa position est incorrecte suite à un mouvement."""

        pass        
                   


    
    """def ajouter_noeuds(self, taille_max:int) -> list:
        "Ajoute de nouveaux noeuds au serpent jusqu'à atteindre la taille taille_max. Retourne la liste des surfaces correspondantes à ces nouveaux noeuds."

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

        return self.noeuds_ajoutes"""
    

    def ajouter_membre(self, grille:Grille, ecran:pygame.Surface, image:str, ligne=0, col=0, est_tete = False) -> Membre:
        """Ajoute un membre au serpent.
        
        Les propriétés acceptées sont:
        
            - grille: grille du jeu où afficher le membre
            - ecran: surface d'affichage du membre
            - image: fichier image du membre
            - ligne: ligne de position du membre
            - col : colonnne de position du membre.
            - est_tete: booléen, False par défaut. Si activé, le nouveau membre est considéré comme la tête du serpent
            
            Les coordonnées ligne et col sont automatiquement converties en coordonnées cartésiennes. La liste des membres est automatiquement mise à jour. Renvoie un objet Membre"""
        
        nouveau_membre = Membre(grille, image, ecran, ligne, col)
        if est_tete:
            self.membres.insert(0, nouveau_membre)
        else:    
            self.membres.append(nouveau_membre)

        return nouveau_membre
    

    def changer_direction(self, nouvelle_direction:str) -> str:
        """Change la direction actuelle du serpent et renvoie cette dernière."""
        self.tete = self.obtenir_tete()
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

            #pygame.display.update()

        elif self.direction == "bas":
            print(self.direction)
            self.tete.changer_image(self.img_tetes["bas"], tete_x, tete_y)
            #self.membres.insert(0, self.tete)
            #pygame.display.update()

        elif self.direction == "gauche":
            print(self.direction)
            self.tete.changer_image(self.img_tetes["gauche"], tete_x, tete_y)
            #self.membres.insert(0, self.tete)
            #pygame.display.update()

        elif self.direction == "droite":
            print(self.direction)
            self.tete.changer_image(self.img_tetes["droite"], tete_x, tete_y)
            #self.membres.insert(0, self.tete)
            #pygame.display.update()

                

        return self.direction

    def deplacer_haut(self) -> None:
        "Déplace le serpent vers le haut"


        self.tete = self.obtenir_tete()

        # Position précédente de chaque membre du serpent
        self.positions_prec = [membre.position() for membre in self.membres]
        #print(f"Positions précédentes : {self.positions_prec}")


        # Positions x et y actuelles de la tête
        ligne_tete = self.grille.coordonnees(self.tete.rect.x, self.tete.rect.y)[0]
        col_tete = self.grille.coordonnees(self.tete.rect.x, self.tete.rect.y)[1]
        self.tete.positionner(ligne_tete-1, col_tete)





        

        # Faire suivre les segments
        for i in range(1, len(self.membres)):
            # Position précédente du membre
            pos_prec = self.positions_prec[i-1]
            # Repositionner le membre
            self.membres[i].positionner(pos_prec[0], pos_prec[1])


        # Supprimer les anciens membres, désormais inutiles
        """while len(self.membres) > self.taille:
            self.membres.pop()"""    

    
    def deplacer_bas(self) -> None:
        "Déplace le serpent vers le bas"
        # Positions x et y actuelles de la tête

        self.tete = self.obtenir_tete()


        # Position précédente de chaque membre du serpent
        self.positions_prec = [membre.position() for membre in self.membres]
        #print(f"Positions précédentes : {self.positions_prec}")


        ligne_tete = self.grille.coordonnees(self.tete.rect.x, self.tete.rect.y)[0]
        col_tete = self.grille.coordonnees(self.tete.rect.x, self.tete.rect.y)[1]
        self.tete.positionner(ligne_tete+1, col_tete)


        # Faire suivre les segments
        for i in range(1, len(self.membres)):
            # Position précédente du membre
            pos_prec = self.positions_prec[i-1]
            # Repositionner le membre
            self.membres[i].positionner(pos_prec[0], pos_prec[1])
        """ while len(self.membres) > self.taille:
            self.membres.pop() """


    def deplacer_gauche(self) -> None:
        "Déplace le serpent vers la gauche"


        self.tete = self.obtenir_tete()

        # Position précédente de chaque membre du serpent
        self.positions_prec = [membre.position() for membre in self.membres]
        #print(f"Positions précédentes : {self.positions_prec}")


        # Positions x et y actuelles de la tête
        ligne_tete = self.grille.coordonnees(self.tete.rect.x, self.tete.rect.y)[0]
        col_tete = self.grille.coordonnees(self.tete.rect.x, self.tete.rect.y)[1]
        self.tete.positionner(ligne_tete, col_tete-1)



        


        # Faire suivre les segments
        for i in range(1, len(self.membres)):
            # Position précédente du membre
            pos_prec = self.positions_prec[i-1]
            # Repositionner le membre
            self.membres[i].positionner(pos_prec[0], pos_prec[1])


        # Supprimer les anciens membres, désormais inutiles
        """while len(self.membres) > self.taille:
            self.membres.pop() """


    def deplacer_droite(self) -> None:
        "Déplace le serpent vers la droite"

        self.tete = self.obtenir_tete()
        # Position précédente de chaque membre du serpent
        self.positions_prec = [membre.position() for membre in self.membres]
        #print(f"Positions précédentes : {self.positions_prec}")


        # Positions x et y actuelles de la tête
        ligne_tete = self.grille.coordonnees(self.tete.rect.x, self.tete.rect.y)[0]
        col_tete = self.grille.coordonnees(self.tete.rect.x, self.tete.rect.y)[1]
        self.tete.positionner(ligne_tete, col_tete+1)

        # Faire suivre les segments
        for i in range(1, len(self.membres)):
            # Position précédente du membre
            pos_prec = self.positions_prec[i-1]
            # Repositionner le membre
            self.membres[i].positionner(pos_prec[0], pos_prec[1])

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




