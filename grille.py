"grille.py représente la grille de jeu"
import pygame

class Grille:
    "Grille du jeu"
    def __init__(self, contenu: list, x1:int, x2:int,y1:int, y2:int, marge:int, taille:int, ecran:pygame.Surface) -> None:
        """Constructeur de la grille.
        - contenu: contenu de la grille
        - x1: position x à laquelle l'affichage commence
        - x2: fin de l'affichage
        - y1: position y de début de l'affichage
        - y2: fin de l'affichage
        - taille: taille de la grille
        - ecran: surface d'affichage."""
        

        self.contenu = contenu

        self.taille = taille



        # Surface d'affichage
        self.ecran = ecran

        # Marge entre les cases de la grille
        self.marge = marge

        self.hauteur_case = 70
        self.largeur_case = 50

        # Positions x et y de départ
        self.x1 = x1
        self.y1 = y1

        # Positions x et y de fin
        self.x2 = x2
        self.y2 = y2

    def objet_dans_case(self, ligne=0, col=0, identifiant=1) -> tuple:
        """Vérifie l'objet dans la case spécifiée à l'aide de son identifiant.
        
        Si l'identifiant est:
            - 1: c'est un membre du serpent
            - 2: c'est une pomme
            
        Renvoie un tuple (id_objet, booleen_de_resultat)"""


        if self.contenu[ligne][col] == identifiant:
            return (identifiant, True)
        
        else:
            return (identifiant, False)
        

    def cartesiennes(self, ligne=0, col=0, centrer=True) -> tuple:
        """Renvoie les coordonnées cartésiennes correspondantes à la case (ligne, col) sous forme de tuple.
        
        - ligne: numéro de la ligne
        - col: numéro de la colonne
        - centrer: booléen True par défaut. Si actif, considère que la position d'une case constitue son plein centre. Si False, la position devient la bordure de celle-ci."""
        x = self.x1 + col * (self.largeur_case + self.marge)
        y = self.y1 + ligne * (self.hauteur_case + self.marge)

        

        if centrer:
            x += self.largeur_case // 2
            y += self.hauteur_case // 2
        
        print(f"[DEBUG cartesiennes] ligne={ligne}, col={col}, → x={x}, y={y}")
        return (x, y)

    def coordonnees(self, x=0, y=0) -> tuple:
        """Renvoie les coordonnées de la case (ligne, col) à partir de coordonnées cartésiennes."""
        ligne = y // self.hauteur_case
        col = x // self.largeur_case
        
        
        return (ligne, col) 



    def afficher(self):
        "Affiche la grille"

        for i in range(self.taille):
            for y in range(self.taille):
                pygame.draw.line(self.ecran, (128, 128, 128), (0, y*self.hauteur_case + self.marge), (self.taille*(self.largeur_case + self.marge), (y*self.hauteur_case+self.marge)), 10)


            for j in range(self.taille):
                pygame.draw.line(self.ecran, (128, 128, 128), (j * (self.largeur_case + self.marge), 0), 
                             (j * (self.largeur_case + self.marge), self.taille * (self.hauteur_case + self.marge)), 10)     
